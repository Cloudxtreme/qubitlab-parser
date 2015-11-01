#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re


class QblMemoryBuilder:

    def __init__(self, qbl_memory):
        self.qbl_memory = qbl_memory
        self.qbl_memory_new_data = {}

    def get_qbl_memory_new_data(self, ast_tree):
        self.qbl_memory_new_data = {}
        self.get_root_objects(ast_tree)
        return self.qbl_memory_new_data

    def get_root_objects(self, ast_tree):
        for ast_node in ast_tree:
            variable = self.get_qbl_object(ast_node)
            self.append_qbl_object(variable)

    def get_qbl_object(self, ast_node):
        qbl_object = None
        if 'create_qstate' == ast_node['pattern_key']:
            qbl_object = self.get_qstate(ast_node)
        if 'create_gate' == ast_node['pattern_key']:
            qbl_object = self.get_gate(ast_node)
        if 'create_circuit' == ast_node['pattern_key']:
            qbl_object = self.get_circuit(ast_node)
        if 'merge_circuits' == ast_node['pattern_key']:
            qbl_object = self.get_circuit_merge(ast_node)
        return qbl_object

    def append_qbl_object(self, qbl_object):
        self.qbl_memory_new_data[qbl_object['name']] = {
            'type': qbl_object['type'],
            'value': qbl_object['value']
        }

    @staticmethod
    def get_qstate(ast_node):
        value = ast_node['children'][0]['args']['value']
        value = value.strip()
        return {
            'name': ast_node['args']['variable_name'],
            'type': 'qstate',
            'value': value
        }

    @staticmethod
    def get_gate(ast_node):
        matrix = []
        for node_child in ast_node['children']:
            vector = node_child['args']['vector_values']
            vector_values = re.split(' *, *', vector)
            matrix.append(vector_values)
        return {
            'name': ast_node['args']['variable_name'],
            'type': 'gate',
            'value': matrix
        }

    def get_circuit(self, ast_node):
        data = {'input': [], 'steps': []}
        circuit_children = ast_node['children']
        for child in circuit_children:
            if 'define_input' == child['pattern_key']:
                data['input'] = self.get_circuit_input(child)
            elif 'define_step' == child['pattern_key']:
                data['steps'].append(self.get_circuit_step(child))
        return {
            'name': ast_node['args']['variable_name'],
            'type': 'circuit',
            'value': data
        }

    @staticmethod
    def get_circuit_input(input_node):
        data = []
        for input_item in input_node['children']:
            data.append(input_item['args'])
        return data

    @staticmethod
    def get_circuit_step(step_node):
        data = []
        for step_item in step_node['children']:
            data.append(step_item['args'])
        return data

    def get_circuit_merge(self, ast_node):
        variable_names = re.split(" *\+ *", ast_node['args']['circuit_merge_expression'])
        circuits_to_merge = []
        for name in variable_names:
            circuits_to_merge.append(self.get_variable_data(ast_node, name, 'circuit'))

        data = self.merge_circuits(circuits_to_merge)
        return {
            'name': ast_node['args']['variable_name'],
            'type': 'circuit',
            'value': data
        }

    @staticmethod
    def merge_circuits(circuits):
        data = {'input': [], 'steps': []}
        if 'input' in circuits[0]['value']:
            data['input'] = circuits[0]['value']['input']
        for circ in circuits:
            data['steps'] += circ['value']['steps']
        return data

    def get_variable_data(self, expression_node, variable_name, excepted_type):
        if self.valid_variable(expression_node, variable_name, excepted_type):
            if variable_name in self.qbl_memory_new_data:
                return self.qbl_memory_new_data[variable_name]
            elif variable_name in self.qbl_memory.qbl_objects:
                return self.qbl_memory.qbl_objects[variable_name]

    def valid_variable(self, expression_node, variable_name, excepted_type):
        if variable_name in self.qbl_memory_new_data:
            if self.qbl_memory_new_data[variable_name]['type'] == excepted_type:
                return True
            else:
                raise SyntaxError('variable "' + variable_name + '" must by type of "' +
                                  excepted_type + '", line ' + str(expression_node['line_number']))
        if variable_name in self.qbl_memory.qbl_objects:
            if self.qbl_memory.qbl_objects[variable_name]['type'] == excepted_type:
                return True
            else:
                raise SyntaxError('variable "' + variable_name + '" must by type of "' +
                                  excepted_type + '", line ' + str(expression_node['line_number']))
        raise SyntaxError('variable "' + variable_name + '" isn\'t set, line ' + str(expression_node['line_number']))

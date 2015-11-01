#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re


class QblMemoryBuilder:

    def __init__(self):
        self.qbl_memory_data = {}

    def get_qbl_memory_data(self, ast_tree):
        self.qbl_memory_data = {}
        self.get_root_objects(ast_tree)
        return self.qbl_memory_data

    def get_root_objects(self, ast_tree):
        for ast_node in ast_tree:
            variable = self.get_variable(ast_node)
            self.append_variable(variable)

    def get_variable(self, ast_node):
        variable = None
        if 'create_qstate' == ast_node['pattern_key']:
            variable = self.get_qstate(ast_node)
        if 'create_gate' == ast_node['pattern_key']:
            variable = self.get_gate(ast_node)
        if 'create_circuit' == ast_node['pattern_key']:
            variable = self.get_circuit(ast_node)
        if 'merge_circuits' == ast_node['pattern_key']:
            variable = self.get_circuit_merge(ast_node)
        return variable

    def append_variable(self, variable):
        self.qbl_memory_data[variable['name']] = {
            'type': variable['type'],
            'value': variable['value']
        }

    @staticmethod
    def get_qstate(ast_node):
        value = ast_node['children'][0]['args']['value']
        value = value.strip()
        return {
            'name': ast_node['args']['variable_name'],
            'type': 'QubitState',
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
            'type': 'Gate',
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
            'type': 'Circuit',
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

    @staticmethod
    def get_circuit_merge(ast_node):
        data = ast_node['args']['circuit_merge_expression']
        return {
            'name': ast_node['args']['variable_name'],
            'type': 'Circuit',
            'value': data
        }

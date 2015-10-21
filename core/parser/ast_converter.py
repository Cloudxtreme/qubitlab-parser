#!/usr/bin/env python
# -*- coding: utf-8 -*-


class AstConverter:

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
        if 'create_qubit_state' == ast_node['pattern_key']:
            variable = self.get_qubit_state(ast_node)
        if 'create_gate' == ast_node['pattern_key']:
            variable = self.get_gate(ast_node)
        if 'create_circuit' == ast_node['pattern_key']:
            variable = self.get_circuit(ast_node)
        if 'adding_variables' == ast_node['pattern_key']:
            variable = self.get_expression(ast_node)
        return variable

    def append_variable(self, variable):
        self.qbl_memory_data[variable['name']] = {
            'type': variable['type'],
            'data': variable['data']
        }

    def get_qubit_state(self, ast_node):

        # ...

        return {
            'name': ast_node['args']['variable_name'],
            'type': 'QubitState',
            'data': 'data1'
        }

    def get_gate(self, ast_node):

        # ...

        return {
            'name': ast_node['args']['variable_name'],
            'type': 'Gate',
            'data': 'data1'
        }

    def get_circuit(self, ast_node):

        # ...

        return {
            'name': ast_node['args']['variable_name'],
            'type': 'Circuit',
            'data': 'data1'
        }

    def get_expression(self, ast_node):

        # ...

        return {
            'name': ast_node['args']['variable_name'],
            'type': 'Expression',
            'data': 'data1'
        }

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy
import json


class AST:

    def __init__(self, qbl_memory):
        self.qbl_memory = qbl_memory
        self.ast_tree = []
        self.current_line_number = 0
        self.current_indentation_level = 0
        self.current_line_data = {}

        self.nodes_settings = {
            'create_qubit_state': {
                'required_children': {
                    'define_qubit_value': True
                },
                'available_children': {
                    'define_qubit_value': True
                },
            },
            'create_gate': {
                'required_children': {
                    'define_vector': True
                },
                'available_children': {
                    'define_vector': True
                },
                'min_numb_of_children': 2
            },
            'create_circuit': {
                'available_children': {
                    'define_input': True,
                    'define_step': True
                },
                'min_numb_of_children': 1
            },
            'define_vector': {
                'no_children': True
            },
            'define_qubit_value': {
                'no_children': True
            },
            'define_input': {
                'available_children': {
                    'add_bit_to_input': True,
                    'add_qubit_to_input': True,
                },
                'not_after_node': {
                    'define_step': True
                },
                'min_numb_of_children': 1,
                'only_one_in_parent_node': True
            },
            'define_step': {
                'available_children': {
                    'add_item_to_step': True
                },
                'min_numb_of_children': 1
            },
            'adding_variables': {
                'no_children': True
            },
            'add_bit_to_input': {
                'no_children': True
            },
            'add_qubit_to_input': {
                'no_children': True
            },
            'add_item_to_step': {
                'no_children': True
            },
        }

    def process_line(self, line_data, indentation_level, line_number):
        self.prepare_line_data(line_data, indentation_level, line_number)
        self.append_current_line_data_to_ast()

    def prepare_line_data(self, line_data, indentation_level, line_number):
        self.current_line_number = line_number
        self.current_line_data = line_data
        if indentation_level - self.current_indentation_level > 1:
            raise SyntaxError('incorrect indentation, ' + 'line ' + str(self.current_line_number))
        self.current_indentation_level = indentation_level

    def append_current_line_data_to_ast(self):
        line_data = copy.copy(self.current_line_data)
        line_data['line_number'] = self.current_line_number
        line_data['children'] = []
        node_children = self.get_node_children()
        node_children.append(
            line_data
        )

    def get_node_children(self):
        node_children = self.ast_tree
        for x in range(0, self.current_indentation_level):
            node_children = node_children[-1]['children']
        return node_children

    def valid_ast_tree(self):
        pass

    def valid_node_children(self):
        pass

    def update_qbl_memory(self):
        print json.dumps(self.ast_tree, sort_keys=True, indent=4)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy


class AST:

    def __init__(self, qbl_memory):
        self.qbl_memory = qbl_memory
        self.node_stack = []
        self.new_node_stack = []
        self.current_line_number = 0
        self.current_indentation_level = 0
        self.current_line_data = {}
        self.current_node_settings = {}

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
        self.prepare_data(line_data, indentation_level, line_number)
        self.update_tmp_qbl_memory()
        self.save_node_stack()

    def prepare_data(self, line_data, indentation_level, line_number):
        self.current_line_data = line_data
        self.current_indentation_level = indentation_level
        self.current_line_number = line_number
        self.set_new_node_stack()

    def set_new_node_stack(self):
        new_node_stack = copy.copy(self.node_stack[:self.current_indentation_level])
        if len(new_node_stack) == self.current_indentation_level + 1:
            new_node_stack[self.current_indentation_level] = self.current_line_data['pattern_key']
        elif len(new_node_stack) == self.current_indentation_level:
            new_node_stack.append(self.current_line_data['pattern_key'])
        else:
            raise Exception('Indentation error. Line: ' + str(self.current_line_number))
        print 'STACK = ' + str(new_node_stack)
        self.new_node_stack = new_node_stack

    def valid_nodes(self):
        return True

    def update_tmp_qbl_memory(self):
        pass

    def save_node_stack(self):
        self.node_stack = self.new_node_stack

    def save_qbl_memory(self):
        if self.valid_nodes():
            self.qbl_memory.commit_new_objects()
        else:
            raise Exception('Syntax error.')

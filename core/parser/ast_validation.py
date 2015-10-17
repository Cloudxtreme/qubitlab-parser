#!/usr/bin/env python
# -*- coding: utf-8 -*-


class AstValidation:

    def __init__(self):

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

    def valid_root(self, root):
        for node_child in root:
            if(False == self.valid_node(node_child)):
                return False

    def valid_node(self, node):
        if(False == self.valid_node_data(node)):
            return False
        for node_child in node['children']:
            if(False == self.valid_node(node_child)):
                return False
        return True

    def valid_node_data(self, node):
        return True;

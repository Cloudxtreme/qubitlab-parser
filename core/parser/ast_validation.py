#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .variable_validation import *


class AstValidation:
    def __init__(self):
        self.variable_validation = VariableValidation()
        self.nodes_settings = self.get_node_settings()

    def get_node_settings(self):
        node_settings = {
            'create_qstate': self.get_create_qstate_settings(),
            'create_gate': self.get_create_gate_settings(),
            'create_circuit': self.get_create_circuit_settings(),
            'define_vector': self.get_define_vector_settings(),
            'define_qubit_value': self.get_define_qubit_value_settings(),
            'define_input': self.get_define_input_settings(),
            'define_step': self.get_define_step_settings(),
            'merge_circuits': self.get_merge_circuits_settings(),
            'add_bit_to_input': self.get_add_bit_to_input_settings(),
            'add_qubit_to_input': self.get_add_qubit_to_input_settings(),
            'add_item_to_step': self.get_add_item_to_step_settings(),
        }
        return node_settings

    @staticmethod
    def get_create_qstate_settings():
        return {
            'required_children': {
                'define_qubit_value': True
            },
            'allowed_children': {
                'define_qubit_value': True
            },
        }

    @staticmethod
    def get_create_gate_settings():
        return {
            'required_children': {
                'define_vector': True
            },
            'allowed_children': {
                'define_vector': True
            },
            'min_numb_of_children': 2
        }

    @staticmethod
    def get_create_circuit_settings():
        return {
            'allowed_children': {
                'define_input': True,
                'define_step': True
            },
            'min_numb_of_children': 1
        }

    @staticmethod
    def get_define_vector_settings():
        return {
            'no_children': True
        }

    @staticmethod
    def get_define_qubit_value_settings():
        return {
            'no_children': True
        }

    @staticmethod
    def get_define_input_settings():
        return {
            'allowed_children': {
                'add_bit_to_input': True,
                'add_qubit_to_input': True,
            },
            'not_after_node': {
                'define_step': True
            },
            'min_numb_of_children': 1,
            'only_one_in_parent_node': True
        }

    @staticmethod
    def get_define_step_settings():
        return {
            'allowed_children': {
                'add_item_to_step': True
            },
            'min_numb_of_children': 1
        }

    @staticmethod
    def get_merge_circuits_settings():
        return {
            'no_children': True
        }

    @staticmethod
    def get_add_bit_to_input_settings():
        return {
            'no_children': True
        }

    @staticmethod
    def get_add_qubit_to_input_settings():
        return {
            'no_children': True
        }

    @staticmethod
    def get_add_item_to_step_settings():
        return {
            'no_children': True
        }

    def valid_root(self, root):
        for index, node_child in enumerate(root):
            if not self.valid_node(node_child, root, index):
                return False

    def valid_node(self, node, parent, child_index):
        if not self.variable_validation.valid_node_variable_name(node):
            return False
        if not self.valid_node_data(node, parent, child_index):
            return False
        for index, node_child in enumerate(node['children']):
            if not self.valid_node(node_child, node, index):
                return False
        return True

    def valid_node_data(self, node, parent, child_index):
        node_settings = self.nodes_settings[node['pattern_key']]
        if 'allowed_children' in node_settings and not self.valid_allowed_children(node_settings, node):
            return False
        if 'required_children' in node_settings and not self.valid_required_children(node_settings, node):
            return False
        if 'min_numb_of_children' in node_settings and not self.valid_min_numb_of_children(node_settings, node):
            return False
        if 'no_children' in node_settings and not self.valid_no_children(node):
            return False
        if 'not_after_node' in node_settings \
                and not self.valid_not_after_node(node_settings, node, parent, child_index):
            return False
        if 'only_one_in_parent_node' in node_settings \
                and not self.valid_only_one_in_parent_node(node, parent):
            return False
        return True

    @staticmethod
    def valid_allowed_children(node_settings, node):
        for node_child in node['children']:
            if node_child['pattern_key'] not in node_settings['allowed_children']:
                raise SyntaxError('command block contains illegal code, line: ' + str(node_child['line_number']))
        return True

    def valid_required_children(self, node_settings, node):
        for required_child_pattern_key, required_child_value in node_settings['required_children'].iteritems():
            if required_child_value \
                    and not self.check_if_node_has_child_by_pattern_key(node, required_child_pattern_key):
                raise SyntaxError('no required code in command block, line: ' + str(node['line_number']))
        return True

    @staticmethod
    def check_if_node_has_child_by_pattern_key(node, pattern_key):
        for node_child in node['children']:
            if node_child['pattern_key'] == pattern_key:
                return True
        return False

    @staticmethod
    def valid_min_numb_of_children(node_settings, node):
        if len(node['children']) < node_settings['min_numb_of_children']:
            raise SyntaxError('missing code in command block, line: ' + str(node['line_number']))
        return True

    @staticmethod
    def valid_no_children(node):
        if len(node['children']) > 0:
            first_node_child = node['children'][0]
            raise SyntaxError('illegal nested command, line: ' + str(first_node_child['line_number']))
        return True

    def valid_not_after_node(self, node_settings, node, parent, child_index):
        for index, parent_node_child in enumerate(parent['children']):
            if index == child_index:
                break
            if self.contains_active_pattern_key(node_settings['not_after_node'], parent_node_child['pattern_key']):
                raise SyntaxError('given command can\'t occur after code above, line: ' + str(node['line_number']))
        return True

    @staticmethod
    def contains_active_pattern_key(pattern_list, pattern_key):
        for item_key, item_value in pattern_list.iteritems():
            if item_key == pattern_key and item_value:
                return True
        return False

    @staticmethod
    def valid_only_one_in_parent_node(node, parent):
        counter = 0
        for index, parent_node_child in enumerate(parent['children']):
            if parent_node_child['pattern_key'] == node['pattern_key']:
                counter += 1
                if counter > 1:
                    raise SyntaxError('given command can occur only once in one code node, line: ' +
                                      str(node['line_number']))
        return True

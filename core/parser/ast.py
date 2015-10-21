#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy
import json
from .ast_validation import *
from .ast_converter import *


class Ast:

    def __init__(self, qbl_memory):
        self.qbl_memory = qbl_memory
        self.ast_tree = []
        self.current_line_number = 0
        self.current_indentation_level = 0
        self.current_line_data = {}
        self.ast_validation = AstValidation()
        self.ast_converter = AstConverter()

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
        self.ast_validation.valid_root(self.ast_tree)

    def update_qbl_memory(self):
        #print json.dumps(self.ast_tree, sort_keys=True, indent=4)
        new_qbl_memory_data = self.ast_converter.get_qbl_memory_data(self.ast_tree)
        print json.dumps(new_qbl_memory_data, sort_keys=True, indent=4)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy
from .ast_validation import *
from .qbl_memory_builder import *


class Ast:

    def __init__(self, qbl_memory):
        self.qbl_memory = qbl_memory
        self.ast_tree = []
        self.current_line_number = 0
        self.current_indentation_level = 0
        self.current_line_data = {}
        self.ast_validation = AstValidation()
        self.qbl_memory_builder = QblMemoryBuilder(self.qbl_memory)

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
        new_qbl_memory_data = self.qbl_memory_builder.get_qbl_memory_new_data(self.ast_tree)
        self.qbl_memory.add_new_data(new_qbl_memory_data)

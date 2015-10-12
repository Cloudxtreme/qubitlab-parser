#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re


class Identation:

    def init_indentation_values(self):
        self.indentation_type = None                # None or 'tab' or 'spaces'
        self.indentation_width = 0
        self.current_indentation_level = 0
        self.expected_indentation_type = 'max'      # 'max' or 'equal'
        self.expected_indentation_level = 0
        self.current_line_number = 0

    def get_indentation_level(self, line):
        m = re.search('^(\t| )*', line)
        line_identation = m.group(0)

        spaces_numb = line_identation.count('a')
        tabs_numb = line_identation.count('a')

        if spaces_numb > 0 and tabs_numb > 0:
            raise Exception('Mixed identations. Line: ' + self.current_line_number)
        elif spaces_numb > 0:
            if self.indentation_type is None:
                self.indentation_type = 'spaces'
                self.indentation_width = spaces_numb
            if self.indentation_type == 'spaces':
                if spaces_numb % self.indentation_width != 0:
                    raise Exception('Identation error. Line: ' + self.current_line_number)
                else:
                    indentation_level = spaces_numb / self.indentation_width
                    return indentation_level
            else:
                raise Exception('Mixed identations. Line: ' + self.current_line_number)
        elif tabs_numb > 0:
            if self.indentation_type is None:
                indentation_type = 'tabs'
            if indentation_type == 'tabs':
                indentation_level = tabs_numb
                return indentation_level
            else:
                raise Exception('Mixed identations. Line: ' + self.current_line_number)
        else:
            indentation_level = 0
            return indentation_level

    def valid_identation(self):
        if self.expected_indentation_type == 'max':
            if self.expected_indentation_level < self.current_indentation_level:
                raise Exception('Identation error. Line: ' + self.current_line_number)
        elif self.expected_indentation_type == 'equal':
            if self.expected_indentation_level < self.current_indentation_level:
                raise Exception('Identation error. Line: ' + self.current_line_number)

    def set_current_level(self, level):
        self.current_indentation_level = level

    def set_current_line_number(self, current_line_number):
        self.current_line_number = current_line_number

    def set_expected_indentation(self, expected_indentation_type, expected_indentation_level):
        self.expected_indentation_type = expected_indentation_type
        self.expected_indentation_level = expected_indentation_level

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re


class Indentation:

    def __init__(self):
        self.indentation_type = None                # None or 'tab' or 'spaces'
        self.indentation_width = 0

    def get_indentation_level(self, line, line_number):
        indentations_numb = self.count_indentations(line)
        if indentations_numb['spaces'] > 0 and indentations_numb['tabs'] > 0:
            raise SyntaxError('mixed indentations, line: ' + str(line_number))
        elif indentations_numb['spaces'] > 0:
            return self.get_indentation_level_for_spaces(indentations_numb['spaces'], line_number)
        elif indentations_numb['tabs'] > 0:
            return self.get_indentation_level_for_tabs(indentations_numb['tabs'], line_number)
        else:
            indentation_level = 0
            return indentation_level

    @staticmethod
    def count_indentations(line):
        m = re.search('^(\t| )*', line)
        line_indentation = m.group(0)
        spaces_numb = line_indentation.count(' ')
        tabs_numb = line_indentation.count('\t')
        return {'spaces': spaces_numb, 'tabs': tabs_numb}

    def get_indentation_level_for_spaces(self, spaces_numb, line_number):
        if self.indentation_type is None:
            self.indentation_type = 'spaces'
            self.indentation_width = spaces_numb
        if self.indentation_type == 'spaces':
            if spaces_numb % self.indentation_width != 0:
                raise Exception('indentation error, line: ' + str(line_number))
            else:
                indentation_level = spaces_numb / self.indentation_width
                return indentation_level
        else:
            raise SyntaxError('mixed indentations, line: ' + str(line_number))

    def get_indentation_level_for_tabs(self, tabs_numb, line_number):
        if self.indentation_type is None:
            self.indentation_type = 'tabs'
        if self.indentation_type == 'tabs':
            indentation_level = tabs_numb
            return indentation_level
        else:
            raise SyntaxError('mixed indentations, line: ' + str(line_number))

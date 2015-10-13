#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re


class Indentation:

    def __init__(self):
        self.indentation_type = None                # None or 'tab' or 'spaces'
        self.indentation_width = 0

    def get_indentation_level(self, line, line_number):
        m = re.search('^(\t| )*', line)
        line_indentation = m.group(0)

        spaces_numb = line_indentation.count(' ')
        tabs_numb = line_indentation.count('\t')

        if spaces_numb > 0 and tabs_numb > 0:
            raise Exception('Mixed indentations. Line: ' + line_number)
        elif spaces_numb > 0:
            if self.indentation_type is None:
                self.indentation_type = 'spaces'
                self.indentation_width = spaces_numb
            if self.indentation_type == 'spaces':
                if spaces_numb % self.indentation_width != 0:
                    raise Exception('indentation error. Line: ' + line_number)
                else:
                    indentation_level = spaces_numb / self.indentation_width
                    return indentation_level
            else:
                raise Exception('Mixed indentations. Line: ' + line_number)
        elif tabs_numb > 0:
            if self.indentation_type is None:
                indentation_type = 'tabs'
            if indentation_type == 'tabs':
                indentation_level = tabs_numb
                return indentation_level
            else:
                raise Exception('Mixed indentations. Line: ' + line_number)
        else:
            indentation_level = 0
            return indentation_level

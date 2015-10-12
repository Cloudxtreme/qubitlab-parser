#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re


class CodeSyntax:

    def __init__(self):

        # Code patterns
        cp = {
            'variable_name'     : '[a-zA-Z_]+[a-zA-Z_0-9]*',
            'optional_space'    : '( |\\t)*',
            'required_space'    : '( |\\t)+',
        }
        cp['natural_number']        = '\d+'
        cp['number_unbracketed']    = '(-?\d+(\.\d+)?((\+|-)\d+(\.\d+)j)?|-?\d+(\.\d+)j)'
        cp['number']                = '(\(' + cp['number_unbracketed'] + '\)|' + cp['number_unbracketed'] + ')'
        cp['attribution']           = cp['optional_space'] + '=' + cp['optional_space']
        cp['qubit_state']           = cp['number'] + '\|0>' + cp['required_space'] + '\+' + cp['required_space'] + \
            cp['number'] + '\|1>'
        cp['gate_range']            = cp['natural_number'] + '\.\.' + cp['natural_number']

        # Line patterns
        lp = {
            'create_qubit_state' : '(?P<variable_name>' + cp['variable_name'] + ')' + cp['attribution'] + 'QubitState:',
            'create_gate'        : '(?P<variable_name>' + cp['variable_name'] + ')' + cp['attribution'] + 'Gate:',
            'create_circuit'     : '(?P<variable_name>' + cp['variable_name'] + ')' + cp['attribution'] + 'Circuit:',
            'define_vector'      : '(?P<vector_values>' + cp['number'] + '(' + cp['optional_space'] + ','
                + cp['optional_space'] + cp['number'] + ')*)',
            'define_qubit_value' : '(?P<value>' + cp['qubit_state'] + ')',
            'define_input'       : 'input:',
            'define_step'        : 'step:',
            'adding_variables'   : '(?P<variable_name>' + cp['variable_name'] + ')' + cp['attribution']
                + '(?P<adding_arguments>' + cp['variable_name'] + '(' + cp['optional_space']+ '\+'
                + cp['optional_space'] + cp['variable_name'] + ')*)',
            'add_bit_to_input'   : 'bit' + cp['required_space'] + '(?P<value>(0|1))',
            'add_qubit_to_input' : 'qubit' + cp['required_space'] + '(?P<value>(' + cp['qubit_state'] + '|'
                + cp['variable_name'] + '))',
            'add_item_to_step'   : '(?P<item_name>' + cp['variable_name'] + ')' + cp['required_space']
                + '(?P<value>(' + cp['gate_range'] + '|' + cp['natural_number'] + '|all))',
        }

        self.description_comment = '(?P<text_line>[a-zA-Z0-9\\t _\-+\.,!@#$%^&*()\\\\|/?<>"[\]{}\'~`=;:]*)'

        self.code_patterns = cp
        self.line_patterns = lp

    def recognize_line(self, line):

        for pattern_key, pattern in self.line_patterns.iteritems():
            match_result = self.check_pattern(line, pattern)
            if match_result['is_matched']:
                return {
                    'pattern_key' : pattern_key,
                    'args' : match_result['args']
                }

        return {'pattern_key': None, 'args': {}}

    def check_pattern(self, line, pattern_str):

        pattern = re.compile('^' + pattern_str + '$')
        line_match = pattern.match(line)
        if line_match:
            args = line_match.groupdict()
            return {'is_matched': True, 'args': args}
        else:
            return {'is_matched': False, 'args': {}}

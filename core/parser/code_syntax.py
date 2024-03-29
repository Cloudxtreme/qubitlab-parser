#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re


class CodeSyntax:

    def __init__(self):
        self.description_comment = '(?P<text_line>[a-zA-Z0-9\\t _\-+\.,!@#$%^&*()\\\\|/?<>"[\]{}\'~`=;:]*)'
        self.code_patterns = self.get_code_patterns()
        self.line_patterns = self.get_line_patterns()

    def get_code_patterns(self):
        cp = {
            'variable_name'     : '[a-zA-Z_]+[a-zA-Z_0-9]*',
            'optional_space'    : '( |\\t)*',
            'required_space'    : '( |\\t)+',
        }
        cp['natural_number']        = '\d+'
        cp['number_unbracketed']    = '(-?\d+(\.\d+)?((\+|-)\d+(\.\d+)?j)?|-?\d+(\.\d+)?j)'
        cp['number']                = '(\(' + cp['number_unbracketed'] + '\)|' + cp['number_unbracketed'] + ')'
        cp['assignment']            = cp['optional_space'] + '=' + cp['optional_space']
        cp['qstate']                = cp['number'] + '\|0>' + cp['required_space'] + '\+' + cp['required_space'] + \
                cp['number'] + '\|1>'
        cp['gate_range']            = cp['natural_number'] + '\.\.' + cp['natural_number']
        return cp

    def get_line_patterns(self):
        cp = self.code_patterns
        lp = {
            'create_qstate' : '(?P<variable_name>' + cp['variable_name'] + ')' + cp['assignment'] + \
                    'qstate:',
            'create_gate'        : '(?P<variable_name>' + cp['variable_name'] + ')' + cp['assignment'] + 'gate:',
            'create_circuit'     : '(?P<variable_name>' + cp['variable_name'] + ')' + cp['assignment'] + 'circuit:',
            'define_vector'      : '(?P<vector_values>' + cp['number'] + '(' + cp['optional_space'] + ','
                    + cp['optional_space'] + cp['number'] + ')*)',
            'define_qubit_value' : '(?P<value>' + cp['qstate'] + ')',
            'define_input'       : 'input:',
            'define_step'        : 'step:',
            'merge_circuits'   : '(?P<variable_name>' + cp['variable_name'] + ')' + cp['assignment']
                    + '(?P<circuit_merge_expression>' + cp['variable_name'] + '(' + cp['optional_space']+ '\+'
                    + cp['optional_space'] + cp['variable_name'] + ')*)',
            'add_qubit_to_input' : '(?P<value>(' + cp['qstate'] + '|' + cp['variable_name'] + '))',
            'add_item_to_step'   : '(?P<item_name>(' + cp['variable_name'] + '|measure))' + cp['required_space']
                    + '(?P<value>(' + cp['gate_range'] + '|' + cp['natural_number'] + '|all))',
        }
        return lp

    def recognize_line(self, line, line_number):
        for pattern_key, pattern in self.line_patterns.iteritems():
            match_result = self.check_pattern(line, pattern)
            if match_result['is_matched']:
                return {
                    'pattern_key' : pattern_key,
                    'args' : match_result['args']
                }
        raise SyntaxError('incorrect syntax, ' + 'line ' + str(line_number))
        return {'pattern_key': None, 'args': {}}

    def check_pattern(self, line, pattern_str):
        pattern = re.compile('^' + pattern_str + '$')
        line_match = pattern.match(line)
        if line_match:
            args = line_match.groupdict()
            return {'is_matched': True, 'args': args}
        else:
            return {'is_matched': False, 'args': {}}

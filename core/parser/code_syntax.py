#!/usr/bin/env python
# -*- coding: utf-8 -*-


class CodeSyntax:

    def __init__(self):

        # Basic code patterns
        cp = {
            'variable_name'     : '[a-zA-Z_]+[a-zA-Z_0-9]*',
            'optional_space'    : '( |\\t)*',
            'required_space'    : '( |\\t)+',
        }

        # Complex code patterns
        cp['number']        = '(-?\d+(\.\d+)?((+|-)\d+(\.\d+)j)?|-?\d+(\.\d+)j)'
        cp['vector']        = cp['number'] + '(' + cp['optional_space'] + ',' + cp['optional_space'] + cp['number'] + ')*'
        cp['attribution']   = cp['optional_space'] + '=' + cp['optional_space']

        self.line_patterns = {
            'new_state'     : cp['variable_name'] + cp['attribution'] + 'State:',
            'new_gate'      : cp['variable_name'] + cp['attribution'] + 'Gate:',
            'new_circuit'   : cp['variable_name'] + cp['attribution'] + 'Circuit:'
        }


    def recognize_line(self, line):

        print line

        # fn_match = re.match(r"(?P<function>\w+)\s?\((?P<arg>(?P<args>\w+(,\s?)?)+)\)", s)
        # fn_dict = fn_match.groupdict()
        # del fn_dict['args']
        # fn_dict['arg'] = [arg.strip() for arg in fn_dict['arg'].split(',')]

        pattern_key = ''
        arguments = {
            'arg1' : '',
            'arg2' : ''
        }

        result = {
            'pattern_key' : pattern_key,
            'arguments' : arguments
        }

        return result
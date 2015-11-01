#!/usr/bin/env python
# -*- coding: utf-8 -*-

import keyword


class VariableValidation:

    def __init__(self):

        qbl_kwlist = ['qstate', 'gate', 'circuit', 'input', 'step', 'qubit', 'bit', 'measure', 'all']
        self.variable_name_blacklist = keyword.kwlist + qbl_kwlist

    def valid_node_variable_name(self, node):
        if 'args' in node and 'variable_name' in node['args']:
            variable_name = node['args']['variable_name']
            if variable_name.lower() in self.variable_name_blacklist:
                raise SyntaxError('forbidden variable name, line: ' + str(node['line_number']))
        return True

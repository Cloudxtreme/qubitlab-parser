#!/usr/bin/env python
# -*- coding: utf-8 -*-


class CodeSyntax:

    def __init__(self):
        self.code_patterns = {
            'name1': 'pattern1',
            'name2': 'pattern2',
            'name3': self.code_patterns['pattern1'] + 'pattern3',
        }

    def example(self):
        pass

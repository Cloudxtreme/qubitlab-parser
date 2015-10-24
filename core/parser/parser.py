#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .code_reader import *

class Parser:

    def parse_code(self, file_path, qbl_memory):
        code_reader = CodeReader(qbl_memory)
        try:
            code_reader.read_file(file_path)
            print '[OK] import from file "' + file_path + '"'
        except SyntaxError as e:
            print '[ERROR] ' + e.message
        return qbl_memory

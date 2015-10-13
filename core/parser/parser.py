#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .code_reader import *

class Parser:

    def parse_code(self, file_path, qbl_memory):

        code_reader = CodeReader(qbl_memory)
        qbl_memory = code_reader.read_file(file_path)

        return qbl_memory

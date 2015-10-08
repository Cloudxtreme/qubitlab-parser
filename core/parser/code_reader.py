#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .identation import *

class CodeReader:

    def read_file(self, file_path, qbl_memory):

        identation = Identation()
        identation.init_indentation_values()

        with open(file_path) as f:
            for line in f:
                print line,

        return qbl_memory



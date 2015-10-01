#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .identation import *

class Parser:

    # parses code and adds new objects to qbl_memory
    def parse_code(self, code, qbl_memory):

        identation = Identation()
        identation.init_indentation_values()

        # while lines
        #   line = line without text after '#'
        #   ...

        return qbl_memory

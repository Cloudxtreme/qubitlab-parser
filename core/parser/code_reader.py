#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .code_syntax import *
from .identation import *

class CodeReader:

    def read_file(self, file_path, qbl_memory):

        identation = Identation()
        identation.init_indentation_values()

        code_syntax = CodeSyntax()
        code_syntax.test()

        with open(file_path) as f:
            for line in f:

                # check indention
                # ...

                line = self.remove_comment_and_trim(line)

                # syntax
                # recognize line
                # ...



                print line,

        return qbl_memory

    def remove_comment_and_trim(self):
        pass


#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .code_syntax import *
from .identation import *

class CodeReader:

    def read_file(self, file_path, qbl_memory):

        identation = Identation()
        identation.init_indentation_values()

        code_syntax = CodeSyntax()

        with open(file_path) as f:
            for line in f:

                # check indention
                # ...

                line_code = self.remove_comment_and_trim(line)

                if len(line_code) == 0:
                    continue

                line_data = code_syntax.recognize_line(line_code)

                print line_data
                print '=' + line_code + '='
                print line,

        return qbl_memory

    def remove_comment_and_trim(self, line):
        line = re.sub(re.compile("#.*?\n" ) ,"" ,line)
        line = line.strip()
        return line


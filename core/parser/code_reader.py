#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .code_syntax import *
from .ast import *
from .indentation import *

class CodeReader:

    def __init__(self, qbl_memory):
        self.qbl_memory = qbl_memory

    def read_file(self, file_path):

        indentation = Indentation()
        ast = Ast(self.qbl_memory)
        code_syntax = CodeSyntax()

        line_number = 0;
        with open(file_path) as f:
            for line in f:
                line_number = line_number + 1
                indentation_level = indentation.get_indentation_level(line, line_number)
                line_code = self.remove_comment_and_trim(line)
                if len(line_code) == 0:
                    continue
                line_data = code_syntax.recognize_line(line_code, line_number)
                ast.process_line(line_data, indentation_level, line_number)

        ast.valid_ast_tree()
        ast.update_qbl_memory()

    def remove_comment_and_trim(self, line):
        line = re.sub(re.compile("#.*?\n" ) ,"" ,line)
        line = line.strip()
        return line

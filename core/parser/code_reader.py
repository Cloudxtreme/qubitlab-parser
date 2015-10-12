#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .code_syntax import *
from .indentation import *

class CodeReader:

    def read_file(self, file_path, qbl_memory):

        indentation = Indentation()
        indentation.init_indentation_values()

        code_syntax = CodeSyntax()

        line_number = 0;
        with open(file_path) as f:
            for line in f:
                ++line_number
                # check indention
                # ...

                indentation_level = indentation.get_indentation_level(line, line_number)

                line_code = self.remove_comment_and_trim(line)

                indentation

                if len(line_code) == 0:
                    continue

                line_data = code_syntax.recognize_line(line_code)

                print "level = " + str(indentation_level) + "; ",
                print line_data
                print line,

        return qbl_memory

    def remove_comment_and_trim(self, line):
        line = re.sub(re.compile("#.*?\n" ) ,"" ,line)
        line = line.strip()
        return line


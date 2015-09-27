#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Parser:


    # parses code and adds new objects to simulation_objects
    def parse_code(self, code, simulaiton_objects):
        print code

        # init_indentation_values()

        # while lines
            # line = line without text after '#'
            #

        # determine indentation
            # find first line with code after white spaces
                # if white spaces are mixed
                    # throw exception
                # if

        return simulation_objects

    def init_indentation_values(self):
        print ''
        # this.indentation_type = None   # tab or spaces
        # this.indentation_spaces_numb = 0
        # this.current_indentation_level = 0
        # this.expected_indentation_level = 0
        # this.expected_indentation_type = 'max'   # max, equal

    def get_indentation_level(self, line):
        print ''
        # whitespace_prefix = line without code from first no-whitespace character including it
        # whitespace_prefix = whitespace_prefix with only spaces and tab (remove everything else)
        # spaces_nub = count spaces
        # tabs_numb = count tabs
        #
        # if spaces_numb > 0 and tabs_numb > 0
        #   exception: mixed indentions
        # elif spaces_numb > 0
        #   if indentation_type == None
        #       indentation_type = 'space'
        #   if indentation_type == spaces
        #       if spaces_numb % this.indentation_spaces_numb != 0
        #           exception: wrong number of spaces in indantation
        #       else
        #           indentation_level = spaces_numb / this.indentation_spaces_numb
        #           return indentation_level
        #   elif
        #       exception: mixed indantions
        # elif tabs_numb > 0
        #   if indentation_type == None
        #       indentation_type = 'tabs'
        #   if indentation_type == tabs
        #       indentation_level = tabs_numb
        #       return indentation_level
        #   elif
        #       exception: mixed indantions
        # else
        #   indentation_level = 0
        #   return indentation_level



    def check_indentation(self):
        print ''
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import pprint

from core.parser.parser import *


class Actions:

    def __init__(self, qbl_memory):
        self.qbl_memory = qbl_memory

    def list_action(self):
        print
        print "=== QBL Memory objects ==="
        print
        pprint.pprint(self.qbl_memory.qbl_objects)
        print

    @staticmethod
    def info_action():
        print "Info about object in QBL memory..."

    @staticmethod
    def graph_action():
        print "Display graphical scheme of circuit..."

    def import_action(self, args):
        if len(args) != 1:
            self.show_params_numb_error('import')
            return False

        qbl_file = args[0]
        if qbl_file:
            if os.path.isfile(qbl_file):
                if not qbl_file.endswith('.qbl'):
                    print ("[ERROR] '%s' must have '.qbl' extension." % qbl_file)
                    return False
            else:
                print ("[ERROR] '%s' is incorrect path to qbl file." % qbl_file)
                return False

        parser = Parser()
        parser.parse_code(qbl_file, self.qbl_memory)

        return True

    @staticmethod
    def run_action():
        print "Start running the simulation..."

    def help_action(self):
        print
        print self.get_header()
        print
        print "=== HELP ==="
        print
        print "USAGE:"
        print "\t./qubitlab.py [OPTIONS] [COMMAND]"
        print
        print "OPTIONS:"
        print "\t--output <file_path>                                           Output file."
        print "\t-o <file_path>                                                 The same as \"--output\"."
        print "\t--help                                                         Show help and ignore command."
        print "\t-h                                                             The same as \"--help\"."
        print
        print "AVAILABLE COMMANDS:"
        print "\thelp                                                           Show help."
        print
        print "\trun <circuit_name>[:<step_number>] <one_or_more_qbl_files>     Start running the simulation"
        print "\t                                                               and get final state."
        print
        print "\t                                                               Use optional <step_number> parameter"
        print "\t                                                               to get state for given step."
        print
        print "\t                                                               <circuit_name> may be also"
        print "\t                                                               circuit merge expression, f.e."
        print "\t                                                               \"circ1+circ2+circ3\"."
        print
        print "\tlist <one_or_more_qbl_files>                                   List of objects in QBL memory."
        print "\tinfo <object_name> <one_or_more_qbl_files>                     Info about object in QBL memory."
        print "\tgraph <circuit_name> <one_or_more_qbl_files>                   Display graphical scheme of circuit.."
        print
        print "EXAMPLE:"
        print "\t./qubitlab.py run circ1+circ2:2 examples/example1.qbl"
        print

    @staticmethod
    def dialog_help_action():
        print
        print "=== HELP ==="
        print
        print "AVAILABLE COMMANDS:"
        print
        print "\tquit                                   Exit the program."
        print "\thelp                                   Show help."
        print
        print "\trun <circuit_name>[:<step_number>]     Start running the simulation"
        print "\t                                       and get final state."
        print
        print "\t                                       Use optional <step_number> parameter"
        print "\t                                       to get state for given step."
        print
        print "\t                                       <circuit_name> may be also"
        print "\t                                       circuit merge expression, f.e."
        print "\t                                       \"circ1+circ2+circ3\"."
        print
        print "\tlist                                   List of objects in QBL memory."
        print "\tinfo <object_name>                     Info about object in QBL memory."
        print "\timport <one_or_more_qbl_files>         Import data from QBL file to QBL memory."
        print "\tgraph <circuit_name>                   Display graphical scheme of circuit.."
        print
        print "EXAMPLE:"
        print "\trun circ1+circ2:2"
        print

    @staticmethod
    def get_header():
        header = """== QubitLab v.0 ==
        Quantum Computing Simulator
        www.qubitlab.net"""
        return header

    def dialog_action(self):
        print
        print self.get_header()
        print

        while 1:
            try:
                sys.stdout.write("qbl> ")
                command_line = sys.stdin.readline().strip()
                command_items = re.split('\s+', command_line)
                if len(command_items) == 0:
                    continue
                command = command_items.pop(0).lower()
                command_args = command_items
            except KeyboardInterrupt:
                break

            if command == 'quit':
                break
            if command == 'import':
                self.import_action(command_args)
                continue
            if command == 'list':
                self.list_action()
                continue
            if command == 'info':
                self.info_action()
                continue
            if command == 'graph':
                self.graph_action()
                continue
            if command == 'run':
                self.run_action()
                continue
            if command == 'help':
                self.dialog_help_action()
                continue

            print "[ERROR] Incorrect command!"
            print "Type 'help' to show available commands."

    @staticmethod
    def error_action():
        print "[ERROR] Incorrect action."
        sys.exit(2)

    @staticmethod
    def show_params_numb_error(command):
        print "[ERROR] Incorrect number of parameters for command \"%s\"" % command
        print "Type 'help' to show available commands."

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

    def info_action(self):
        print "Info about object in QBL memory..."

    def graph_action(self):
        print "Display graphical scheme of circuit..."

    def import_action(self, args):
        if len(args) != 1:
            self.show_params_numb_error('import')
            return False

        file = args[0]
        if file:
            if os.path.isfile(file):
                if file.endswith('.qbl'):
                    self.file = file
                else:
                    print ("[ERROR] '%s' must have '.qbl' extension." % file)
                    return False
            else:
                print ("[ERROR] '%s' is incorrect path to qbl file." % file)
                return False

        parser = Parser()
        parser.parse_code(file, self.qbl_memory)

        return True

    def run_action(self):
        print "Start running the simulation..."

    def help_action(self):
        print
        print "=== HELP ==="
        print
        print "Usage:"
        print "./qubitlab.py <OPTIONS> <COMMAND>"
        print
        print "\tOPTIONS:"
        print "\t--output <file_path>                                           Output file."
        print "\t-o <file_path>                                                 The same as \"--output\"."
        print "\t--help                                                         Show help and ingore command."
        print "\t-h                                                             The same as \"--help\"."
        print
        print "\tCOMMANDS:"
        print "\thelp                                                           Show help."
        print
        print "\tlist <one_or_more_qbl_files>                                   List of objects in QBL memory."
        print "\tinfo <object_name> <one_or_more_qbl_files>                     Info about object in QBL memory."
        print "\tgraph <circiut_name> <one_or_more_qbl_files>                   Display graphical scheme of circuit.."
        print "\trun <circuit_name>[:<step_number>] <one_or_more_qbl_files>     Start running the simulation"
        print "\t                                                               and get final state."
        print
        print "\t                                                               Use optional <step_number> parameter"
        print "\t                                                               to get state for this step."
        print
        print "\t                                                               <circuit_name> may be also"
        print "\t                                                               concatenation of many circuits, f.e."
        print "\t                                                               \"circ1+circ2+circ3\"."
        print
        print "Example usage:"
        print "./qubitlab.py run circ1 examples/example1.qbl"
        print

    def dialog_help_action(self):
        print
        print "=== HELP ==="
        print
        print "Available commands:"
        print
        print "\tquit                                   Exit the program."
        print "\thelp                                   Show help."
        print
        print "\tlist                                   List of objects in QBL memory."
        print "\tinfo <object_name>                     Info about objecti in QBL memory."
        print "\timport <one_or_more_qbl_files>         Import data from QBL file to QBL memory."
        print "\tgraph <circiut_name>                   Display graphical scheme of circuit.."
        print "\trun <circiut_name>[:<step_number>]     Start running the simulation"
        print "\t                                       and get final state."
        print
        print "\t                                       Use optional <step_number> parameter"
        print "\t                                       to get state for this step."
        print
        print "\t                                       <circuit_name> may be also"
        print "\t                                       concatenation of many circuits, f.e."
        print "\t                                       \"circ1+circ2+circ3\"."
        print

    def dialog_action(self):

        print
        print "== QubitLab v.0 =="
        print "Quantum Computing Simulator"
        print "www.qubitlab.net"
        print

        while 1:
            try:
                sys.stdout.write("qbl> ")
                command_line = sys.stdin.readline().strip()
                command_items = re.split('\s+', command_line)
                if len(command_items) == 0:
                    continue;
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

    def error_action(self):
        print "[ERROR] Incorrect action."
        sys.exit(2)

    def show_params_numb_error(self, command):
        print "[ERROR] Incorrect number of parameters for command \"%s\"" % command
        print "Type 'help' to show available commands."

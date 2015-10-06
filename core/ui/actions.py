#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re
import os


class Actions:

    def __init__(self):
        pass

    @staticmethod
    def graph_action():
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


        print "Import data from QBL file to QBL memory..."
        return True

    @staticmethod
    def run_action():
        print "Start running the simulation..."

    @staticmethod
    def help_action():
        print
        print "-- HELP --"
        print "Available options:"
        print
        print "\tquit                       Exit the program."
        print "\thelp                       Show available options."
        print
        print "\timport <filename>.qbl      Import data from QBL file to QBL memory."
        print "\tgraph                      Display graphical scheme of circuit.."
        print "\trun                        Start running the simulation."
        print

    def dialog_action(self):

        print
        print "== QubitLab v.0 =="
        print "Quantum Computing Laboratory"
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
            if command == 'graph':
                self.graph_action()
                continue
            if command == 'run':
                self.run_action()
                continue
            if command == 'help':
                self.help_action()
                continue

            print "[ERROR] Incorrect command!"
            print "Type 'help' to show available options."

    @staticmethod
    def error_action():
        print "[ERROR] Incorrect action."
        sys.exit(2)

    @staticmethod
    def show_params_numb_error(command):
        print "[ERROR] Incorrect number of parameters for command \"%s\"" % command
        print "Type 'help' to show available options."
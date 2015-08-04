#!/usr/bin/python

import sys


class Actions:

    def __init__(self):
        pass

    @staticmethod
    def graph_action():
        print "Display graphical scheme of circuit..."

    @staticmethod
    def run_action():
        print "Start running the simulation..."

    @staticmethod
    def help_action():
        print
        print "-- HELP --"
        print "Available options:"
        print
        print "\tquit - Exit the program."
        print "\thelp - Show available options."
        print
        print "\tgraph - Display graphical scheme of circuit.."
        print "\trun - Start running the simulation."
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
                line = sys.stdin.readline().strip()
            except KeyboardInterrupt:
                break

            if line.lower() == 'quit':
                break

            elif line.lower() == 'graph':
                self.graph_action()

            elif line.lower() == 'run':
                self.run_action()

            elif line.lower() == 'help':
                self.help_action()
            else:
                print "[ERROR] Incorrect command!"
                print "Type 'help' to show available options."

    @staticmethod
    def error_action():
        print "[ERROR] Incorrect action."
        sys.exit(2)

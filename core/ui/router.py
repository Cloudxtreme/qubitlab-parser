#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import getopt


class Router:

    def __init__(self, actions):
        self.actions = actions
        self.current_action = ''
        self.output = ''
        self.args = []

    def get_params(self, argv):
        try:
            opts, args = getopt.getopt(argv, "o:", ["output="])
        except getopt.GetoptError:
            print "[ERROR] Wrong parameters."
            sys.exit(2)

        for opt, value in opts:
            if opt in ("-o", "--output"):
                self.output = value

        if len(args) > 0:
            self.args = args
            self.current_action = self.args.pop(0)

        if self.output != '':
            if self.current_action != '':
                sys.stdout = open(self.output, 'w')
            else:
                print "[WARNING] In dialog mode '-o' and '--output' options are ignored."

    def call_action(self):

        if self.current_action == 'list':
            self.actions.list_action()
        elif self.current_action == 'info':
            self.actions.info_action()
        elif self.current_action == 'run':
            if len(self.args) < 2:
                self.actions.show_params_numb_error('run')
                sys.exit(2)
            if False == self.actions.import_action([self.args[1]]):
                sys.exit(2)
            self.actions.run_action()
        elif self.current_action == 'help':
            self.actions.help_action()
        elif self.current_action == '':
            self.actions.dialog_action()
        else:
            self.actions.error_action()

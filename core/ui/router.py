#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import getopt

from actions import Actions


class Router:

    def __init__(self):
        self.action = ''
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
            self.action = self.args.pop(0)

        if self.output != '':
            if self.action != '':
                sys.stdout = open(self.output, 'w')
            else:
                print "[WARNING] In dialog mode '-o' and '--output' options are ignored."

    def call_action(self):
        actions = Actions()

        if self.action == 'list':
            actions.list_action()
        elif self.action == 'info':
            actions.info_action()
        elif self.action == 'run':
            if len(self.args) < 2:
                actions.show_params_numb_error('run')
                sys.exit(2)
            if False == actions.import_action([self.args[1]]):
                sys.exit(2)
            actions.run_action()
        elif self.action == 'help':
            actions.help_action()
        elif self.action == '':
            actions.dialog_action()
        else:
            actions.error_action()

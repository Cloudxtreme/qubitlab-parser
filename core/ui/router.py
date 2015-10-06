#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import getopt

from actions import Actions


class Router:

    def __init__(self):
        self.action = 'dialog'
        self.output = ''
        self.args = []

    def get_params(self, argv):
        try:
            opts, args = getopt.getopt(argv, "a:o:", ["action=", "output="])
        except getopt.GetoptError:
            print "[ERROR] Wrong parameters."
            sys.exit(2)

        for opt, value in opts:
            if opt in ("-a", "--action"):
                self.action = value
            elif opt in ("-o", "--output"):
                self.output = value

        if self.output != '':
            if self.action != 'dialog':
                sys.stdout = open(self.output, 'w')
            else:
                print "[WARNING] In dialog mode '-o' and '--output' option is ignored."

        if len(args) > 0:
            self.args = args

    def call_action(self):
        actions = Actions()

        if self.action == 'list':
            actions.list_action()
        elif self.action == 'info':
            actions.info_action()
        elif self.action == 'run':
            if len(self.args) == 0:
                print "Parameter with <filename>.qbl is required."
                sys.exit(2)
            if False == actions.import_action([self.args[0]]):
                sys.exit(2)
            actions.run_action()
        elif self.action == 'help':
            actions.help_action()
        elif self.action == 'dialog' or self.action == '':
            actions.dialog_action()
        else:
            actions.error_action()

#!/usr/bin/python

import os
import sys
import getopt

from actions import Actions


class Router:

    def __init__(self):
        self.action = 'dialog'
        self.output = ''
        self.file = ''

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
            file = args[0]
            if file:
                if os.path.isfile(file):
                    if file.endswith('.qbl'):
                        self.file = file
                    else:
                        print ("[ERROR] '%s' must have '.qbl' extension." % file)
                        sys.exit(2)
                else:
                    print ("[ERROR] '%s' is incorrect path to qbl file." % file)
                    sys.exit(2)

    def call_action(self):
        actions = Actions()

        if self.action == 'list':
            actions.list_action()
        elif self.action == 'info':
            actions.info_action()
        elif self.action == 'run':
            actions.run_action()
        elif self.action == 'help':
            actions.help_action()
        elif self.action == 'dialog' or self.action == '':
            actions.dialog_action()
        else:
            actions.error_action()

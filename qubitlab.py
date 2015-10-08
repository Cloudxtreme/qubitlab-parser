#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from core.ui.router import Router
from core.ui.actions import Actions
from core.qbl_memory.qbl_memory import *


def main(argv):

    qbl_memory = QblMemory()
    actions = Actions(qbl_memory)

    router = Router(actions)
    router.get_params(argv)
    router.call_action()


if __name__ == "__main__":
    main(sys.argv[1:])
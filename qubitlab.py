#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from core.ui.router import Router


def main(argv):

    router = Router()
    router.get_params(argv)
    router.call_action()


if __name__ == "__main__":
    main(sys.argv[1:])
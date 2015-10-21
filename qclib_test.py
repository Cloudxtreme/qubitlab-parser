#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib.qclib.qclib import *

circ = (I ** h ** I) * (I ** cnot) * (cnot2 ** I)
print circ(ket0 ** ket0 ** ket0).dirac()

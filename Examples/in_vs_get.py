# -*-  coding: utf-8 -*-
"""
Each method run 2,000,000 times:

check_with_in    : 0.74073 sec
check_with_get   : 1.73232 sec 2.34x slower

"""

# Copyright (C) 2015 ZetaOps Inc.
#
# This file is licensed under the GNU General Public License v3
# (GPLv3).  See LICENSE.txt for details.
from ztimer import Timer, M
import random

a_dict = {}
for i in range(400):
    a_dict[str(random.random())] = random.random()

keys = a_dict.keys()

class Tst(Timer):

    def check_with_get(self):
        a_dict.get(keys[30])
        a_dict.get(keys[50])
        a_dict.get('dfdfsd', None)
        a_dict.get('dfdfsd23', None)

    def check_with_in(self):
        keys[30] in a_dict
        keys[50] in a_dict
        'dfdfsd' in a_dict
        'dfdfsd2323' in a_dict



Tst(2*M, hide_unsorted=False)


# -*-  coding: utf-8 -*-
"""
python2.7

no_override        : 0.73158 sec
override_setattr   : 4.56946 sec

Each method run 2,000,000 times:

no_override        : 0.73158 sec
override_setattr   : 4.56946 sec 6.25x slower

=======================================================================
python3.4

no_override        : 0.85222 sec
override_setattr   : 4.51983 sec

Each method run 2,000,000 times:

no_override        : 0.85222 sec
override_setattr   : 4.51983 sec 5.3x slower


"""

# Copyright (C) 2015 ZetaOps Inc.
#
# This file is licensed under the GNU General Public License v3
# (GPLv3).  See LICENSE.txt for details.
from ztimer import Timer, M
import random

class Properti(object):

    def __init__(self, **kwargs):
        self.name = kwargs.pop('name', '')

    def __get__(self, instance, cls=None):
        return instance.props.get(self.name, None)

    def __set__(self, instance, value):
        instance.props[self.name] = value



class Noveride(object):

    prop = Properti()

    def __init__(self):
        self.props = {}


class Overide(object):
    prop = Properti()

    def __init__(self):
        self.props = {}

    def __setattr__(self, key, value):
        object.__setattr__(self, key, value)


over1 = Overide()
over2 = Overide()
over3 = Overide()
over4 = Overide()
over5 = Overide()
over6 = Overide()


nover1 = Noveride()
nover2 = Noveride()
nover3 = Noveride()
nover4 = Noveride()
nover5 = Noveride()
nover6 = Noveride()

class Tst0(Timer):

    def override_for_prop_int(self):
        over1.prop = 2323

    def override_for_prop_str(self):
        over1.prop = 'dsdsd'

    def noverride_for_prop_int(self):
        nover1.prop = 2323

    def noverride_for_prop_str(self):
        nover1.prop = 'dsdsd'

class Tst1(Timer):

    def override_for_string(self):
        over1.string1 = 'foo'

    def no_override_for_string(self):
        nover1.string2 = 'foo'

    def override_for_integer(self):
        over1.integer1 = 3

    def no_override_for_integer(self):
        nover1.integer2 = 3

    def override_for_list(self):
        over1.lst1 = []

    def no_override_for_list(self):
        nover1.lst2 = []

class Tst2(Timer):
    def no_override_multi(self):
        nover1.integer3 = 3
        nover1.string3 = 'sdassdas'
        nover1.lst3 = [1,2,3]
        nover1.dict3 = {1:1,2:2}
        nover1.integer4 = 3
        nover1.string4 = 'sdassdas'
        nover1.lst4 = [1, 2, 3]
        nover1.dict4 = {1: 1, 2: 2}

    def override_multi(self):
        over1.integer3 = 3
        over1.string3 = 'sdassdas'
        over1.lst3 = [1,2,3]
        over1.dict3 = {1:1,2:2}
        over1.integer4 = 3
        over1.string4 = 'sdassdas'
        over1.lst4 = [1, 2, 3]
        over1.dict4 = {1: 1, 2: 2}

Tst0(M, hide_unsorted=False)
Tst1(M, hide_unsorted=False)
Tst2(M, hide_unsorted=False)


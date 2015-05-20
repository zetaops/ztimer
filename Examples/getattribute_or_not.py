# -*-  coding: utf-8 -*-
"""
Each method run 1,000,000 times:

without_getattribute                    : 0.297    sec
getattribute_with_tryexcept             : 1.79314  sec 6.0x slower
getattribute_with_ifelse                : 3.25342  sec 11.0x slower
"""

# Copyright (C) 2015 ZetaOps Inc.
#
# This file is licensed under the GNU General Public License v3
# (GPLv3).  See LICENSE.txt for details.
from ztimer import Timer


class A(object):
    obj_cache = {'a': {}, 'b': 12345, 'c': []}
    def __getattribute__(self, key):
        try:
            return object.__getattribute__(self, 'obj_cache')[key]
        except KeyError:
            return object.__getattribute__(self, key)


class AA(object):
    obj_cache = {'a': {}, 'b': 12345, 'c': []}
    def __getattribute__(self, key):
        if key in super(AA, self).__getattribute__('obj_cache'):
            return object.__getattribute__(self, 'obj_cache')[key]
        else:
            return object.__getattribute__(self, key)

class B(object):
    a = {}
    b = 12345
    c = []

a = A()
aa = AA()
b = B()

class Tst(Timer):

    def getattribute_with_tryexcept(self):
        a.a, a.b, a.c

    def getattribute_with_ifelse(self):
        aa.a, aa.b, aa.c

    def without_getattribute(self):
        b.a, b.b, b.c



Tst(method_list=['getattribute_with_ifelse', 'without_getattribute'])


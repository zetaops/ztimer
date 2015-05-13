# -*-  coding: utf-8 -*-
"""
according to these tests, simply checking for the equality of string gaves best performance

Each method run 1,000,000 times, sorted results listed bellow:

base_name_is_equal_NOT_equal            : 0.25714  sec
base_name_is_equal_equal                : 0.27107  sec
is_instance                             : 0.33097  sec
base_hasattr                            : 0.37031  sec
is_NOT_instance                         : 0.38185  sec
base_has_NOT_attr                       : 0.8913   sec

"""

# Copyright (C) 2015 ZetaOps Inc.
#
# This file is licensed under the GNU General Public License v3
# (GPLv3).  See LICENSE.txt for details.
from ztimer import Timer


class A(object):
    attr = "Foo"


class B(A):
    bttr = "Doo"

b = B()

class Tst(Timer):

    def base_name_is_equal_equal(self):
        return b.__class__.__base__.__name__ == 'A'

    def base_name_is_equal_NOT_equal(self):
        return b.__class__.__base__.__name__ == 'AAA'

    def base_hasattr(self):
        return hasattr(b.__class__.__base__, 'attr')

    def base_has_NOT_attr(self):
        return hasattr(b.__class__.__base__, 'nonattr')

    def is_instance(self):
        return isinstance(b, A)

    def is_NOT_instance(self):
        return isinstance(b, int)


Tst()


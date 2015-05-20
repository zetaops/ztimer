# -*-  coding: utf-8 -*-
"""
simply checking for the equality of base class names gives best performance.
while this is absolutely wrong way for general use, it's safe enough for my use case.

Each method run 1,000,000 times:

base_name_is_equal_NOT_equal            : 0.24945  sec
base_name_is_equal_equal                : 0.25527  sec 1.0x slower
is_instance                             : 0.31937  sec 1.3x slower
base_hasattr                            : 0.36778  sec 1.5x slower
is_NOT_instance                         : 0.38748  sec 1.6x slower
base_has_NOT_attr                       : 0.87158  sec 3.5x slower

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


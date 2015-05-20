# -*-  coding: utf-8 -*-
"""
While it's nice to be able to use dots instead of ugly brackets and quotes, it's unacceptably slower.

Each method run 2,000,000 times:

bracket_notation                        : 0.34383  sec
by_getter                               : 0.52543  sec 1.5x slower
dot_notation                            : 2.1887   sec 6.4x slower

"""

# Copyright (C) 2015 ZetaOps Inc.
#
# This file is licensed under the GNU General Public License v3
# (GPLv3).  See LICENSE.txt for details.
from ztimer import Timer, M


class DotDict(dict):
    def __getattr__(self, attr):
        return self.get(attr, None)

    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

dot_dict = DotDict({'a': 1})
a_dict = {'a': 1}

class Tst(Timer):

    def dot_notation(self):
        dot_dict.a

    def bracket_notation(self):
        a_dict['a']

    def by_getter(self):
        a_dict.get('a')



Tst(2*M, hide_unsorted=False)


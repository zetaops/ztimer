# -*-  coding: utf-8 -*-
"""
Tuple rulez!

Each method run 50,000 times:

tuple_create                   : 0.00712 sec
list_access                    : 0.00836 sec 1.2x slower
dict_access                    : 0.0089 sec 1.3x slower
tuple_access                   : 0.0104 sec 1.5x slower
class_access                   : 0.01097 sec 1.5x slower
list_create                    : 0.0144 sec 2.0x slower
namedtuple_access              : 0.01593 sec 2.2x slower
dict_create                    : 0.02089 sec 2.9x slower
class_create                   : 0.66754 sec 93.8x slower
namedtuple_positional_create   : 27.22996 sec 3825.5x slower
namedtuple_create              : 27.52619 sec 3867.1x slower

"""

# Copyright (C) 2015 ZetaOps Inc.
#
# This file is licensed under the GNU General Public License v3
# (GPLv3).  See LICENSE.txt for details.
from ztimer import Timer, K, M

from collections import namedtuple

a_tuple = ('a', 'b', 'c', 'd', 'e')
A_NTuple = namedtuple('ntuple', 'a b c d e')
a_ntuple = A_NTuple(a='a', b='b', c='c', d='d', e='e')
a_dict = {'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e'}
a_list = ['a', 'b', 'c', 'd', 'e']

class A_CLASS(object):
    a = 'a'
    b = 'b'
    c = 'c'
    d = 'd'
    e = 'e'


aclass = A_CLASS()


class Tst(Timer):

    def namedtuple_positional_create(self):
        NTuple = namedtuple('ntuple', 'a b c d e')
        ntuple = NTuple('a', 'b', 'c', 'd', 'e')

    def namedtuple_create(self):
        NTuple = namedtuple('ntuple', 'a b c d e')
        ntuple = NTuple(a='a', b='b', c='c', d='d', e='e')

    def namedtuple_access(self):
        a_ntuple.b

    def class_create(self):
        class N_CLASS(object): a = 'a'; b = 'b'; c = 'c'; d = 'd'; e = 'e'
        nclass = N_CLASS()

    def class_access(self):
        aclass.a

    def tuple_create(self):
        tuple = ('a', 'b', 'c', 'd', 'e')

    def list_create(self):
        alist = ['a', 'b', 'c', 'd', 'e']

    def tuple_access(self):
        a_tuple[1]

    def list_access(self):
        a_list[1]

    def dict_access(self):
        a_dict['b']

    def dict_create(self):
        dct = {'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e'}


Tst(50 * K)

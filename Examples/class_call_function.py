# -*-  coding: utf-8 -*-
"""
Each method run 10,000,000 times: ( with Python 3.4)

function                         : 2.35402 sec
class_instance_method            : 2.62464 sec 1.11x slower
class_init                       : 3.40103 sec 1.44x slower
class__call                      : 4.20906 sec 1.79x slower
class_instance__call__runs_foo   : 4.61189 sec 1.96x slower
class_init_runs_foo              : 5.28737 sec 2.25x slower


Each method run 10,000,000 times: (with python 2.7.10)

function                         : 2.2193 sec
class_instance_method            : 2.76581 sec 1.25x slower
class__call                      : 4.32812 sec 1.95x slower
class_init                       : 4.42555 sec 1.99x slower
class_instance__call__runs_foo   : 5.8423 sec 2.63x slower
class_init_runs_foo              : 5.84575 sec 2.63x slower

"""

# Copyright (C) 2015 ZetaOps Inc.
#
# This file is licensed under the GNU General Public License v3
# (GPLv3).  See LICENSE.txt for details.
from ztimer import Timer, M


class Foo():
    def __init__(self):
        self.foo()

    def __call__(self):
        self.foo()

    def foo(self):
        x = 3 * 3

class Boo():
    def __init__(self):
        x = 3 * 3

    def __call__(self):
        x = 3 * 3

boo_call = Boo()

foo_call = Foo()

def foo():
    x = 3 * 3


class Tst(Timer):
    def class_init_runs_foo(self):
        Foo()

    def class_instance__call__runs_foo(self):
        foo_call()

    def class__call(self):
        Boo()

    def class_init(self):
        boo_call()

    def function(self):
        foo()

    def class_instance_method(self):
        foo_call.foo()

Tst(10*M)

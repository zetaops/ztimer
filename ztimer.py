# -*-  coding: utf-8 -*-
"""
"""

# Copyright (C) 2015 ZetaOps Inc.
#
# This file is licensed under the GNU General Public License v3
# (GPLv3).  See LICENSE.txt for details.

from time import time
K = 1000
M = K * K

DEFAULT_REPEAT_COUNT = M


class Timer(object):
    def __init__(self, repeat=None, show_results=False):
        self.rank = {}
        self.show_results = show_results
        if repeat is None:
            repeat = DEFAULT_REPEAT_COUNT
        for name in sorted(self.__class__.__dict__):
            if not name.startswith('__'):
                self.timeit(getattr(self, name), repeat)
        print("\nEach method run {:,} times, sorted results listed bellow:\n".format(repeat))
        for rnk in sorted(self.rank):
            self.prnt(self.rank[rnk][0], rnk, self.rank[rnk][1])


    def timeit(self, method, repeat):
        t1 = time()
        result = None
        if self.show_results:
            for i in xrange(repeat):
                result = method()
        else:
            for i in xrange(repeat):
                method()
        t2 = time()
        took = t2-t1
        self.rank[took] = method.__name__, result
        self.prnt(method.__name__, took, result)

    def prnt(self, name, took, result=None):
        if result is not None:
            result= "result: %s" % result
        print '%s: %s sec %s' % (name.ljust(40), str(round(took, 5)).ljust(8), result or '')



# -*-  coding: utf-8 -*-
"""
"""

# Copyright (C) 2015 ZetaOps Inc.
#
# This file is licensed under the GNU General Public License v3
# (GPLv3).  See LICENSE.txt for details.

from time import time
import sys

K = 1000
M = K * K
DEFAULT_REPEAT_COUNT = M
try:
    xrange
except NameError:
    xrange = range

class Timer(object):
    def __init__(self, repeat=None, show_results=False, hide_unsorted=True, method_list=[]):
        """

        :param repeat: integer, default: DEFAULT_REPEAT_COUNT number of calls for each method.
        :param show_results: default: False, if True, result of last call to each method will be added to report. defaults
        :param hide_unsorted: default: True, if False timing  of each method will be printed as it completes it's repeats.
        :param method_list: limit tests to listed methods.
        :return:
        """
        super(Timer, self).__init__()
        self._zt_hide_unsorted = hide_unsorted
        self._zt_rank = {}
        self._zt_test_methods = method_list
        self._zt_show_results = show_results
        self._zt_pad_len = 0
        self._zt_repeat = repeat or DEFAULT_REPEAT_COUNT
        self._zt_prepare()
        self._zt_run_tests()
        self._zt_print_reports()

    def _zt_prepare(self):
        longest_method_name_len = 0
        for name in sorted(self._zt_test_methods or self.__class__.__dict__):
            if not name.startswith('__'):
                if len(name) > longest_method_name_len:
                    longest_method_name_len = len(name)
                self._zt_test_methods.append(name)
        self._zt_test_methods = sorted(list(set(self._zt_test_methods)))
        self._zt_pad_len = longest_method_name_len + 3

    def _zt_run_tests(self):

        for method_name in self._zt_test_methods:
            if self._zt_hide_unsorted:
                self._zt_print_progress("Running {} ({:,})  [ {} / {} ]   \r".format(
                    method_name.ljust(self._zt_pad_len),
                    self._zt_repeat, self._zt_test_methods.index(method_name) + 1,
                    len(self._zt_test_methods)))
            method = getattr(self, method_name)
            t1 = time()
            result = ''
            if self._zt_show_results:
                for i in xrange(self._zt_repeat):
                    result = method()
            else:
                for i in xrange(self._zt_repeat):
                    method()
            t2 = time()
            took = t2 - t1
            self._zt_rank[took] = method.__name__, result
            if not self._zt_hide_unsorted:
                self._zt_report(method.__name__, took, result=result)
        if self._zt_hide_unsorted:
            self._zt_print_progress(" \n")

    def _zt_print_progress(self, msg):
        sys.stdout.write(msg)
        sys.stdout.flush()

    def _zt_print_reports(self):
        print("\nEach method run {:,} times:\n".format(self._zt_repeat))
        sorted_ranks = sorted(self._zt_rank)
        for rnk in sorted_ranks:
            itm = self._zt_rank[rnk]
            self._zt_report(itm[0], rnk, result=itm[1],
                        slowness=round(rnk / sorted_ranks[0], 1) if rnk != sorted_ranks[0] else '')

    def _zt_report(self, name, took, slowness='', result=''):
        if result:
            result = "result: %s" % result
        if slowness:
            slowness = "%sx slower" % slowness

        print('%s: %s %s %s' % (name.ljust(self._zt_pad_len), (str(round(took, 5)) + ' sec').ljust(10), slowness, result))

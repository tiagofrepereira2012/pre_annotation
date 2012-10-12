#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Andre Anjos <andre.dos.anjos@gmail.com>
# Wed 15 Aug 09:59:33 2012 

"""Test Units
"""

import unittest

class MyTests(unittest.TestCase):

  def test_version(self):
    from .script import version
    self.assertEqual(version.main(), 0)

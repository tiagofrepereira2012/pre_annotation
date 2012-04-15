#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Andre Anjos <andre.dos.anjos@gmail.com>
# Sun 15 Apr 14:01:39 2012 

"""Prints the version of bob and exits
"""

def main():
  from bob.build import version
  print "The installed version of Bob is '%s'" % version

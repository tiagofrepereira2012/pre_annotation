#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Andre Anjos <andre.dos.anjos@gmail.com>
# Sun 15 Apr 14:01:39 2012 

"""Prints the version of bob and exits
"""

def bob_version(): 
  """Returns the current version of Bob"""

  from bob.build import version

  return version

def main():
  """Main routine, called by the script that gets the version of bob"""

  print "The installed version of Bob is '%s'" % bob_version()

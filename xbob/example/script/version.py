#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Andre Anjos <andre.dos.anjos@gmail.com>
# Sun 15 Apr 14:01:39 2012 

"""Prints the version of bob and exits
"""

def main():
  """Main routine, called by the script that gets the version of bob"""

  import pkg_resources
  packages = pkg_resources.require('bob')
  this = packages[0]
  deps = packages[1:]

  print "The installed version of %s is %s" % (this.key, this.version)
  print "%s is installed at: %s" % (this.key, this.location)
  print "%s depends on the following Python packages:" % (this.key,)
  for d in deps:
    print " * %s: %s (%s)" % (d.key, d.version, d.location)

  return 0

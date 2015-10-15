"""
Script that receives a text file containing all the images to be post process.

Which is basically remove the first line and remove the 0 in front of the coordinates

Usage:

python post_process.py <file.txt>
"""

import sys
import os



def main():

  if(len(sys.argv)!=3):
    print("Wrong number of arguments.")
    print("  Usage: ./bin/pre_annotate.py <file.txt> <input_dir>")
    sys.exit(0)

  files = open(sys.argv[1]).readlines()

  for o in files:
    filename        =  os.path.join(sys.argv[2], o.rstrip("\n")) + ".pos"
    print("Processing the filename {0}".format(filename))
    lines = open(filename,'r').readlines()
    coords = lines[1].split(' ')
    annotations = "{0} {1} {2} {3}".format(str(coords[1]), str(coords[2]), str(coords[3]), str(coords[4]))
    open(filename,'w').write(annotations)
  print("Done!!")
  
if __name__ == "__main__":
  main()

  

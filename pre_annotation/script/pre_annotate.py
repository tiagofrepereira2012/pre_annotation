"""
Script that receives a text file containing all the images to be annotated

Usage:

python pre_annotate.py <file.txt> <image_dir> <output_dir>
"""

import bob.io.base
import bob.io.image
import bob.ip.flandmark
import bob.ip.color
import sys
import os

from cv2 import CascadeClassifier


def main():

  if(len(sys.argv)!=4):
    print("Wrong number of arguments.")
    print("  Usage: ./bin/pre_annotate.py <file.txt> <image_dir> <output_dir>")
    sys.exit(0)


  localizer = bob.ip.flandmark.Flandmark()
  files = open(sys.argv[1]).readlines()

  if os.environ.has_key('SGE_TASK_ID'):
    pos = int(os.environ['SGE_TASK_ID']) - 1
    if pos >= len(files):
      raise RuntimeError, "Grid request for job %d on a setup with %d jobs" % \
          (pos, len(files))
    files = [files[pos]]


  for o in files:
    filename        =  os.path.join(sys.argv[2], o.rstrip("\n"))
    output_filename =  os.path.join(sys.argv[3], o.rstrip("\n")+".pos")

    img = bob.ip.color.rgb_to_gray(bob.io.base.load(filename))
    cc = CascadeClassifier('./pre_annotation/data/haarcascade_frontalface_alt2.xml')

    face_bbxs = cc.detectMultiScale(img, 1.3, 4, 0, (20, 20))
    if(len(face_bbxs)>0):
      key_temp = localizer.locate(img, face_bbxs[0][1], face_bbxs[0][0], face_bbxs[0][2], face_bbxs[0][3])
      if(key_temp is not None):
        R_eye = [ (key_temp[1,0] + key_temp[5,0])/2, (key_temp[1,1] + key_temp[5,1])/2  ]        
        L_eye = [ (key_temp[2,0] + key_temp[6,0])/2, (key_temp[2,1] + key_temp[6,1])/2  ]
        keypoints = [int(L_eye[1]), int(L_eye[0]), int(R_eye[1]), int(R_eye[0])]
                        
      else:
        keypoints = [100,100,100,200]

    else:
      keypoints = [100,100,100,200]

    print("{0}: {1}".format(filename,str(keypoints)))
    bob.io.base.create_directories_safe(os.path.dirname(output_filename))

    annotations = "L R\n0 {0} {1} {2} {3}".format(str(keypoints[0]), str(keypoints[1]), str(keypoints[2]), str(keypoints[3]))
    open(output_filename,'w').write(annotations)  

if __name__ == "__main__":
  main()

  

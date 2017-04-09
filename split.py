import os, sys

filen, suffx = os.path.splitext(sys.argv[1])
os.system("split {0} -l {1} {2}-part -d --verbose --additional-suffix {3}".format(sys.argv[1], sys.argv[2], filen, suffx))
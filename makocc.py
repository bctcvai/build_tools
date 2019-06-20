#!/usr/bin/env python3

import argparse
from mako.template import Template
import traceback
import os
import sys

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("infile")
    parser.add_argument("-o", type=argparse.FileType('w'))
    args=parser.parse_args()

    mytemplate=Template(filename=args.infile, strict_undefined=True)
    if args.o is None:
        print(mytemplate.render())
    else:
        try:
            args.o.write(mytemplate.render())
        except Exception as e:
            traceback.print_exc(file=sys.stdout)
            args.o.close()
            os.remove(args.o.name)

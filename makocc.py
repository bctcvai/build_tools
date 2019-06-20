#!/usr/bin/env python3

import argparse
from mako.template import Template

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("infile")
    parser.add_argument("-o", type=argparse.FileType('w'))
    args=parser.parse_args()

    mytemplate=Template(filename=args.infile, strict_undefined=True)
    if args.o is None:
        print(mytemplate.render())
    else:
        args.o.write(mytemplate.render())

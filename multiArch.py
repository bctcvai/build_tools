#!/usr/bin/env python3

import os
import platform
host=platform.machine()
arch=host
if os.getenv("CROSS_ARCH"):
    arch=os.getenv("CROSS_ARCH")

docker_archMap={"x86_64": "amd64",
                    "aarch64": "arm64"}
google_archMap=docker_archMap
try:
    #Docker uses different architecture names
    docker_arch=docker_archMap[arch]

    #Google uses different architecture names
    google_arch=google_archMap[arch]
except Exception as e:
    pass

def help():
    print("./multiArch.py [--help]")
    print("By default print out docker arch\n")
    print("To cross compile, set environment variable to one of: ")
    for e in docker_archMap.keys():
        print(f"\t{e}")

    print("Current Settings:")
    if os.getenv("CROSS_ARCH"):
        print(f"\tCROSS_ARCH={os.getenv('CROSS_ARCH')}")
    else:
        print("\tCROSS_ARCH is unset")
    print(f"\tHost is '{platform.machine()}'")

    if arch not in docker_archMap:
        print(f"ERROR: '{arch}' is not recognized.")

    

if __name__=="__main__":
    import argparse
    import sys
    parser=argparse.ArgumentParser(add_help=False)
    parser.add_argument("--help",
                        action="store_true")
    parser.add_argument("--buildArgs",
                        action="store_true")
    args=parser.parse_args()
    if args.help:
        help()
        sys.exit(0)

    if args.buildArgs:
        if host != arch:
            print(f"--platform linux/{docker_archMap[arch]}",end='')
    else:
        print(f"linux/{docker_archMap[arch]}",end='')

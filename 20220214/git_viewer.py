#!/usr/bin/env python3.10
import sys
from os.path import join
import os

match len(sys.argv):
    case 1:
        repopath = join('.git', "refs", "heads")
        for branchname in os.listdir(repopath):
            print(branchname)
    case _:
        print("Unknown operands count")

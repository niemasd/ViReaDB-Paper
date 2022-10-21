#! /usr/bin/env python3
'''
Remove reads from a given ViReaDB that only has 1 entry
'''
from os.path import isfile
from resource import getrusage, RUSAGE_CHILDREN, RUSAGE_SELF
from sys import argv
from time import time
from vireadb import load_db
import argparse

# main content
if __name__ == "__main__":
    if len(argv) != 2:
        print("USAGE: %s <db>" % argv[0]); exit(1)
    assert isfile(argv[1]), "Input ViReaDB file not found: %s" % argv[1]
    t1 = time()
    db = load_db(argv[1])
    db.del_reads(db.get_IDs()[0], confirm=False)
    t2 = time(); print("Total Time (s)\t%s" % (t2-t1))
    print("Peak Memory (KB)\t%s" % (getrusage(RUSAGE_SELF).ru_maxrss + getrusage(RUSAGE_CHILDREN).ru_maxrss))

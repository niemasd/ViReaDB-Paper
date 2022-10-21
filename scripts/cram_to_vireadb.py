#! /usr/bin/env python3
'''
Create a ViReaDB database from a given CRAM
'''
from os.path import isfile
from resource import getrusage, RUSAGE_SELF
from sys import argv
from time import time
from vireadb import create_db
import argparse

# main content
if __name__ == "__main__":
    if len(argv) != 4:
        print("USAGE: %s <input_cram> <ref_fas> <output_db>" % argv[0]); exit(1)
    assert isfile(argv[1]), "Input CRAM file not found: %s" % argv[1]
    assert isfile(argv[2]), "Reference FASTA file not found: %s" % argv[2]
    assert not isfile(argv[3]), "Output DB file exists: %s" % argv[3]
    t1 = time()
    db = create_db(argv[3], argv[2])
    db.add_entry(argv[1], argv[1])
    t2 = time(); print("Time to Build DB (s)\t%s" % (t2-t1))
    db.compute_counts(argv[1])
    t3 = time(); print("Time to Compute Counts (s)\t%s" % (t3-t2))
    db.compute_consensus(argv[1])
    t4 = time(); print("Time to Compute Consensus (s)\t%s" % (t4-t3))
    print("Total Time (s)\t%s" % (t4-t1))
    print("Peak Memory (KB)\t%s" % getrusage(RUSAGE_SELF).ru_maxrss)

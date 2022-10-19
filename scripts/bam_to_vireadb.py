#! /usr/bin/env python3
'''
Create a ViReaDB database from a given BAM
'''
from os.path import isfile
from sys import argv
from vireadb import create_db
import argparse

# main content
if __name__ == "__main__":
    if len(argv) != 4:
        print("USAGE: %s <input_bam> <ref_fas> <output_db>" % argv[0]); exit(1)
    assert isfile(argv[1]), "Input BAM file not found: %s" % argv[1]
    assert isfile(argv[2]), "Reference FASTA file not found: %s" % argv[2]
    assert not isfile(argv[3]), "Output DB file exists: %s" % argv[3]
    create_db(argv[3], argv[2]).add_entry(argv[1], argv[1])

#!/usr/bin/env bash
if [ "$#" -ne 4 ] && [ "$#" -ne 5 ] ; then
    echo "USAGE: $0 <ref_fas> <num_reads> <input_cram> <output_cram> [num_threads=1]" ; exit 1
fi
REF=$1 ; N=$2 ; IN=$3 ; OUT=$4 ; THREADS=1
if [ ! -f "$REF" ] ; then
    echo "File not found: $REF" ; exit 1
elif ! test "$N" -gt 0 2> /dev/null ; then
    echo "Number of reads must be positive integer: $N" ; exit 1
elif [ ! -f "$IN" ] ; then
    echo "File not found: $IN" ; exit 1
elif [ -f "$OUT" ] ; then
    echo "File already exists: $OUT" ; exit 1
fi
if [ "$#" -eq 5 ] ; then
    if test "$5" -gt 0 2> /dev/null ; then
        THREADS=$5
    else
        echo "Number of threads must be a positive integer: $5" ; exit 1
    fi
fi
cat <(samtools view -T "$REF" -SH "$IN") <(samtools view -T "$REF" "$IN" | shuf -n $N) | samtools view --output-fmt-option version=3.0 --output-fmt-option use_lzma=1 --output-fmt-option archive=1 --output-fmt-option level=9 --output-fmt-option lossy_names=1 -C -@ $THREADS -o $OUT

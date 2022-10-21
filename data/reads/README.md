[`reads.cram`](reads.cram) was produced by extracting mapped reads from this file, and converting to CRAM:

```
s3://ucsd-all/210730_A00953_0364_BHGYJ7DSX2/210730_A00953_0364_BHGYJ7DSX2_results/2021-08-02_21-03-00_pe/210730_A00953_0364_BHGYJ7DSX2_samples/SEARCH-43114__E0000062__J08__210730_A00953_0364_BHGYJ7DSX2__004/SEARCH-43114__E0000062__J08__210730_A00953_0364_BHGYJ7DSX2__004.trimmed.sorted.bam
```

Create subsamples:

```
for n in 100 1000 10000 100000 1000000 ; do mkdir -p n$n && for r in $(seq -w 1 10) ; do ../../scripts/subsample_cram.sh ../ref/NC_045512.2.fas $n reads.cram n$n.r$r.cram 6 ; done ; done
```

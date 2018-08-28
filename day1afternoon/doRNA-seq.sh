#!/bin/bash

GENOME=../genomes/BDGP6
ANNOTATED=../genomes/BDGP6.Ensembl.81.gtf

for SAMPLE in GENOME 
do 
  mkdir $SAMPLE
  hisat2-build BDGP6.fa BDGP6_index
  samtools view -b BDGP6.sam > BDGP6.bam
  
done

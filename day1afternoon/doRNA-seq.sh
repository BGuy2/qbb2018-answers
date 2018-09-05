#!/bin/bash

GENOME=../genomes/BDGP6
ANNOTATED=../genomes/BDGP6.Ensembl.81.gtf

# copied SRR files into WD

for SAMPLE in SRR072893 SRR072903 SRR72905 SRR072915 
do 
  cd ~/qbb2018-answers/day1afternoon/
  mkdir $SAMPLE
  cd ~/qbb2018-answer/day1afternoon/$SAMPLE
  fastqc ~/data/rawdata/$SAMPLE.fastq
  hisat2 -p 8 -x ~/qbb2018-answers/genomes/BDGP6 -U ~/data/rawdata/$SAMPLE.fastq -S $SAMPLE.sam
  samtools view -S -b $SAMPLE.sam > -o $SAMPLE.bam
  samtools sort $SAMPLE.bam -o $SAMPLE.sorted.bam
  samtools index $SAMPLE.sorted.bam
  stringtie $SAMPLE.sorted.bam -p 8 -e -G ~/qbb2018-anwers/genomes/BDGP6.Ensembl.81.gtf -o $SAMPLE-quant.gtf -B
doner
  
done

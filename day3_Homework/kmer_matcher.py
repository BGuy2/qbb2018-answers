#!/usr/bin/env python3

#this script requires 3 inputs: kmer_matcher.py (target fasta) (query fasta) (kmer size)

import sys
import fasta

target = open (sys.argv[1])

reader = fasta.FASTAReader( target) 

k = sys.argv[3]

target_dict = {} 

#So, brian, tall dude; this is the same code from countkmers.py: but yeilds a dictionary target_dic{kmer,[(gene,pos),(gene 2, pos3)]}
#ident, sequence is arbitraryish, right?
for ident, sequence in reader:
    for i in range( 0, len(sequence) - int(k) ):
        kmer = sequence[i:i + int(k)]
        if kmer not in target_dict:
            target_dict[kmer] = [(ident, i)]
        else:
            target_dict[kmer].append((ident, i))

#alright Moron. Yes Brian, thats you. now we generate kmers from the query, and search for those kmers in target_dict. if its there, we are printing out its name and its position in the target file. 
query = open (sys.argv[2])

reader2 = fasta.FASTAReader( query )

for ident2, sequence2 in reader2:
    for pos in range( 0, len(sequence2) - int(k) ):
        kmer2 = sequence2[pos:pos + int(k)]
        if kmer2 in target_dict:
            for hit in target_dict[kmer2]:
                print( "Match, gene name: " + str(hit[0]) + " Position " + str(hit[1]) + " " + str( kmer2 ) + " "  + str(pos) )
                #ask how you can shorten this line(bring it down a line)
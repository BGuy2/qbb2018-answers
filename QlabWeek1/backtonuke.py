#!/usr/bin/env python3
"""
backtonuke newfasta aligned_aas query
"""
import fasta
import sys
import itertools
import numpy
import matplotlib.pyplot as plt
#import Bio

dna_reader = fasta.FASTAReader(open(sys.argv[1]) )
aa_reader = fasta.FASTAReader(open(sys.argv[2]) )



dna_seq = []
aa_seq= []

for (dna_id, dna), (aa_id, aa) in zip(dna_reader, aa_reader):
    nuc_list= []
    k = 0
    aa_list= []
    for i in range(len(aa)):
        a = aa[i]
        aa_list.append(a)
        nuc = dna[k * 3: (k *3) + 3]
        if a == "-":
            nuc_list.append("---")
        else:    
            nuc_list.append(nuc)
            k += 1 
            
    dna_seq.append(nuc_list)
    aa_seq.append(aa_list)
    

codontable = {'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }
#
# print(len(dna_seq[0]))
# print(len(aa_seq[0]))

dN_list= []
dS_list= []


for j in range(len(dna_seq[0])):
    dS = 0
    dN = 0
    for i in range(1,len(dna_seq)):
        if len(dna_seq[i][j]) != 3:
            pass
        elif dna_seq[0][j] == '':
            pass
        elif dna_seq[0][j] == '---':
            pass
        elif dna_seq[i][j] == "---":
            pass
        elif dna_seq[i][j] == "":
            pass
        elif dna_seq[i][j] == dna_seq[0][j]:
            pass
        elif dna_seq[0][j] not in codontable:
            pass
        elif dna_seq[i][j] not in codontable:
            pass
        elif codontable[dna_seq[0][j]] == codontable[dna_seq[i][j]]:
            dS += 1
        else:
            dN += 1
    dN_list.append(dN)
    dS_list.append(dS)
#
# print(dN_list)
# print(dS_list)

#z= (Dc - Dn)/SE
#
#
# print( numpy.mean(dN_list))
# print( numpy.mean(dS_list))
Diffs_all= []
i = 0
for num in dN_list:
        diff = float(dS_list[i] - float(num))
        Diffs_all.append(diff)
        i += 1 
        
print( Diffs_all)
std_dev= numpy.std(Diffs_all)
print( std_dev)
std_err= float(float(std_dev) / numpy.sqrt(len(Diffs_all)))
print(std_err)

z_list= []
for q in Diffs_all:
    z= float((q - 0)/std_err)
    z_list.append(z)

print( z_list)
    

print("Neat")



fig,ax = plt.subplots()
ax.set_title("Descriptive Title Here")
ax.scatter(range(0,6615),z_list)
ax.set_xlabel("position")
ax.set_ylabel("zlabel")
fig.savefig("zcore")
plt.close(fig)

"""
for each codon, is the mutation significantly different from what we would expect from the null
"""
#
# fig, ax = plt.subplots()
# fig.suptitle( "MA plot" )
# ax.set_xlabel("log(fpkm) " + str(name1))
# ax.scatter(log_a,log_m, alpha= 0.2)
# #I'm thinking theres something wrong with line 34, for some reason my graph is orange
# ax.set_ylabel("log(fpkm) " + str(name2))
# # ax.plot(xplot, yplot)
# # ax.scatter( log_fpkm1, log_fpkm2)
# fig.savefig("day4MA.png")
# plt.close(fig)

#
# def twoSampZ(X1, X2, mudiff, sd1, sd2, n1, n2):
#     from scipy.stats import norm
#     pooledSE = sqrt(sd1**2/n1 + sd2**2/n2)
#     z = ((X1 - X2) - mudiff)/pooledSE
#     pval = 2*(1 - norm.cdf(abs(z)))
#     return round(z, 3), round(pval, 4)
#
#
#
# #
# # for i in dna_seq[0:][0:]:
#     if i == '---' or '':
#         dna_seq[0].remove(i)
    
    #
# codons = []
# i = 0
# for (qu_id, seq) in quarry:
#     for char in seq:
#         codons.append(seq[i:(i + 3)])
#         i = i + 3
#         if i >= len(seq):
#             break
# print(len(codons))








#print( "Neat")


# for i in dna_seq :
#     if i == '':
#       dna_seq.remove(i)
#
# ref_nuc = dna_seq[0]
# ref_aa = aa_seq[0]
##
#


#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt

#
# for line in open(sys.argv[1]):
#     if line.startswith("#"):
#         continue
#     else:
#         fields = line.strip("\r\n").split("\t")
#         columns = fields[7].split(";")
#         deptp = columns[7].split("=")
#         print(deptp)
#         plt.figure()
#         # count = 0
# #         for item in deptp:
# #             if type(item[1]) != int:
# #                 pass
# #             else:
# #                 count += 1
# #                 depth = item[1]
# #                 plt.plot(count,int(depth))
# #                #
#
#         plt.xlabel( 'count' )
#         plt.ylabel( 'coverage' )
#         plt.title( "coverage per sample" )
#         plt.savefig( "depth.png")
#         plt.close()
#

Depths=[]

for line in open(sys.argv[1]):
    if line.startswith("#"):
        continue
    else:
        fields = line.strip("\r\n").split("\t")
        columns = fields[7].split(";")
        deptp = columns[7].split("=")
        #print(deptp)
        values = deptp[1].strip("\r\n").split(",")
        bettervalues = values[0]
        Depths.append(bettervalues)
count = len(Depths)
print(count)
print(Depths)

plt.figure()
plt.plot(range(count), Depths )
plt.xlabel( 'count' )
plt.ylabel( 'coverage' )
plt.title( "coverage per sample" )
plt.savefig( "depth.png")
plt.close()

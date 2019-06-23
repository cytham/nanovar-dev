"""
This script parses the output from HS-BLASTN.

Copyright (C) 2019 Tham Cheng Yong, Roberto Tirado Magallanes, Touati Benoukraf.

This file is part of NanoVar.

NanoVar is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

NanoVar is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with NanoVar.  If not, see <https://www.gnu.org/licenses/>.
"""

from sys import argv
import sys
import os
import logging

#Ensure correct number of inputs
if len(argv)<4 or len(argv)>=5:
    sys.exit("Usage: python nv_hsblast_parse.py file.hsblast file.fa log_file > output.tsv")

#Assign variable to inputs
file1 = argv[1]
file2 = argv[2]
log_path = argv[3]

#Calculating query lengths
def measureQlen(fasta):
    global qlendict
    qlendict = {}
    with open(fasta) as f:
        line1 = [next(f) for x in range(2)]
        if line1[0][0] == '>': #fasta
            qlendict[line1[0].split()[0][1:].strip()] = len(line1[1].strip())
            lc = 0
            for line in f:
                qlendict[line.split()[0][1:].strip()] = len(next(f).strip())
        elif line1[0][0] == '@': #fastq
            qlendict[line1[0].split()[0][1:].strip()] = len(line1[1].strip())
            line2 = [next(f) for x in range(2)]
            lc = 0
            for line in f:
                if lc == 0:
                    qlendict[line.split()[0][1:].strip()] = len(next(f).strip())
                    lc = 1
                else:
                    lc += 1
                    if lc == 3:
                        lc = 0
    return qlendict

#Detects strandedness of an alignment
def strander(line):
    if line.split('\t')[8] < line.split('\t')[9]:
        return "+"
    elif line.split('\t')[8] > line.split('\t')[9]:
        return "-"

#Gathering alignment information and parsing
def info(line):
    qid = line.split('\t')[0]
    sid = line.split('\t')[1]
    piden = line.split('\t')[2]
    nmismatch = line.split('\t')[4]
    ngapopen = line.split('\t')[5]
    qstart = line.split('\t')[6]
    qstretch = int(line.split('\t')[7]) - int(line.split('\t')[6])
    sstart = min(int(line.split('\t')[8]), int(line.split('\t')[9]))
    sstretch = abs(int(line.split('\t')[9]) - int(line.split('\t')[8]))
    evalue = line.split('\t')[10]
    bitscore = line.split('\t')[11].strip('\n')
    strand = strander(line)
    qlen = qlendict[qid]
    entry = sid + '\t' + str(sstart) + '\t' + str(sstretch) + '\t+\t' + qid + '\t' + qstart + '\t' + str(qstretch) + '\t' + strand + '\t' + str(qlen) + '\t' + evalue + '\t' + bitscore + '\t' + piden + '\t' + nmismatch + '\t' + ngapopen
    return entry

def getbitscore(line):
    return float(line.split('\t')[10])

def main():
    qlendict = measureQlen(file2)
    tmp = []
    with open(file1, 'r') as hsblast:
        for line in hsblast:
            tmp.append(info(line))
    tmp.append('null\tnull\tnull\tnull\tnull\tnull')
    l = len(tmp) - 1
    overlap_tolerance = 0.9
    temp = []
    temp2 = []
    output = []
    #For Collecting chromosome number
    chromocollect = []
    for i in range(l):
        if tmp[i].split('\t')[4] == tmp[i+1].split('\t')[4]: #Grouping alignments by readname
            temp.append(tmp[i])
            if tmp[i].split('\t')[0].strip() not in chromocollect:
                chromocollect.append(tmp[i].split('\t')[0].strip())
        else:
            temp.append(tmp[i])
            if tmp[i].split('\t')[0].strip() not in chromocollect:
                chromocollect.append(tmp[i].split('\t')[0].strip())
            nchr = len(chromocollect)
            h = len(temp) #total number of alignments
            while len(temp) != 0:
                temp.sort(key=getbitscore, reverse=True) #Order by bitscore
                temp2.append(temp[0] + '\tn=' + str(h) + '\t' + str(nchr) + 'chr') #Lock in lead alignment (highest bitscore)
                leadrange = [int(temp[0].split('\t')[5]), int(temp[0].split('\t')[5]) + int(temp[0].split('\t')[6])]
                del temp[0] #remove lead alignment entry
                j = len(temp)
                temp3 = []
                for p in range(j):
                    queryx = [int(temp[p].split('\t')[5]), int(temp[p].split('\t')[5]) + int(temp[p].split('\t')[6])]
                    queryrange = range(int(temp[p].split('\t')[5]), int(temp[p].split('\t')[5]) + int(temp[p].split('\t')[6]) + 1)
                    leadintersect = range(max(leadrange[0], queryx[0]), min(leadrange[1], queryx[1]) + 1)
                    if len(leadintersect) == 0: #Good, no intersect with lead
                        temp3.append(temp[p])
                    else:
                        new = ''
                        qulen = len(queryrange)
                        leadintlen = len(leadintersect)
                        if float(leadintlen)/qulen > overlap_tolerance: #Check if overlap len is more than x% of query alignment length. Means that x% of query is overlapped, therefore considered weak alignment compared to lead alignment
                            continue #omitted
                        else: #If overlap is tolerated, then do trimming
                            sign = str(temp[p].split('\t')[7])
                            if queryx[0] == min(leadintersect): #left overlap
                                if sign == '+': #alter query and subject ranges and adjust bitscore as a proportion of alignment length
                                    new = temp[p].split('\t')[0] + '\t' + str(int(temp[p].split('\t')[1]) + leadintlen) + '\t' + str(int(temp[p].split('\t')[2]) - leadintlen) + '\t' + '\t'.join(temp[p].split('\t')[3:5]) + '\t' + str(int(temp[p].split('\t')[5]) + leadintlen) + '\t' + str(int(temp[p].split('\t')[6]) - leadintlen) + '\t' + '\t'.join(temp[p].split('\t')[7:10]) + '\t' + str(round(float(temp[p].split('\t')[10])*(float(qulen - leadintlen)/qulen), 2)) + '\t' + '\t'.join(temp[p].split('\t')[11:])
                                elif sign == '-':
                                    new = temp[p].split('\t')[0] + '\t' + temp[p].split('\t')[1] + '\t' + str(int(temp[p].split('\t')[2]) - leadintlen) + '\t' + '\t'.join(temp[p].split('\t')[3:5]) + '\t' + str(int(temp[p].split('\t')[5]) + leadintlen) + '\t' + str(int(temp[p].split('\t')[6]) - leadintlen) + '\t' + '\t'.join(temp[p].split('\t')[7:10]) + '\t' + str(round(float(temp[p].split('\t')[10])*(float(qulen - leadintlen)/qulen), 2)) + '\t' + '\t'.join(temp[p].split('\t')[11:])
                            elif queryx[1] == max(leadintersect): #right overlap
                                if sign == '+':
                                    new = temp[p].split('\t')[0] + '\t' + temp[p].split('\t')[1] + '\t' + str(int(temp[p].split('\t')[2]) - leadintlen) + '\t' + '\t'.join(temp[p].split('\t')[3:5]) + '\t' + temp[p].split('\t')[5] + '\t' + str(int(temp[p].split('\t')[6]) - leadintlen) + '\t' + '\t'.join(temp[p].split('\t')[7:10]) + '\t' + str(round(float(temp[p].split('\t')[10])*(float(qulen - leadintlen)/qulen), 2)) + '\t' + '\t'.join(temp[p].split('\t')[11:])
                                elif sign == '-':
                                    new = temp[p].split('\t')[0] + '\t' + str(int(temp[p].split('\t')[1]) + leadintlen) + '\t' + str(int(temp[p].split('\t')[2]) - leadintlen) + '\t' + '\t'.join(temp[p].split('\t')[3:5]) + '\t' + temp[p].split('\t')[5] + '\t' + str(int(temp[p].split('\t')[6]) - leadintlen) + '\t' + '\t'.join(temp[p].split('\t')[7:10]) + '\t' + str(round(float(temp[p].split('\t')[10])*(float(qulen - leadintlen)/qulen), 2)) + '\t' + '\t'.join(temp[p].split('\t')[11:])
                            else: #If intersection lies entirely within the lead, omit query
                                continue
                            if int(new.split('\t')[2]) > 0:
                                temp3.append(new)
                temp = temp3
            sortdict = {}
            for k in temp2:
                sortdict[int(k.split('\t')[5])] = k
            output = [value for (key, value) in sorted(sortdict.items())]
            for n in output:
                print(n)
            temp = []
            temp2 = []
            output = []
            chromocollect = []

if __name__ == '__main__':
    main()

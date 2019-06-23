"""
This script is used for make check.

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

if len(argv)<5 or len(argv)>=6:
    sys.exit("Usage: python nv_test.py md5sumfile [b1 or b0] maindir [linux or mac]")

md5_file = argv[1]
bowtie = argv[2]
maindir = argv[3]
machtype = argv[4]
md5_names = open(md5_file, 'r').read().splitlines()
md5 = []
for i in md5_names:
    md5.append(i.split(' ')[0])

def checker(test, ref):
    if test == ref:
        return 1
    else:
        return 0

#cut -f 1 -d' ' md5.out  | perl -pe 's/\n/\+/g'

lb = 'f846237582adf9340d40f9c23e2563e4+353914b702cdb564ebfa41fa8819bc77+3168ccfb91a64a6d0e3174b05bab9adf+399fa36013ebec490df7923963ed6892+c76d425ecd5af4ef0c6059da6e4bb847+b95f9a36c118811952a149562a7f2d61+8ef81022eb9c2d12e67eb0f79982d152+45d73fff1fd267ff5606831f99a0952d+dd20f9ca6221d6ccb3ac9f686e7564b1+371ab7815cca215b63d0acbac245ff4c+3c4bddf8ddc525bc0fee6ea2ad1ac714+8506e7d6ecdb13a205dfb5ddc0ee6870+2c5c01b1dcfe571a074120d5ae151051+0b30579e91aeb001cdb57701cbe31579+8c68ba585e3584c0c8e8b2ad13964faf+5faee0c81428759824ba3a933f486e5b+8b349cca5cb9d003c9e80a1490f209d8+a8eaecee4e063d9f345dfba92d023e4b+05b2165304639d42f3217f0108f32189+bde26f7abea332ed0a36aad88da4d787+ca7a90f610d907ba166e2f4b3537d422+98e80622974ae5c6e9f3c73d8931454b+347f23dd69e5488f81bcdabdddecb996+a1779ecf3b69e587dad9ba034b0e3537+9e224ca09361d90bca972bbf97331d78+805cf95c7e10d2d3cbfc0f570e0a95b7+2a25c634f68b9831302a9d3f82dd7396+fd18ade05ea1c05ba7bd915baca2c36d+c5e323aac84839829669b86e5e359c9a+afb1218ebdba8841719f4ef3328bc8e8+a0eeafb3fddcf10dbfea3447ff3a532c+1dadfc7dcf7530c7a7926d2fc2f8c801+dc84e54bae57d53bc0d4e83d63fa7c9e+61c24dcb5f4c6b23689a933677ad2e2f+4decc1cfc26a13d34b8becf8faf0dd69+b3e0bc41abacd249cfd99ab58537a3aa+5d5aeb32871bf06a25cd1ff92be3c595+6420a30ea45e100d84db2fef5360866a+2801a3ff17d7cdd295c757cdf7b1749b'.split('+')

lnb = 'f846237582adf9340d40f9c23e2563e4+353914b702cdb564ebfa41fa8819bc77+3168ccfb91a64a6d0e3174b05bab9adf+399fa36013ebec490df7923963ed6892+c76d425ecd5af4ef0c6059da6e4bb847+b95f9a36c118811952a149562a7f2d61+8df70c335a4d277d2512df839dbdbf02+45d73fff1fd267ff5606831f99a0952d+dd20f9ca6221d6ccb3ac9f686e7564b1+2cca3ea71e4b25920d421eeec5606ece+3c4bddf8ddc525bc0fee6ea2ad1ac714+8506e7d6ecdb13a205dfb5ddc0ee6870+2c5c01b1dcfe571a074120d5ae151051+0b30579e91aeb001cdb57701cbe31579+8c68ba585e3584c0c8e8b2ad13964faf+5faee0c81428759824ba3a933f486e5b+8b349cca5cb9d003c9e80a1490f209d8+a8eaecee4e063d9f345dfba92d023e4b+05b2165304639d42f3217f0108f32189+7b840430835a55c98465f94c4ac22708+e32107036876fc74355d615c9862096a+8adfdaef5362c76a5392305b52a5c3ab+1dadfc7dcf7530c7a7926d2fc2f8c801+fb2f1c3705a15886c7706bb94d379d79+61c24dcb5f4c6b23689a933677ad2e2f+4decc1cfc26a13d34b8becf8faf0dd69+b3e0bc41abacd249cfd99ab58537a3aa+5d5aeb32871bf06a25cd1ff92be3c595+6420a30ea45e100d84db2fef5360866a+2801a3ff17d7cdd295c757cdf7b1749b'.split('+')

mb = ''.split('+')

mnb = ''.split('+')

def main():
    if machtype == "linux":
        if bowtie == "b1": #Enabled bowtie2
            if checker(md5[0], lb[0]):
                print("<Reference> ---------: Checked")
            else:
                print("<Reference> ---------: Failed")
                sys.exit("Test data file corrupted, please re-download NanoVar")
            if checker(md5[1], lb[1]):
                print("<longfa>    ---------: Checked")
            else:
                print("<longfa>    ---------: Failed")
                sys.exit("Test data file corrupted, please re-download NanoVar")
            if checker(md5[2], lb[2]):
                print("<shortfa1>  ---------: Checked")
            else:
                print("<shortfa1>  ---------: Failed")
                sys.exit("Test data file corrupted, please re-download NanoVar")
            if checker(md5[3], lb[3]):
                print("<shortfa2>  ---------: Checked")
            else:
                print("<shortfa2>  ---------: Failed")
                sys.exit("Test data file corrupted, please re-download NanoVar")
            if checker(md5[4], lb[4]):
                print("<fai>       ---------: Passed")
            else:
                print("<fai>       ---------: Failed")
                sys.exit("Samtools faidx failed, please ensure samtools is functional")
            if checker(md5[5], lb[5]):
                print("<nhr>       ---------: Passed")
            else:
                print("<nhr>       ---------: Failed")
                sys.exit("makeblastdb failed, please download Blast v2.7.1+ source, build it and copy 'makeblastdb' binaries into " + maindir + "/blast/")
            if checker(md5[7], lb[7]):
                print("<nsq>       ---------: Passed")
            else:
                print("<nsq>       ---------: Failed")
                sys.exit("makeblastdb failed, please download Blast v2.7.1+ source, build it and copy 'makeblastdb' binaries into " + maindir + "/blast/")
            if checker(md5[8], lb[8]):
                print("<bwt>       ---------: Passed")
            else:
                print("<bwt>       ---------: Failed")
                sys.exit("hsblast index failed, please re-configure and re-compile NanoVar")
            if checker(md5[10], lb[10]):
                print("<sa>        ---------: Passed")
            else:
                print("<sa>        ---------: Failed")
                sys.exit("hsblast index failed, please re-configure and re-compile NanoVar")
            if checker(md5[11], lb[11]):
                print("<sequence>  ---------: Passed")
            else:
                print("<sequence>  ---------: Failed")
                sys.exit("hsblast index failed, please re-configure and re-compile NanoVar")
            if checker(md5[12], lb[12]):
                print("<counts>    ---------: Passed")
            else:
                print("<counts>    ---------: Failed")
                sys.exit("windowmasker failed, please download Blast v2.7.1+ source, build it and copy 'windowmasker' binaries into " + maindir + "/blast/")
            if checker(md5[13], lb[13]):
                print("<obinary>   ---------: Passed")
            else:
                print("<obinary>   ---------: Failed")
                sys.exit("windowmasker failed, please download Blast v2.7.1+ source, build it and copy 'windowmasker' binaries into " + maindir + "/blast/")
            if checker(md5[14], lb[14]):
                print("<align>     ---------: Passed")
            else:
                print("<align>     ---------: Failed")
                sys.exit("hsblast align failed, please re-configure and re-compile NanoVar")
            if checker(md5[15], lb[15]):
                print("<parse>     ---------: Passed")
            else:
                print("<parse>     ---------: Failed")
                sys.exit("bedtools sort failed, please ensure bedtools version >= 2.26.0 and functional")
            if checker(md5[16], lb[16]):
                print("<overlap>   ---------: Passed")
            else:
                print("<overlap>   ---------: Failed")
                sys.exit("bedtools intersect or awk failed, please ensure bedtools version >= 2.26.0 and awk are functional")
            if checker(md5[17], lb[17]):
                print("<ANN>       ---------: Passed")
            else:
                print("<ANN>       ---------: Failed")
                sys.exit("python3 failed, please ensure python3 is in PATH and functional")
            if checker(md5[18], lb[18]):
                print("<ANN0>      ---------: Passed")
            else:
                print("<ANN0>      ---------: Failed")
                sys.exit("awk failed, please ensure awk is functional")
            if checker(md5[19], lb[19]):
                print("<bt1>       ---------: Passed")
            else:
                print("<bt1>       ---------: Failed")
                sys.exit("bowtie2-build failed, please ensure bowtie2-build is functional")
            if checker(md5[20], lb[20]):
                print("<bt2>       ---------: Passed")
            else:
                print("<bt2>       ---------: Failed")
                sys.exit("bowtie2-build failed, please ensure bowtie2-build is functional")
            if checker(md5[21], lb[21]):
                print("<bt3>       ---------: Passed")
            else:
                print("<bt3>       ---------: Failed")
                sys.exit("bowtie2-build failed, please ensure bowtie2-build is functional")
            if checker(md5[22], lb[22]):
                print("<bt4>       ---------: Passed")
            else:
                print("<bt4>       ---------: Failed")
                sys.exit("bowtie2-build failed, please ensure bowtie2-build is functional")
            if checker(md5[23], lb[23]):
                print("<revbt1>    ---------: Passed")
            else:
                print("<revbt1>    ---------: Failed")
                sys.exit("bowtie2-build failed, please ensure bowtie2-build is functional")
            if checker(md5[24], lb[24]):
                print("<revbt2>    ---------: Passed")
            else:
                print("<revbt2>    ---------: Failed")
                sys.exit("bowtie2-build failed, please ensure bowtie2-build is functional")
            if checker(md5[25], lb[25]):
                print("<bam-sam>   ---------: Passed")
            else:
                print("<bam-sam>   ---------: Failed")
                sys.exit("bowtie2 align or samtools view/sort failed, please ensure bowtie2 and samtools are functional")
            if checker(md5[26], lb[26]):
                print("<fq1>       ---------: Passed")
            else:
                print("<fq1>       ---------: Failed")
                sys.exit("samtools fastq failed, please ensure samtools is functional")
            if checker(md5[27], lb[27]):
                print("<fq2>       ---------: Passed")
            else:
                print("<fq2>       ---------: Failed")
                sys.exit("samtools fastq failed, please ensure samtools is functional")
            if checker(md5[28], lb[28]):
                print("<cov>       ---------: Passed")
            else:
                print("<cov>       ---------: Failed")
                sys.exit("bedtools map or awk or sort failed, please ensure bedtools and awk and sort are functional")
            if checker(md5[29], lb[29]):
                print("<t-vcf>     ---------: Passed")
            else:
                print("<t-vcf>     ---------: Failed")
                sys.exit("bedtools sort failed, please ensure bedtools is functional")
            if checker(md5[30], lb[30]):
                print("<filt-vcf>  ---------: Passed")
            else:
                print("<filt-vcf>  ---------: Failed")
                sys.exit("bedtools sort or awk failed, please ensure bedtools and awk are functional")
            if checker(md5[31], lb[31]):
                print("<svoverlap> ---------: Passed")
            else:
                print("<svoverlap> ---------: Failed")
                sys.exit("awk or sed failed, please ensure awk and sed are functional")
            os.system('echo "AllPassed" > ' + maindir + '/test/AllPassed')
        elif bowtie == "b0": #Disabled bowtie2
            if checker(md5[0], lnb[0]):
                print("<Reference> ---------: Checked")
            else:
                print("<Reference> ---------: Failed")
                sys.exit("Test data file corrupted, please re-download NanoVar")
            if checker(md5[1], lnb[1]):
                print("<longfa>    ---------: Checked")
            else:
                print("<longfa>    ---------: Failed")
                sys.exit("Test data file corrupted, please re-download NanoVar")
            if checker(md5[2], lnb[2]):
                print("<shortfa1>  ---------: Checked")
            else:
                print("<shortfa1>  ---------: Failed")
                sys.exit("Test data file corrupted, please re-download NanoVar")
            if checker(md5[3], lnb[3]):
                print("<shortfa2>  ---------: Checked")
            else:
                print("<shortfa2>  ---------: Failed")
                sys.exit("Test data file corrupted, please re-download NanoVar")
            if checker(md5[4], lnb[4]):
                print("<fai>       ---------: Passed")
            else:
                print("<fai>       ---------: Failed")
                sys.exit("Samtools faidx failed, please ensure samtools is functional")
            if checker(md5[5], lnb[5]):
                print("<nhr>       ---------: Passed")
            else:
                print("<nhr>       ---------: Failed")
                sys.exit("makeblastdb failed, please download Blast v2.7.1+ source, build it and copy 'makeblastdb' binaries into " + maindir + "/blast/")
            if checker(md5[7], lnb[7]):
                print("<nsq>       ---------: Passed")
            else:
                print("<nsq>       ---------: Failed")
                sys.exit("makeblastdb failed, please download Blast v2.7.1+ source, build it and copy 'makeblastdb' binaries into " + maindir + "/blast/")
            if checker(md5[8], lnb[8]):
                print("<bwt>       ---------: Passed")
            else:
                print("<bwt>       ---------: Failed")
                sys.exit("hsblast index failed, please re-configure and re-compile NanoVar")
            if checker(md5[10], lnb[10]):
                print("<sa>        ---------: Passed")
            else:
                print("<sa>        ---------: Failed")
                sys.exit("hsblast index failed, please re-configure and re-compile NanoVar")
            if checker(md5[11], lnb[11]):
                print("<sequence>  ---------: Passed")
            else:
                print("<sequence>  ---------: Failed")
                sys.exit("hsblast index failed, please re-configure and re-compile NanoVar")
            if checker(md5[12], lnb[12]):
                print("<counts>    ---------: Passed")
            else:
                print("<counts>    ---------: Failed")
                sys.exit("windowmasker failed, please download Blast v2.7.1+ source, build it and copy 'windowmasker' binaries into " + maindir + "/blast/")
            if checker(md5[13], lnb[13]):
                print("<obinary>   ---------: Passed")
            else:
                print("<obinary>   ---------: Failed")
                sys.exit("windowmasker failed, please download Blast v2.7.1+ source, build it and copy 'windowmasker' binaries into " + maindir + "/blast/")
            if checker(md5[14], lnb[14]):
                print("<align>     ---------: Passed")
            else:
                print("<align>     ---------: Failed")
                sys.exit("hsblast align failed, please re-configure and re-compile NanoVar")
            if checker(md5[15], lnb[15]):
                print("<parse>     ---------: Passed")
            else:
                print("<parse>     ---------: Failed")
                sys.exit("bedtools sort failed, please ensure bedtools version >= 2.26.0 and functional")
            if checker(md5[16], lnb[16]):
                print("<overlap>   ---------: Passed")
            else:
                print("<overlap>   ---------: Failed")
                sys.exit("bedtools intersect or awk failed, please ensure bedtools version >= 2.26.0 and awk are functional")
            if checker(md5[17], lnb[17]):
                print("<ANN>       ---------: Passed")
            else:
                print("<ANN>       ---------: Failed")
                sys.exit("python3 failed, please ensure python3 is in PATH and functional")
            if checker(md5[18], lnb[18]):
                print("<ANN0>      ---------: Passed")
            else:
                print("<ANN0>      ---------: Failed")
                sys.exit("awk failed, please ensure awk is functional")
            if checker(md5[19], lnb[19]):
                print("<cov>       ---------: Passed")
            else:
                print("<cov>       ---------: Failed")
                sys.exit("awk or sort failed, please ensure awk and sort are functional")
            if checker(md5[20], lnb[20]):
                print("<t-vcf>     ---------: Passed")
            else:
                print("<t-vcf>     ---------: Failed")
                sys.exit("bedtools sort failed, please ensure bedtools is functional")
            if checker(md5[21], lnb[21]):
                print("<filt-vcf>  ---------: Passed")
            else:
                print("<filt-vcf>  ---------: Failed")
                sys.exit("bedtools sort or awk failed, please ensure bedtools and awk are functional")
            if checker(md5[22], lnb[22]):
                print("<svoverlap> ---------: Passed")
            else:
                print("<svoverlap> ---------: Failed")
                sys.exit("awk or sed failed, please ensure awk and sed are functional")
            os.system('echo "AllPassed" > ' + maindir + '/test/AllPassed')
    elif machtype == "mac":
        if bowtie == "b1": #Enabled bowtie2
            if checker(md5[0], mb[0]):
                print("<Reference> ---------: Checked")
            else:
                print("<Reference> ---------: Failed")
                sys.exit("Test data file corrupted, please re-download NanoVar")
            if checker(md5[1], mb[1]):
                print("<longfa>    ---------: Checked")
            else:
                print("<longfa>    ---------: Failed")
                sys.exit("Test data file corrupted, please re-download NanoVar")
            if checker(md5[2], mb[2]):
                print("<shortfa1>  ---------: Checked")
            else:
                print("<shortfa1>  ---------: Failed")
                sys.exit("Test data file corrupted, please re-download NanoVar")
            if checker(md5[3], mb[3]):
                print("<shortfa2>  ---------: Checked")
            else:
                print("<shortfa2>  ---------: Failed")
                sys.exit("Test data file corrupted, please re-download NanoVar")
            if checker(md5[4], mb[4]):
                print("<fai>       ---------: Passed")
            else:
                print("<fai>       ---------: Failed")
                sys.exit("Samtools faidx failed, please ensure samtools is functional")
            if checker(md5[5], mb[5]):
                print("<nhr>       ---------: Passed")
            else:
                print("<nhr>       ---------: Failed")
                sys.exit("makeblastdb failed, please download Blast v2.7.1+ source, build it and copy 'makeblastdb' binaries into " + maindir + "/blast/")
            if checker(md5[7], mb[7]):
                print("<nsq>       ---------: Passed")
            else:
                print("<nsq>       ---------: Failed")
                sys.exit("makeblastdb failed, please download Blast v2.7.1+ source, build it and copy 'makeblastdb' binaries into " + maindir + "/blast/")
            if checker(md5[8], mb[8]):
                print("<bwt>       ---------: Passed")
            else:
                print("<bwt>       ---------: Failed")
                sys.exit("hsblast index failed, please re-configure and re-compile NanoVar")
            if checker(md5[10], mb[10]):
                print("<sa>        ---------: Passed")
            else:
                print("<sa>        ---------: Failed")
                sys.exit("hsblast index failed, please re-configure and re-compile NanoVar")
            if checker(md5[11], mb[11]):
                print("<sequence>  ---------: Passed")
            else:
                print("<sequence>  ---------: Failed")
                sys.exit("hsblast index failed, please re-configure and re-compile NanoVar")
            if checker(md5[12], mb[12]):
                print("<counts>    ---------: Passed")
            else:
                print("<counts>    ---------: Failed")
                sys.exit("windowmasker failed, please download Blast v2.7.1+ source, build it and copy 'windowmasker' binaries into " + maindir + "/blast/")
            if checker(md5[13], mb[13]):
                print("<obinary>   ---------: Passed")
            else:
                print("<obinary>   ---------: Failed")
                sys.exit("windowmasker failed, please download Blast v2.7.1+ source, build it and copy 'windowmasker' binaries into " + maindir + "/blast/")
            if checker(md5[14], mb[14]):
                print("<align>     ---------: Passed")
            else:
                print("<align>     ---------: Failed")
                sys.exit("hsblast align failed, please re-configure and re-compile NanoVar")
            if checker(md5[15], mb[15]):
                print("<parse>     ---------: Passed")
            else:
                print("<parse>     ---------: Failed")
                sys.exit("bedtools sort failed, please ensure bedtools version >= 2.26.0 and functional")
            if checker(md5[16], mb[16]):
                print("<overlap>   ---------: Passed")
            else:
                print("<overlap>   ---------: Failed")
                sys.exit("bedtools intersect or awk failed, please ensure bedtools version >= 2.26.0 and awk are functional")
            if checker(md5[17], mb[17]):
                print("<ANN>       ---------: Passed")
            else:
                print("<ANN>       ---------: Failed")
                sys.exit("python3 failed, please ensure python3 is in PATH and functional")
            if checker(md5[18], mb[18]):
                print("<ANN0>      ---------: Passed")
            else:
                print("<ANN0>      ---------: Failed")
                sys.exit("awk failed, please ensure awk is functional")
            if checker(md5[19], mb[19]):
                print("<bt1>       ---------: Passed")
            else:
                print("<bt1>       ---------: Failed")
                sys.exit("bowtie2-build failed, please ensure bowtie2-build is functional")
            if checker(md5[20], mb[20]):
                print("<bt2>       ---------: Passed")
            else:
                print("<bt2>       ---------: Failed")
                sys.exit("bowtie2-build failed, please ensure bowtie2-build is functional")
            if checker(md5[21], mb[21]):
                print("<bt3>       ---------: Passed")
            else:
                print("<bt3>       ---------: Failed")
                sys.exit("bowtie2-build failed, please ensure bowtie2-build is functional")
            if checker(md5[22], mb[22]):
                print("<bt4>       ---------: Passed")
            else:
                print("<bt4>       ---------: Failed")
                sys.exit("bowtie2-build failed, please ensure bowtie2-build is functional")
            if checker(md5[23], mb[23]):
                print("<revbt1>    ---------: Passed")
            else:
                print("<revbt1>    ---------: Failed")
                sys.exit("bowtie2-build failed, please ensure bowtie2-build is functional")
            if checker(md5[24], mb[24]):
                print("<revbt2>    ---------: Passed")
            else:
                print("<revbt2>    ---------: Failed")
                sys.exit("bowtie2-build failed, please ensure bowtie2-build is functional")
            if checker(md5[25], mb[25]):
                print("<bam-sam>   ---------: Passed")
            else:
                print("<bam-sam>   ---------: Failed")
                sys.exit("bowtie2 align or samtools view/sort failed, please ensure bowtie2 and samtools are functional")
            if checker(md5[26], mb[26]):
                print("<fq1>       ---------: Passed")
            else:
                print("<fq1>       ---------: Failed")
                sys.exit("samtools fastq failed, please ensure samtools is functional")
            if checker(md5[27], mb[27]):
                print("<fq2>       ---------: Passed")
            else:
                print("<fq2>       ---------: Failed")
                sys.exit("samtools fastq failed, please ensure samtools is functional")
            if checker(md5[28], mb[28]):
                print("<cov>       ---------: Passed")
            else:
                print("<cov>       ---------: Failed")
                sys.exit("bedtools map or awk or sort failed, please ensure bedtools and awk and sort are functional")
            if checker(md5[29], mb[29]):
                print("<t-vcf>     ---------: Passed")
            else:
                print("<t-vcf>     ---------: Failed")
                sys.exit("bedtools sort failed, please ensure bedtools is functional")
            if checker(md5[30], mb[30]):
                print("<filt-vcf>  ---------: Passed")
            else:
                print("<filt-vcf>  ---------: Failed")
                sys.exit("bedtools sort or awk failed, please ensure bedtools and awk are functional")
            if checker(md5[31], mb[31]):
                print("<svoverlap> ---------: Passed")
            else:
                print("<svoverlap> ---------: Failed")
                sys.exit("awk or sed failed, please ensure awk and sed are functional")
            os.system('echo "AllPassed" > ' + maindir + '/test/AllPassed')
        elif bowtie == "b0": #Disabled bowtie2
            if checker(md5[0], mnb[0]):
                print("<Reference> ---------: Checked")
            else:
                print("<Reference> ---------: Failed")
                sys.exit("Test data file corrupted, please re-download NanoVar")
            if checker(md5[1], mnb[1]):
                print("<longfa>    ---------: Checked")
            else:
                print("<longfa>    ---------: Failed")
                sys.exit("Test data file corrupted, please re-download NanoVar")
            if checker(md5[2], mnb[2]):
                print("<shortfa1>  ---------: Checked")
            else:
                print("<shortfa1>  ---------: Failed")
                sys.exit("Test data file corrupted, please re-download NanoVar")
            if checker(md5[3], mnb[3]):
                print("<shortfa2>  ---------: Checked")
            else:
                print("<shortfa2>  ---------: Failed")
                sys.exit("Test data file corrupted, please re-download NanoVar")
            if checker(md5[4], mnb[4]):
                print("<fai>       ---------: Passed")
            else:
                print("<fai>       ---------: Failed")
                sys.exit("Samtools faidx failed, please ensure samtools is functional")
            if checker(md5[5], mnb[5]):
                print("<nhr>       ---------: Passed")
            else:
                print("<nhr>       ---------: Failed")
                sys.exit("makeblastdb failed, please download Blast v2.7.1+ source, build it and copy 'makeblastdb' binaries into " + maindir + "/blast/")
            if checker(md5[7], mnb[7]):
                print("<nsq>       ---------: Passed")
            else:
                print("<nsq>       ---------: Failed")
                sys.exit("makeblastdb failed, please download Blast v2.7.1+ source, build it and copy 'makeblastdb' binaries into " + maindir + "/blast/")
            if checker(md5[8], mnb[8]):
                print("<bwt>       ---------: Passed")
            else:
                print("<bwt>       ---------: Failed")
                sys.exit("hsblast index failed, please re-configure and re-compile NanoVar")
            if checker(md5[10], mnb[10]):
                print("<sa>        ---------: Passed")
            else:
                print("<sa>        ---------: Failed")
                sys.exit("hsblast index failed, please re-configure and re-compile NanoVar")
            if checker(md5[11], mnb[11]):
                print("<sequence>  ---------: Passed")
            else:
                print("<sequence>  ---------: Failed")
                sys.exit("hsblast index failed, please re-configure and re-compile NanoVar")
            if checker(md5[12], mnb[12]):
                print("<counts>    ---------: Passed")
            else:
                print("<counts>    ---------: Failed")
                sys.exit("windowmasker failed, please download Blast v2.7.1+ source, build it and copy 'windowmasker' binaries into " + maindir + "/blast/")
            if checker(md5[13], mnb[13]):
                print("<obinary>   ---------: Passed")
            else:
                print("<obinary>   ---------: Failed")
                sys.exit("windowmasker failed, please download Blast v2.7.1+ source, build it and copy 'windowmasker' binaries into " + maindir + "/blast/")
            if checker(md5[14], mnb[14]):
                print("<align>     ---------: Passed")
            else:
                print("<align>     ---------: Failed")
                sys.exit("hsblast align failed, please re-configure and re-compile NanoVar")
            if checker(md5[15], mnb[15]):
                print("<parse>     ---------: Passed")
            else:
                print("<parse>     ---------: Failed")
                sys.exit("bedtools sort failed, please ensure bedtools version >= 2.26.0 and functional")
            if checker(md5[16], mnb[16]):
                print("<overlap>   ---------: Passed")
            else:
                print("<overlap>   ---------: Failed")
                sys.exit("bedtools intersect or awk failed, please ensure bedtools version >= 2.26.0 and awk are functional")
            if checker(md5[17], mnb[17]):
                print("<ANN>       ---------: Passed")
            else:
                print("<ANN>       ---------: Failed")
                sys.exit("python3 failed, please ensure python3 is in PATH and functional")
            if checker(md5[18], mnb[18]):
                print("<ANN0>      ---------: Passed")
            else:
                print("<ANN0>      ---------: Failed")
                sys.exit("awk failed, please ensure awk is functional")
            if checker(md5[19], mnb[19]):
                print("<cov>       ---------: Passed")
            else:
                print("<cov>       ---------: Failed")
                sys.exit("awk or sort failed, please ensure awk and sort are functional")
            if checker(md5[20], mnb[20]):
                print("<t-vcf>     ---------: Passed")
            else:
                print("<t-vcf>     ---------: Failed")
                sys.exit("bedtools sort failed, please ensure bedtools is functional")
            if checker(md5[21], mnb[21]):
                print("<filt-vcf>  ---------: Passed")
            else:
                print("<filt-vcf>  ---------: Failed")
                sys.exit("bedtools sort or awk failed, please ensure bedtools and awk are functional")
            if checker(md5[22], mnb[22]):
                print("<svoverlap> ---------: Passed")
            else:
                print("<svoverlap> ---------: Failed")
                sys.exit("awk or sed failed, please ensure awk and sed are functional")
            os.system('echo "AllPassed" > ' + maindir + '/test/AllPassed')

if __name__ == "__main__":
    main()

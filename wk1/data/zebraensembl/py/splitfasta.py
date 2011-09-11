#fastasplit.py
#Author: Jaimie Imrie, University of Victoria, British Columbia,
#imrie@csc.uvic.ca
#A simple FASTA file splitter. Tested to work on S. cerevisiae ORFs from
#www.yeastgenome.com. Should work on any standard FASTA format where the 
#ORF is the first attribute after the '>'. Will output a file with the name
#of the ORF in FASTA format with the fasta file type. ie. YAL001C.fasta

import os
import re

#Regular expression that finds the FASTA format for an ORF and creates two
#groups: ORF for ORF name, and Annoation for the annotation information
fasta_pattern = re.compile(r"^>(?P<ORF>(\w+))\s+(?P<Annotation>(.)*\n)")
#Get input path, output path
input_path = str(raw_input("Input Directory: "))
output_path = str(raw_input("Output Directory (press enter to use input directory): "))

#if output path was blank use input path as output path
if output_path == '':
    print "Using input directory as output directory"
    output_path=input_path

#get input file
in_file=raw_input("FASTA file to split into individual fasta files for each ORF:")

#Test that all paths and input file exist
if not os.path.exists(input_path):
    print "Input directory does not exist"
    exit(1)
if not os.path.exists(input_path+in_file):
    print "File does not exist"
    exit(1)
if not os.path.exists(output_path):
    print "Output directory does not exist. Make it first"
    exit(1)

#open the fasta file to split
fasta_file_to_split = open(input_path+in_file, "r")
#some helper variables
curr_file = 0
match_count = 0

#try and match each line to the regular expression, if a match
#create a new file ORF.fasta for the current ORF. Add each
#line subsequent to the match to the new file.
for line in fasta_file_to_split:
    new_sequence_match = fasta_pattern.search(line)
    if new_sequence_match:
        match_count+=1
        print "Creating: ", new_sequence_match.group('ORF')+".fasta"
        #if we have opened a file make sure we close it before opening a new one
        if curr_file is not 0:
            try:
                curr_file.close()
            except OSError:
                print "Error closing", curr_file.name
        #try and create a new file for the current ORF
        try:
            curr_file = open(output_path+new_sequence_match.group('ORF')+".fasta", "w")
        except OSError:
            print "Error opening", output_path+new_sequence_match.group('ORF')+".fasta"
            exit(1)
    try:
        curr_file.write(line)
    except OSError:
        print "Error writing to", curr_file.name
        exit(1)
curr_file.close()
print match_count, "ORFs successfully split into individual files"
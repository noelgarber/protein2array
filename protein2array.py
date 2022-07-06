#This script generates a CSV containing peptide sequences derived from a protein sequence of interest. 

import numpy as np
import pandas as pd
import math
import os

print("Protein2Array")
print("------------------")
print("This script generates overlapping peptide sequences for array synthesis from a user-inputted protein sequence.")
print("------------------")

print("Please place your protein's sequence in a text file on a single line with no other characters.")
sequence_filename = input("Input the filename:  ")

with open(sequence_filename, "r") as file: 
	sequence = file.read().rstrip()

def input_int(prompt):
    input_value = False
    while not isinstance(input_value, int) or not input_value:
        try:
            input_value = int(input(prompt))
        except ValueError:
            print("That was not an integer. Please try again!")
    return input_value

frame_size = input_int("Enter the output peptide length:  ")
overlap_size = input_int("Enter the number of residues to overlap by:  ")

peptide_dict = {}

end_reached = False
start_position = 0
while not end_reached: 
	remaining_sequence = sequence[start_position:]
	remaining_length = len(remaining_sequence)
	if remaining_length >= frame_size: 
		pep_seq = sequence[start_position : start_position + frame_size]
		pep_name = sequence_filename[:-4] + "_" + str(start_position) + "_" + str(start_position + frame_size)
		#print("pep_name =", pep_name, "and pep_seq =", pep_seq)
		peptide_dict[pep_name] = pep_seq
		start_position += overlap_size
	elif remaining_length >= 1: 
		pep_seq = sequence[(-1 * frame_size) :]
		pep_name = sequence_filename[:-4] + "_" + str(len(sequence) - frame_size) + "_" + str(len(sequence))
		#print("pep_name =", pep_name, "and pep_seq =", pep_seq)
		peptide_dict[pep_name] = pep_seq
		end_reached = True
	else: 
		end_reached = True

dataframe = pd.Series(peptide_dict, name = "Peptide_Sequence")
dataframe.index.name = "Peptide"
output_filename = sequence_filename[:-4] + "_array_peptides.csv"
dataframe.to_csv(output_filename)

current_directory = os.getcwd()
output_path = os.path.join(current_directory, output_filename)

print("Success! Results path: ", output_path)
#This script generates a CSV containing peptide sequences derived from a protein sequence of interest. 

import numpy as np
import pandas as pd
import math

print("Please place your protein's sequence in a text file on a single line with no other characters. Must be in the same directory as this script.")
sequence_filename = input("Input the filename:  ")

with open(sequence_filename, "r") as file: 
	sequence = file.read().rstrip()

def InputInt(prompt): 
	value = ""
	while value is not int: 
		value = input(prompt + "  ")
		try: 
			value = int(value)
			return value
		except:
			print("That was not an integer! Please try again.")

frame_size = InputInt("Enter the output peptide length:")
overlap_size = InputInt("Enter the number of residues to overlap by:")

peptide_dict = {}

end_reached = "No"
start_position = 0
while end_reached != "Yes": 
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
		end_reached = "Yes"
	else: 
		end_reached = "Yes"

dataframe = pd.Series(peptide_dict, name = "Peptide_Sequence")
dataframe.index.name = "Peptide"
dataframe.to_csv(sequence_filename[:-4] + "_array_peptides.csv")
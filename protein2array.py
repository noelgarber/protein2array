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

peptide_list = []

end_reached = "No"
start_position = 0
while end_reached != "Yes": 
	remaining_sequence = sequence[start_position:]
	remaining_length = len(remaining_sequence)
	if remaining_length >= frame_size: 
		pep_seq = sequence[start_position : start_position + frame_size]
		print(pep_seq)
		peptide_list.append(pep_seq)
		start_position += overlap_size
	elif remaining_length >= 1: 
		pep_seq = sequence[(-1 * frame_size) :]
		print(pep_seq)
		peptide_list.append(pep_seq)
		end_reached = "Yes"
	else: 
		end_reached = "Yes"

dataframe = pd.DataFrame(peptide_list, columns = ["Peptide_Sequence"])
dataframe.to_csv(sequence_filename[:-4] + "_array_peptides.csv")
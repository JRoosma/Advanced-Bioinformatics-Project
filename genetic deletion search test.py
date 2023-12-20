# Jordan Roosma
# Ramapo College of New Jersey - Advanced Bioinformatics Capstone Project
# Initial Date: 2/1/2023
# Update Date: 12/20/2023

# Y Chromosome Genetic Sequence Deletion Analysis Program

# Import necessary modules
import pysam

# Ask the user for the BAM file and genetic sequence
bam_file = input("Enter the path to the BAM file: ")
#sequence = input("Enter the genetic sequence to search for: ")

# Open the BAM file using PySam / Samtools
bam = pysam.AlignmentFile(bam_file, "rb")

# Check bam file header / contents
header = bam.header
print(f"BAM file header: {header}")

# Index to the Y chromosome since this is the chromosome we need to search for the genetic deletion / abnormality
y_chromosome = bam.get_reference_name(23)
print(f"Y-chromosome: {y_chromosome}")

"""In this script, pysam.AlignmentFile automatically detects and uses the .bai file if it's located in the same 
directory as the BAM file and has the same name (except for the extension). This allows efficient querying and 
retrieval of reads from the BAM file."""
# For example, iterating through the first few reads:
for read in bam.fetch(until_eof=True):
    print(read)
    # Break after printing a few reads to avoid too much output
    break

"""
# Loop through each read in the BAM file
for read in y_chromosome:
    
    # Get the read sequence
    read_seq = read.query_sequence

    # Search for the genetic sequence within the read sequence
    if sequence in read_seq:
        
        # Print the read ID and position where the sequence was found
        print(f"{read.query_name}: {read.reference_name}:{read.reference_start}")
"""

# Close the BAM file
bam.close()

"""
#########################################################
# Alternative methods for searching for sequence deletion 
#########################################################

# Original 100 base pair genetic sequence
seq = "CTAGTCGATCGAGCTAGCTCGAGCTAGCTAGCTCGAGCTAGCTAGCTCGAGCTAGCTCGAGCTAGCTCGAGCTAGCTCGAGCTAGCTCGAGCTAGCTCGA"

# base pair deletion sequence
del_seq = "AGCTCGAGCTAGCTAGCTCGAGCTAGCTCGAGCTAGCTCG"

# Find the index where the deletion starts in the original sequence
del_start_idx = seq.index(del_seq)

# Extract the sequence before the deletion
pre_del_seq = seq[:del_start_idx]

# Extract the sequence after the deletion
post_del_seq = seq[del_start_idx + len(del_seq):]

# Concatenate the pre- and post-deletion sequences to get the remaining sequence
remaining_seq = pre_del_seq + post_del_seq

# Print the remaining sequence
print(remaining_seq)


#########################################################
# Alternative methods for searching for sequence deletion 
#########################################################

# define the original sequence
original_seq = "ATCGGCTAGGACCGTATA"

# define the mutated sequence with a deletion
mutated_seq = "ATCGGCTAGGACGTATA"

# compare the two sequences
for i in range(len(original_seq)):
    if original_seq[i] != mutated_seq[i]:
        if original_seq[i+1:] == mutated_seq[i:]:
            print("Deletion detected at position", i)
            break


#########################################################
# Manual function for detecting a sequence deletion 
#########################################################

def detect_deletion(sequence, deletion_start, deletion_end):
REMEMBER TO ADD TRIPLE QOUTES HERE!!!        
    Detects a deletion in a genetic sequence.

    Parameters:
    sequence (str): The genetic sequence to search for deletions.
    deletion_start (int): The starting index of the deletion.
    deletion_end (int): The ending index of the deletion.

    Returns:
    str: A message indicating whether a deletion was detected.
REMEMBER TO ADD TRIPLE QUOTES HERE!!!    

    # Check if the deletion overlaps with the ends of the sequence
    if deletion_start < 0 or deletion_end >= len(sequence):
        return "Deletion overlaps with the ends of the sequence."

    # Check if the deletion has a valid length
    deletion_length = deletion_end - deletion_start + 1
    if deletion_length <= 0:
        return "Deletion length must be greater than 0."

    # Check if the deletion is in the middle of the sequence
    left_flanking = sequence[deletion_start - 1] if deletion_start > 0 else None
    right_flanking = sequence[deletion_end + 1] if deletion_end < len(sequence) - 1 else None
    if left_flanking is not None and right_flanking is not None and left_flanking == right_flanking:
        return "Deletion is in the middle of the sequence."

    # If none of the checks triggered a return statement, then no deletion was detected
    return "No deletion detected."

# Example usage
sequence = "ATCGATCGTAGCTACG"
deletion_start = 6
deletion_end = 9
result = detect_deletion(sequence, deletion_start, deletion_end)
print(result) # Output: Deletion is in the middle of the sequence.

"""

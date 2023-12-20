# Jordan Roosma
# Ramapo College of New Jersey - Advanced Bioinformatics Capstone Project
# Initial Date: 2/1/2023
# Update Date: 12/20/2023

# GUI for "Y Chromosome Genetic Sequence Deletion Analysis Program"

# Import necessary modules
import tkinter as tk
from tkinter import filedialog
import pysam

# Create a class for the GUI
class FileUploaderGUI:
    
    def __init__(self, master):
        self.master = master
        master.title("Y Chromosome Genetic Anomaly Detector")

        self.label = tk.Label(master, text="Choose a BAM/SAM and BAI file to upload:",
                              foreground="white",
                              background="black",)
        self.label.pack()

        self.upload_button = tk.Button(master, text="Upload",
                                       foreground="white",
                                       background="purple",
                                       relief="raised",
                                       command=self.upload_file)
        self.upload_button.pack()

        self.filename_label = tk.Label(master, text="")
        self.filename_label.pack()

    def upload_file(self):

        filetypes = [("BAM/SAM files", "*.bam *.sam")]
        filename = filedialog.askopenfilename(title="Select a file to upload",
                                              filetypes=filetypes)
        self.filename_label.config(text=filename)


window = tk.Tk()
width= window.winfo_screenwidth()
height= window.winfo_screenheight()
window.geometry("%dx%d" % (width, height))
uploader = FileUploaderGUI(window)
window.mainloop()

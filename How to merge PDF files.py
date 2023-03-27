#1: Install PyPDF2
#2: Copy the file in WD

import os
from PyPDF2 import PdfFileMerger
source_dir = os.getcwd()
merger = PdfFileMerger()
for item in os.listdir(source_dir):
    if item.endswith('pdf'):
        merger.append(item)
merger.write ("C:/Users/ariad/PycharmProjects/pythonProject/Merged.pdf")
merger.close()

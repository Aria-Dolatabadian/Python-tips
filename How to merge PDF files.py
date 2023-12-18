#1: Install PyPDF2
#2: Copy the file in WD

import os
from PyPDF2 import PdfMerger
source_dir = os.getcwd()
merger = PdfMerger()
for item in os.listdir(source_dir):
    if item.endswith('pdf'):
        merger.append(item)
merger.write ("C:/Users/ariad/PycharmProjects/pythonProject/Merged.pdf")
merger.close()

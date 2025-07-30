import PyPDF2
import os
import time

# with open("pdf-files/Taupe-Notch-SRS(Khadija).pdf","rb") as file:
#     reader = PyPDF2.PdfReader(file)
#     #print(reader)
#     for page in reader.pages:
#         print(page)

merge = PyPDF2.PdfMerger()
file_names = ["pdf-files/Taupe-Notch-SRS(Khadija).pdf","pdf-files/Menu Idea (1).pdf"]
for file_name in file_names:
    merge.append(file_name)

merge.write("pdf-files/comabine.pdf")
merge.close()
os.startfile("pdf-files/comabine.pdf")

# a = PyPDF2.PdfReader('pdf-files/Taupe-Notch-SRS(Khadija).pdf')
# print(a.metadata) 
# print(len(a.pages))
# print(a.pages[10].extract_text())

# string1 = ""
# for i in range(1,10):
#     all_text = a.pages[i].extract_text()
#     string = string1 + all_text

# with open("text-files/toupe_notch.txt","w",encoding="utf-8") as file:
#     file.write(string)

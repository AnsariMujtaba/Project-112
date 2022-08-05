import os
import shutil

from_dir="C:/Users/ma185080/Downloads"
to_dir="C:/Users/ma185080/OneDrive - NCR Corporation/Desktop/Documents_Files"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for file in list_of_files:
    root,ext=os.path.splitext(file)
    
    if ext =="":
        continue
    if ext in [".txt",".doc",".docx",".pdf"]:
        path1=from_dir+"/"+file
        path2=to_dir+"/"+"pdf_files"
        path3=to_dir+"/"+"pdf_files"+"/"+file

        if os.path.exists(path2):
            print("moving"+file+"....")

            shutil.move(path1,path3)
        else:
            os.mkdir(path2)
            print("Moving"+file+"....")

            shutil.move(path1,path3)
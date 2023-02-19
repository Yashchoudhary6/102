import os 
import shutil
from_directory="C:/Users/DELL LAPTOP/Desktop"
to_directory="C:/do not open"
listofffiles=os.listdir(from_directory)
#    print(listofffiles)
for file_name in listofffiles:
    name,extension=os.path.splitext(file_name)
   # print(name)
    #print(extension)
    if extension=="":
        continue
    if extension in [".txt",".doc",".docx",".pdf"]:
        path1=from_directory+"/"+file_name
        path2=to_directory+"/"+"images_files"
        path3=to_directory+"/"+"images_files"+"/"+file_name   
      #  print(path1)
       # print(path3)
        if os.path.exists(path2):
            print("moving"+file_name)
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("moving"+file_name)
            shutil.move(path1,path3)  
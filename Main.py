import os
import shutil

from_dir = "Images"
to_dir = "Images2"

listoffiles = os.listdir(from_dir)
for filename in listoffiles:
    name,extension = os.path.splitext(filename)
    if extension=='':
        continue
    if extension in ['.gif','.png','.jpg','.jpeg','.jfif']:
        path1=from_dir+'/'+filename
        path2=to_dir+'/'+"image_files"
        path3=to_dir+'/'+"image_files"+'/'+filename
        if os.path.exists(path2):
            shutil.move(path1,path3)
        else: 
            os.mkdir(path2) 
            shutil.move(path1,path3)
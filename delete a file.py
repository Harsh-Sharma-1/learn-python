import os
import shutil

path = './assets/delete.txt'

try:
    os.remove(path)
    print(path,'got deleted')
except FileNotFoundError:
    print('File was not found')
else:
    print(path,'got deleted')
    

folder_path = './assets/delete'

try:
    #os.remove(folder_path) # to delete a file
    #os.rmdir(folder_path) # to delete a empty folder
    shutil.rmtree(folder_path) # to delete a folder which contains a file
except FileNotFoundError:
    print("This file was not found")
except PermissionError:
    print("You do not have permission to delete that")
except OSError:
    print("You cannot delete that using that function")
else:
    print(folder_path,"was deleted")
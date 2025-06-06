import os 
import time
import shutil
from dotenv import load_dotenv


load_dotenv()
principal_folder = os.getenv('PRINCIPAL_FOLDER')


def check_labcorp_folder(folder_path):
  
  list_of_folders = os.getenv('LIST_OF_FOLDERS')
  
  for folder in list_of_folders.split(','):      
    print(folder)
    
       
  #List all files and directories in the current directory
    check_path = os.path.join(folder_path, folder, 'IN')
    path_to_move = os.path.join(check_path, 'ERROR')
    items = os.listdir(check_path)    
    # Print the items
    print("Items in the current directory:")
    files_to_move = []
    for item in items:
      if os.path.isfile(os.path.join(check_path, item)):
        print(f"File: {item}")
        creation_time = os.path.getctime(os.path.join(check_path, item))     
        now = time.time()
        time_difference = now - creation_time 
        if time_difference >=  7200:
          files_to_move.append(item)
          #shutil.move(os.path.join(check_path, item), os.path.join(path_to_move, item))
        else:
          continue
    if len(files_to_move) > 0:       
      n = 1
      msg =''
      for file in files_to_move:
          msg += f"{n}. {file}\n"
          n += 1
      print(msg)
    
        # legible_time = time.ctime(time_difference)
        # print(f"Creation time: {legible_time}")
        
      
      
        
        
print(check_labcorp_folder(principal_folder))
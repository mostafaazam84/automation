import os
import shutil

current_dir = os.path.dirname(os.path.realpath(__file__))
for filename in os.listdir(current_dir):
    
    
    if filename.endswith((".jpg",".png")):
        if not os.path.exists("Models"):
            os.mkdir('Models')
        shutil.copy(filename,"Models")
        os.remove(filename)
        print ("Images Done")
        
        
    if filename.endswith((".pdf",".word", ".txt")):
        if not os.path.exists("Models"):
            os.mkdir('Models')
        shutil.copy(filename,"Models")
        os.remove(filename)
        print ("Document Done")
        
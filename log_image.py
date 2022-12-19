import os
from PIL import Image

## Logo .new folder
LOGO_NAME = input("Enter The Logo Name With Extension : ")
NEW_FOLDER_NAME = input("Enter The Folder Name : ")

logo_image = Image.open(LOGO_NAME)
logo_width , logo_height = logo_image.size

## create folder 
if not os.path.exists(NEW_FOLDER_NAME):
   os.mkdir(NEW_FOLDER_NAME)


## loop over images 
for filename in os.listdir('.'):
    ## check in file image & not logo
    if not(filename.endswith('.png') or filename.endswith('.jpg') or filename == LOGO_NAME):
        continue
    
    img = Image.open(filename)
    width,height = img.size
    
    #add log to the image 
    img.paste(logo_image ,(width-logo_width , height-logo_height))
    
    ## save image
    img.save(os.path.join(NEW_FOLDER_NAME,filename))
    print (f'done image :{filename}')
    
print("Done")    
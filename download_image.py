import urllib.request

 
def image(url,file_path,file_name):
    full_path = file_path + file_name + ".PNG"
    urllib.request.urlretrieve(url, full_path)
    if full_path == image:
        print("done")
url =input("Enter Image URL To Download : ")
file_name = input("Enter image Name To Save as : ")
file_path = input("Enter Location Folder : : ")


    
image(url,file_path ,file_name)
    
    
    download_image , numbersWords , text_colors
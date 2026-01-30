import os

# path= "C:/Users/tniha/OneDrive/Desktop/Capg training/Primary Track/Codes VS/DAY4/3logfile_extract.py"

# new_path= "C:/Users/tniha/OneDrive/Desktop/Capg training/Primary Track/Codes VS/DAY4/logfile_extract.py"

# os.rename(path,new_path)

path =r"C:\Users\tniha\OneDrive\Desktop\Capg training\Primary Track\pictures"

for count, file in enumerate(os.listdir(path) ,start= 1):
    old_path=os.path.join(path,file)
    new_path=os.path.join(path,f"file_{count}.jpg")
    os.rename(old_path,new_path)

print("File renamed successfully!!")

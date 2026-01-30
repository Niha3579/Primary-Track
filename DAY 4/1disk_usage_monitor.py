import shutil

total, used, free= shutil.disk_usage("D:/")

print(f"Total Disk Space: {total//(1024**3)} GB")
print(f"Used Disk Space: {used//(1024**3)} GB")
print(f"Free Disk Space: {free//(1024**3)} GB")

# 1. disk usage monitoring script total, used, free  
# 2. automatic file backup script  
# 3. log file error extractor 
# 4. system usage monitor
# 5. folder cleanup automation : remove temp files of disk, %temp% remove files in this
# 6. csv report generator 
# 7. password strength checker
# 8. ping multiple script
# 9. file renamer script
# 10. file manager: pdfs, words, images folder
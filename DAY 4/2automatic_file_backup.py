import shutil
import datetime

source="C:/Users/tniha/OneDrive/Desktop/Capg training/Primary Track/Codes VS/DAY4/data.txt"
backup=f"C:/Users/tniha/OneDrive/Desktop/Capg training/Primary Track/Codes VS/DAY4/data_backup_txt_{datetime.date.today()}.txt"

shutil.copy(source, backup)
print(f"Backup of {source} created ay {backup}")
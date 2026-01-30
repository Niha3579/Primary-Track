with open("sample_logs.log","r") as log:
    lines=log.readlines()

for line in lines:
    if "ERROR" in line:
        with open("error_extract.txt","w") as file:
            file.write(line)
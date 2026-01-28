import sys

# var=sys.argv[1]
# print(var)


#to run type in terminal: python3 sys.py niha aiere sam
print("Prog Name: ", sys.argv[0])
for i in range(1, len(sys.argv)):
    print(f"arg {i}:", sys.argv[i])
import re

# text="python is powerful"
# result=re.match("python",text)
# if result:
#     print("Math found", result.group())

# result=re.search("powerful",text)
# if result:
#     print("Math found", result.group())


# text="my number is 1234567890 and 9876543210"
# number=re.findall("\d{10}",text) 
# print(number)

# for match in re.finditer("\d{10}",text):
#     print("Match found at index:", match.start(), "to", match.end())


text="my phone number is 1234567891"
masked=re.sub('\\d{6}','******',text)
print(masked)

# log file analyser
# emailid, pw validator with re, 8 characters, 1upper, 1lower, number, special char
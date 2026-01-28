# build bill calculator, showing client information : name, place, bill1,bill2, 
# phone number masked, city , restaurant, total bill value of all the bills




def add(*args):
    sum=0
    for num in args:
        sum+=num
    return sum


def display(**kwargs):
    ls=[]
    for key,value in kwargs.items():
       ls.append(f"{key} : {value}")
    return ls


name=input("Enter Name:")
phnum=input("Enter Phone Number:")
city=input("Enter City:")
restaurant=input("Enter Restaurant:")

bill1=int(input("Enter bill 1:"))
bill2=int(input("Enter bill 2:"))
bill3=int(input("Enter bill 3:"))

# arr=[]
# for i in range(10):
#     item = input(f"Enter Bill amount {i}: ")
#     arr.append(item)


maskedphnum=phnum[:2]+"******"+phnum[-2:]
totalbill=add(bill1,bill2,bill3)
# totalbill=add(arr)

print("\n")
list=display(Name=name.title().strip(), PhoneNumber=maskedphnum, City=city.title().strip(), Restaurant=restaurant.title().strip(), TotalBill=totalbill)

for i in list:
    print(i)

print("Welcome to Zomato!")

try:
    number_of_items = int(input("Enter number of items: "))

    if number_of_items == 0:
        raise ZeroDivisionError

    total_price = number_of_items * 200
    average_price = total_price / number_of_items

except ValueError:
    print(" Invalid input! Please enter numbers only.")

except ZeroDivisionError:
    print("Number of items cannot be zero.")

else:
    print("Total price:", total_price)
    print("Average price per item:", average_price)

finally:
    print("Thank you for ordering with Zomato!")
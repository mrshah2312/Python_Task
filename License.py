# Apply For The License
# Using if-else statement

req_age = 16
age = int(input("Enter Your Age : "))

if age >= req_age:
    print("Congratulations ! You Can Apply For The License")
else:
    print(f"Sorry You Can't Apply For The License, Please Come After {req_age-age} Years")
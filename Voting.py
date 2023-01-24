req_age = 18
y = ['yes']
n = ['no']

age = int(input("Enter Your Age : "))

if age>=req_age:

    ic = str(input("You have indian citizenship? yes/no : "))
    if ic in y :
        print("Congratulations ! You Can Eligible For Voting.")
    else:
        print("Sorry You Are Not Eligible For The Voting.")
else:
    print(f"You Are Not Eligible For Voting, Please Come After {req_age-age} Years")
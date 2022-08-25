#PNC means Prime Number Checker
PNC = int(input('Is it a prime number? Enter to see: '))

if PNC > 1:
    for i in range(2, PNC):
        if (PNC % i) == 0:
            print(PNC, "is not a prime number")
            break
    else:
        print(PNC, "is a prime number")

# if the entered number is less than or equal to 1
# then it is not prime number
else:
    print(PNC, "is not a prime number")

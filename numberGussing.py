import random 

missing_random_number = random.randint(1,100)

while True :
 try:
    gues =int( input("Enter a numbe 1 to 100 "))

    if gues < missing_random_number:
        print("To Low ...")
    elif gues > missing_random_number:
        print("To High")
    else :
        print("Your guess is correct" f"{gues}")
        break

 except ValueError:
    print("Invailed number")
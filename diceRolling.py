import random

while True :
    choose = input("Roll the dies ? (y / n) : ").lower()
    match choose :
        case "y" :
            dies1 = random.randint(1,6)
            dies2 = random.randint(1,6)
            print(f"({dies1},{dies2})")
        case "n" :
         print("Thank you for playing")

        case _:
         print("Invalid choose")




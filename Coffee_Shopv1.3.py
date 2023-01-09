#Let's start a coffee shop together!! We're going to build a coffee shop using some new Python programming concepts!!

#Let's build robot Barista!!

print("Hello, welcome to NetworkChuck Coffee!!!!!!!!!")

name = input("What is you name?\n")

if name == "Ben" or name == "Patricia" or name == "Loki":
    evil_status = input("are you evil?\n")
    good_deeds = int(input("How many good deeds have you done today?\n"))
    if evil_status == "yes" and good_deeds < 4:
        print("You're not welcome here Evil " + name + "!! Get out !!")
        exit()
    else:
        print("Oh, so you're one of those good " + name + "'s. Come on in!!")
else:
    print("Hello " + name + ", thank you so much for coming in today!!\n\n\n")

#menu/ order

menu = "Black Coffee, Espresso, Latte, Cappucino, Frappuccino"

print(name + ", What would you like from our menu today? Here is what we are serving\n" + menu)

order = input()

#money
if order == "Frappuccino":
    price = 13
elif order == "Black Coffee":
    price = 3
elif order == "Espresso":
    price = 4
elif order == "Latte":
    whip = input("Do you Want extra Whip Cream?\n")
    if whip == "yes":
        price = 11
    else:
        price = 9
elif order == "Cappucino":
    price = 10
else:
    print("Sorry, we don't have that here.")
    exit()

quantity = input("\n\n\nhow many coffees would you like?\n")

total = price * int(quantity)

print("Thank you. Your total is: " + "$" + str(total))

print("\n\n\n" + "Sounds good " + name + ", we'll have your " + quantity + " " + order + " ready for you in a moment.\n\n\n")

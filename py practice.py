name = input("What is your name? ")
age = int(input("How old are you? "))
if age < 18:
    print("Hello {name} you're a minor.")
elif age < 65:
    print("Hello + {name} you're an adult.")
else:
    print("hello you're a senior.")
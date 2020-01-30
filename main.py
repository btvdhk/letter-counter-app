print("Welcome to the letter counter app")

name = input("What is your name? ")
greet = ("hello")
print(f'{greet.title()} {name.title()}!')

msg = input("Please enter a message: ")
letter = input("which letter you want to count? ")

letter = letter
count = msg.count(letter)


print(f"{greet.title()} {name.title()}! Your message has {count} {letter}'s in it!")
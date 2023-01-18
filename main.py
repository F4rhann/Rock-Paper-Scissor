name = input("Set your name for this game: ")
print(""""Important Instructions:
Rock, Paper, Scissors Game!

Note: Rock beats scissor, paper beats rock and scissor beats paper.

1) Enter 'r' for rock, 'p' for paper and 's' for scissor.
2) There will be a total of 5 rounds and you get a point for each round you win. No point changes for a draw or loss.
3) Results will be shown at the last and the player with the highest points wins!

Enjoy the game!""")

import random
username = str(name)

user_points = 0
computer_points = 0
rounds = 1

while rounds <= 5:
    commands = ['r', 'p', 's']
    computer_input = random.choice(commands)
    dicti = {"r" : "Rock",
    "p" : "Paper", 
    "s" : "Scissor"}

    user_input =  input(f"Round {rounds}: ")
    rounds+=1

    # For rock
    if user_input.lower() == "r" and computer_input == 'r':
        print(f"Draw\nUser: {user_input} ({dicti.get(user_input)}), Computer: {computer_input} ({dicti.get(computer_input)})")
    elif user_input.lower() == 'r' and computer_input == 's':
        print(f"You won!\nUser: {user_input} ({dicti.get(user_input)}), Computer: {computer_input} ({dicti.get(computer_input)})")
        user_points+=1
    elif user_input.lower() == 'r' and computer_input == 'p':
        print(f"You lost\nUser: {user_input} ({dicti.get(user_input)}), Computer: {computer_input} ({dicti.get(computer_input)})")
        computer_points+=1

    # For paper
    if user_input.lower() == 'p' and computer_input == 'p':
        print(f"Draw\nUser: {user_input} ({dicti.get(user_input)}), Computer: {computer_input} ({dicti.get(computer_input)})")
    elif user_input.lower() == 'p' and computer_input == 'r':
        print(f"You won!\nUser: {user_input} ({dicti.get(user_input)}), Computer: {computer_input} ({dicti.get(computer_input)})")
        user_points+=1
    elif user_input.lower() == 'p' and computer_input == 's':
        print(f"You lost\nUser: {user_input} ({dicti.get(user_input)}), Computer: {computer_input} ({dicti.get(computer_input)})")
        computer_points+=1

    # For scissor
    if user_input.lower() == 's' and computer_input == 's':
        print(f"Draw\nUser: {user_input} ({dicti.get(user_input)}), Computer: {computer_input} ({dicti.get(computer_input)})")
    elif user_input.lower() == 's' and computer_input == 'p':
        print(f"You won!\nUser: {user_input} ({dicti.get(user_input)}), Computer: {computer_input} ({dicti.get(computer_input)})")
        user_points+=1
    elif user_input.lower() == 's' and computer_input == 'r':
        print(f"You lost\nUser: {user_input} ({dicti.get(user_input)}), Computer: {computer_input} ({dicti.get(computer_input)})")
        computer_points+=1

    if user_input != "r" and user_input != "p" and user_input != 's':
        print("Invalid Input. Please type 'r' or 'p' or 's'")
        rounds-=1

if user_points > computer_points:
    print(f"""\nPoints Distribution - 
    {username}: {user_points} points
    Computer: {computer_points} points
    
    {username} is the winner!\n""")
elif computer_points > user_points:
    print(f"""\nPoints Distribution - 
    {username}: {user_points} points
    Computer: {computer_points} points
    
    Computer is the winner!\n""")

elif computer_points == user_points:
    print(f"""\nPoints Distribution - 
    {username}: {user_points} points
    Computer: {computer_points} points
    
    The game is a draw!\n""")
import random
import tkinter as tk

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]


def play_game(user_choice):
    computer_choice = random.randint(0, 2)
    user_choice_text.set(game_images[user_choice])
    computer_choice_text.set(game_images[computer_choice])

    if user_choice == computer_choice:
        result_text.set("It's a draw")
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        result_text.set("You win!")
    else:
        result_text.set("You lose")

root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("500x500")

user_choice_text = tk.StringVar()
computer_choice_text = tk.StringVar()
result_text = tk.StringVar()

user_choice_label = tk.Label(root, text="What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
user_choice_label.pack()

user_choice_entry = tk.Entry(root)
user_choice_entry.pack()

play_button = tk.Button(root, text="Play", command=lambda: play_game(int(user_choice_entry.get())))
play_button.pack()

result_label = tk.Label(root, textvariable=result_text)
result_label.pack()

user_choice_display = tk.Label(root, textvariable=user_choice_text)
user_choice_display.pack()

computer_choice_display = tk.Label(root, textvariable=computer_choice_text)
computer_choice_display.pack()

root.mainloop()

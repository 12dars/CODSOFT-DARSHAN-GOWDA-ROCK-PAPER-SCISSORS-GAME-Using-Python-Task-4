# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 12:07:54 2023

@author: darshan
"""

import random

options = ("rock", "paper", "scissors")
running = True

while running:

    Darshan = None
    computer = random.choice(options)

    while Darshan not in options:
        Darshan = input("Enter a choice (rock, paper, scissors): ")

    print(f"Darshan: {Darshan}")
    print(f"Computer: {computer}")

    if Darshan == computer:
        print("It's a tie!")
    elif Darshan == "rock" and computer == "scissors":
        print("Darshan wins and rock beats scissors")
    elif Darshan == "paper" and computer == "rock":
        print("Darshan wins and paper beats rock")
    elif Darshan == "scissors" and computer == "paper":
        print("Darshan wins and scissors beats paper")
    else:
        print("Darshan lose")

    if not input("Play again? (yes/no): ").lower() == "yes":
        running = False

print("Thankyou for playing this game")
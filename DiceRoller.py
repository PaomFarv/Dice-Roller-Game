import random
from colorama import Fore
import time
#● ┌ ─ ┐ │ └ ┘

dice_faces = {
    1: (Fore.BLUE+"┌─────────────┐",
        "│             │",
        "│             │",
        "│      ●      │",
        "│             │",
        "│             │",
        "└─────────────┘"),
    2: (Fore.BLUE+"┌─────────────┐",
        "│             │",
        "│   ●         │",
        "│             │",
        "│         ●   │",
        "│             │",
        "└─────────────┘"),
    3: (Fore.BLUE+"┌─────────────┐",
        "│             │",
        "│   ●         │",
        "│      ●      │",
        "│         ●   │",
        "│             │",
        "└─────────────┘"),
    4: (Fore.BLUE+"┌─────────────┐",
        "│             │",
        "│   ●     ●   │",
        "│             │",
        "│   ●     ●   │",
        "│             │",
        "└─────────────┘"),
    5: (Fore.BLUE+"┌─────────────┐",
        "│   ●     ●   │",
        "│             │",
        "│      ●      │",
        "│             │",
        "│   ●     ●   │",
        "└─────────────┘"),
    6: (Fore.BLUE+"┌─────────────┐",
        "│   ●     ●   │",
        "│             │",
        "│   ●     ●   │",
        "│             │",
        "│   ●     ●   │",
        "└─────────────┘")
}
print("-"*150)
while True:
    num_of_dice = input(Fore.YELLOW + "Number of dice to roll (max 09): ")
    if num_of_dice.isdigit():
        num_of_dice = int(num_of_dice)
        break
    else:
        print("Input must be a valid Number.")
        continue

total_points = 0
dice_rolls = []

for char in range(num_of_dice):
    dice_rolls.append(random.randint(1,6))

total_points = sum(dice_rolls)
for line in range(7):
    for num in dice_rolls:
        print(dice_faces.get(num)[line], end=" "*3)
        time.sleep(0.01)
    print()

print("\nCalculating----")
time.sleep(1.5)
print(Fore.GREEN + f"Total Points = {total_points}")

print(Fore.WHITE + "-"*150)
play_again = input("Press ENTER to roll again ('Q' to quit).---")

if play_again.lower() == 'q':
    print("Thanks for playing! Goodbye.")
    time.sleep(1)
    exit()
else:
    print("\n"*5)
    import DiceRoller

# Dice Roller Game

A fun Python-based dice roller simulation that lets you roll multiple dice and see the results in an ASCII art format. The game calculates and displays the total points from the dice rolls. It uses the `colorama` library to add colorful output and the `random` library to simulate the dice rolls.

## Features
- Roll any number of dice.
- Display each dice face in an ASCII art format.
- Calculate the total points based on the dice rolls.
- Colorful output with `colorama`.

## Requirements
To run this project, you need to have Python installed along with the `colorama` library.

You can install the `colorama` library by running:

```bash
pip install colorama
```

## How to Use

1. Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/Dice-Roller-Game.git
```

2. Navigate into the project directory:

```bash
cd Dice-Roller-Game
```

3. Run the game:

```bash
python dice_roller_game.py
```

4. Follow the on-screen prompts to roll the dice and view the results.

## Example Output

```
----------------------------------------------------------
Press ENTER to begin---
Number of dice to roll: 3
┌─────────────┐  ┌─────────────┐  ┌─────────────┐
│             │  │             │  │             │
│      ●      │  │   ●         │  │   ●         │
│             │  │             │  │             │
│             │  │         ●   │  │         ●   │
│             │  │             │  │             │
└─────────────┘  └─────────────┘  └─────────────┘

Calculating----
Total Points = 8
----------------------------------------------------------
Press ENTER to quit.---
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements
- The game uses the `colorama` library to provide colorful console output.
- ASCII art used for the dice faces.


# Ludo Game Simulator
![ludo](https://github.com/elikem1z/Ludo-Game/assets/109632084/4c98a60b-79fd-4aaa-8849-33c4a0f58504)




## Overview

This project is a Python-based simulation of the classic board game Ludo, designed for two players. It includes all the essential features of the traditional game, such as player movement based on dice rolls, switching turns, and a check for winning conditions. The project aims to provide an interactive and enjoyable experience, simulating the game dynamics with user inputs for player names and choices throughout the game.

## Motivation

The motivation behind creating this Ludo game simulator was to bring the cherished board game experience into the digital realm, allowing players to enjoy the game without the need for physical components. This project also serves as an educational tool for beginners in Python programming, demonstrating basic programming concepts like classes, loops, and conditionals in a fun and engaging way.

## Code Style

This project adheres to the Python PEP 8 style guide to ensure the readability and maintainability of the code.

## Screenshots

![Ludo Game Interface](#) *Screenshot of the game interface here*

## Tech/Framework Used

**Built with**
- Python 3.9

## Features

- **Interactive Gameplay:** Players can enter their names and interact with the game through console inputs.
- **Dice Simulation:** Includes a simulated dice roll with outcomes affecting player piece movement.
- **Player Turns:** Players take turns based on dice roll outcomes, with special rules for rolling a six.
- **Win Condition Checking:** The game checks for win conditions, announcing the winner and concluding the game.

## Code Example

```python
player1 = Player(input('Player1, enter your username: '), 'red')
player2 = Player(input('Player2, enter your username: '), 'blue')
ludo2()  # Start the game
```

## Installation
To run this Ludo game simulator, follow these steps:

1. Ensure Python 3.x is installed on your system.
1. Download the project files to your local machine.
1. Open a terminal or command prompt in the project directory.
1. Run the script with the command: python ludo_game.py


## How to Use?
To play the game, start the script as mentioned above. The game will prompt you to enter player names and guide you through the game rules. Follow the on-screen instructions to roll the dice, select pieces to move, and navigate your pieces towards victory.

## Contribute
Contributions are welcome! If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcomed.

## Credits
Inspiration for this Ludo game simulator came from playing the traditional board game with family and friends and a desire to replicate that experience digitally.

## License
MIT © Elikem Hamenoo

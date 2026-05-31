# Bulls & Cows Game 🐂🐄

A command-line version of the classic "Bulls and Cows" game, written in Python.

## Description

The computer generates a random 4-digit number with **unique digits** (the first digit is not 0).
The player tries to guess the number in a limited number of attempts.

- **Bulls** – correct digit in the correct position.
- **Cows** – correct digit but in the wrong position.

## How to Run

1. Make sure you have Python 3 installed.
2. Clone this repository or download `BullsAndCows.py`.
3. Run the game in your terminal:

```bash

python BullsAndCows.py

```

## Difficulty Levels

When starting the game, you can choose a difficulty level:

- **Level 1** – 10 attempts
- **Level 2** – 7 attempts
- **Level 3** – 5 attempts

## Input Rules

- You must enter a **4-digit number**.
- Digits **must not repeat**.
- The **first digit cannot be 0**.
- If the input is invalid, the game asks you to try again **without spending an attempt**.

## Implementation Details

- Uses Python's `random` module to generate the secret number.
- Uses `while` and `for` loops, as well as `if/elif/else` conditions.
- User input is validated using loops until a correct value is provided.
- The game can be played multiple times in a single session.

## Author

Educational Python implementation of the "Bulls and Cows" game.

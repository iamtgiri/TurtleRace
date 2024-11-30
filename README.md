# Turtle Race Game

## Overview
This is a Python-based turtle race game where players can log in as new or existing users and place bets on which turtle will win the race. Players can bet their points, watch the turtles race, and see if they win or lose based on their prediction. The game uses the `turtle` library for graphical output and the `pandas` library for managing user data and scores.

## Features
- **User Login**: New users can create an account, while existing users can log in using their username and password.
- **Turtle Race**: Players can choose which turtle (out of four) they think will win the race and bet points on the selected turtle.
- **Interactive Gameplay**: The game features animated turtles racing on a graphical interface.
- **User Score Tracking**: After each race, the user's points are updated based on the result (win/lose).
- **Data Storage**: User details and points are stored in a CSV file (`usersdata.csv`), ensuring that scores persist between game sessions.

## Requirements
- **Python 3.x**: Ensure Python is installed on your machine.
- **Libraries**: The following libraries must be installed:
  - `turtle`
  - `random`
  - `time`
  - `csv`
  - `pandas`

You can install the required libraries by running:
```bash
pip install pandas
```

## Files
1. **Turtle Race Game Script** (`turtle_race.py`): The main Python file that contains the game logic.
2. **Users Data CSV** (`usersdata.csv`): A CSV file used to store user information (username, password, and points). This file is automatically created and updated as users log in and play the game.

## How to Run
1. Download or clone the repository containing the `turtle_race.py` file.
2. Ensure the required libraries (`turtle`, `random`, `time`, `csv`, `pandas`) are installed.
3. Run the Python script:
   ```bash
   python turtle_race.py
   ```
4. Follow the on-screen prompts to log in or register as a new user.
5. Select a turtle to bet on, enter your bet amount, and watch the turtles race!
6. After the race, the game will update your score based on whether you guessed the winner correctly.
7. You can choose to play again or exit.

## Game Flow
1. **Login**: The user will be prompted to either log in as an existing user or register as a new user.
2. **Race Setup**: A race track is drawn, and four turtles are initialized, each with different colors.
3. **Betting**: The user is asked to select a turtle and enter a bet amount. The bet amount cannot exceed the current score.
4. **Race**: The turtles race across the screen with random movements. The race continues until one of the turtles crosses the finish line.
5. **Result**: The game will display whether the user won or lost based on the selected turtle.
6. **Score Update**: The user’s score is updated and stored in `usersdata.csv`.

## Example
```
Are you new here?
If you are a new user, enter: N
If you are an old user, enter: O
> N

Username: user123
Password: password123

Successfully Login
Hello user123, Welcome to The Turtle Race

Which turtle will win the game? (Choose 1-4)
> 2

Points you have now: 5000
How much do you want to bet?
> 500

[Race Animations...]
Congrats! You Win!
Your new points are 5500

Would you like to play again? (Y/N)
> N
```

## User Data Format
- **usersdata.csv**: Stores user details and points. The CSV file has the following structure:
  ```
  Name, Password, Points
  user123, password123, 5000
  ```

## Notes
- The game is designed to be played on a fullscreen graphical interface.
- If the user chooses to play again, the race resets and the score is carried over.
- The turtle race game is simple yet fun and is an ideal way to practice programming with graphics and user interactions in Python.

## License
This project is open-source and free to use for personal or educational purposes. No warranty is provided for the code's functionality or usage.


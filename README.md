# Hangman

## Contents 

- [Project Description](#project-description)
- [Installation Instructions](#installation-instructions)
- [Usage Instructions](#usage-instructions)
- [File Structure](#file-structure)
- [License Information](#license-information)

## Project Description
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

The Hangman project is a Python-based implementation of the classic word-guessing game. In this digital rendition, the computer selects a word from a predefined list of fruits, and the player attempts to guess it letter by letter. The aim of the project is to provide a simple yet engaging command-line game that demonstrates basic programming concepts such as loops, conditionalobject oriented programmings, and data structures in Python.

This project serves not only as an entertaining game but also as an educational tool. By developing it, I deepened my understanding of Python programming, especially in areas such as string manipulation, handling user input, and maintaining game state. Additionally, the project provided valuable practice in structuring code using classes and functions to create a well-organized and easily understandable codebase.

Through the process of creating the Hangman game, I learned the importance of planning and breaking down a problem into smaller, manageable tasks. This was aided by the way in which the project was structured into milestones. It also offered insights into the user experience design, even in a text-based environment, emphasizing the need for clear instructions and feedback to the player. This project has been a practical exercise in applying theoretical knowledge to a real-world application, reinforcing my programming skills and contributing to my growth as a developer.

## Installation Instructions
To run this game, you will need Python installed on your computer. This code was written and tested with Python 3.11.5 but should be compatible with any Python 3.x version.

Ensure Python 3 is installed on your system. You can download it from python.org.
Download the Hangman file to your local machine. You can do this by cloning the repository or simply copying the code into a .py file. Note that this repo is broken down into 4 separate python files: milestone_2.py, milestone_3.py, milestone_4.py, and milestone_5.py. The completed hangman code which is ready to play is only on milestone_5.py. For ease of use, save milestone_5.py on your machine as hangman.py.
No external libraries are required for this project.

## Usage Instructions 
After installing, follow these steps to play the game:

1. Open a terminal or command prompt.
2. Navigate to the directory where you saved the Hangman game script.
3. Run the script using Python by typing python3 hangman.py 
4. Follow the on-screen instructions to play the game. The game will prompt you to guess letters until you either guess the word correctly or run out of lives.

## File Structure
The Hangman project consists of several python scripts which were used in the development of the hangman game. Since this project was used as an educational excercise to consolidate the lessons that I had learnt at AiCore, each script was used to progressively expand on the code, focusing on different aspects of what was learnt on the course. 
1. 'milestone_2.py': This is the first python file created for the hangman project. This file focused on creating variables for the game. It also involved creating if-else statements and while loops.
2. 'milestone_3.py': This file added if-else and while loops which checked if the user input was valid and whether their guess was in the chosen word.
3. 'milestone_4.py': This file focused on using Object Oriented Programming (OOP) and creating a class to develop a complete hangman game. 
4. 'milestone_5.py': The final Python script containing the Hangman game logic and execution flow. This file is the the culmination of the project, where all of the concepts learnt come together. This file includes the Hangman class definition and the play_game function which together manage the game's setup, player interactions, and game-over conditions. 

## Licence Information
This Hangman game is provided under the MIT License. You are free to use, modify, and distribute the code as you see fit

MIT License

Copyright (c) [2024] [Wellington Saikat]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
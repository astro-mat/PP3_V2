
# Battleships Game

Battleships is a Python-based terminal game where players engage in a battle against the computer. The objective is to sink all three of the opponent's ships on the playboard. Each player has 10 turns to make their shots by guessing coordinates. This game is hosted on the Code Institute's mock terminal on Heroku.

A live link to the game can be found here: [Battleships Game](https://mattleships-1ef855055238.herokuapp.com/).

![Battleship - am i responsive](images/amiresponsive.png)




## How to play

The game is played with two boards, one for each pplayer.

Each game board is a 5 x 5 grid labeled from 0 to 4. the player chooses a coordinate to guess where the computers ship is. The computer does the same.

On a player's board, ships are represented by '@' symbols. When an opponent successfully hits a ship, that coordinate is marked with an 'X'. A miss is indicated by a '*' symbol.

The computers board does not display the ships. Only the hits and misses

Players are given 10 turns each to try and hit all three ships.

Players have the option to exit the game if they choose to do so before each turn.

## Site Owner Goals  

- To offer the user an enjoyable and straightforward gaming experience.

- To ensure the game is well-designed and user-friendly, making it easy to navigate.

- To allow the user the option to play another round or request a rematch.

## User Stories 

- ### As a first time user, I want to: 

- I wish to quickly grasp the game's instructions.

- I want a game that is both simple and enjoyable to play.

- I seek the option to exit the game whenever I choose.

- I want the ability to play another round once the current game concludes.

## Flowchart  

I sketched out a flowchart to clearly grasp the game's underlying logic and structure.

This tool was instrumental in organizing my project, particularly in verifying user inputs.

The flowchart's logic guided me in determining the types of functions to develop and how these functions should interact with one another.

![Flowchart Image](images/flowchart.png) 

## Features 

#### Username Input & Instructions  

The game begins with the game title and a brief desciption of the game.
The user is then prompted to enter a username.

![Screenshot of the game](images/usernameandinstructions.png) 

#### Game initialisation

The game is started. Some information is displayed about the game
- The board size
- The number of ships each side has
- the number of turns each player has
- A description of the numbers of the board

The two boards are then displayed, the players board with his ships visable and the computers board showing no ships

![Game initialisation](images/init_game.png) 








Future

Adjust level of dificulty
keep both computer and players score
increase ship size
include graphics



# Credits

- [Code institute Love Sandwiches Project](https://github.com/tildeholmqvist/LoveSandwiches)
- [W3Schools](https://www.w3schools.com/)
- [Stack Overflow](https://stackoverflow.com/)


- [Battleships game by Mark Anthony Lleg](https://llego.dev/posts/how-code-simple-battleship-game-python/)
- [Python Battleship with Object Oriented Programming](https://www.youtube.com/watch?v=alJH_c9t4zw&t=275s&ab_channel=KnowledgeMavens)
- [Battleships game by Tilde Holm](https://github.com/tildeholmqvist/battleshipgame)
- And my mentor Antonio for all his help.

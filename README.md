# Battleship Game

Battleship is a strategy type guessing game for two players. It is played on a board on which each player's fleet of battleships are marked. The locations of the fleets are hidden from the other player. Players alternate turns attacking the other player's ships, and the objective of the game is to destroy the opposing player's fleet.

Battleship is known worldwide. The game is played on grids. The grids are typically square – usually 10×10. The individual squares in the grid are identified by letter and number. On one grid the player arranges ships and records the shots by the opponent. On the other grid, the player records their own shots.

Before play begins, each player's ships are secretly arranged on their grid. Each ship occupies a number of consecutive squares on the grid, arranged either horizontally or vertically. The number of squares for each ship is determined by the size of the ship. The ships cannot overlap (i.e., only one ship can occupy any given square in the grid). The size and numbers of ships allowed are the same for each player. These may vary depending on the rules. The ships should be hidden from each player. The game is a discovery game which players need to discover their opponents ship positions.
After the ships have been positioned, the game proceeds in a series of rounds. In each round, each player takes a turn to announce a target square in the opponent's grid which is to be attacked. The opponent reveals whether or not the square is occupied by a ship. Records of 'Hits' and 'Misses' are made.
When all of the squares of a ship have been hit, the ship's owner reveals the sinking of the ship. If all of a player's ships have been sunk, the game is over and their opponent wins.

A live website can be found [here](https://project-3-battle.herokuapp.com/)

<img width="920" alt="Am I responsive battleship" src="https://user-images.githubusercontent.com/88341568/200432813-8634ab57-f230-43a3-bbba-e4dcf5d31aba.png">

## Table of Contents

1. [Plans and structure](#plans-and-structure)
    - [Objectives](#objectives)
2. [Features](#features)
    - [Welcome to Battleship](#welcome-to-battleship)
    - [Instructions](#instructions)
    - [Game](#game)
    - [Losing message](#losing-message)   
    - [Winning message](#winning-message) 
    - [Extra features](#extra-features)
3. [Testing](#testing)
    - [Manual Testing](#manual-testing)
    - [Bugs](#bugs)
4. [Deployment](#deployment)
5. [Credits](#credits)

## Plans and Structure 

<img width="371" alt="lucid app diagram Pro-3" src="https://user-images.githubusercontent.com/88341568/200435940-95b1281d-6886-4e5f-86e7-56991aa8739f.png">

## Objectives

To create a game that is easy to navigate. The game is straight forward. Choose a letter from A-J and then choose a number from 0-9.

<img width="547" alt="general game play" src="https://user-images.githubusercontent.com/88341568/200438924-75a990ba-a4f3-4d54-876a-e14953fe03c4.png">


To build a game that ran in a smooth loop. This allows the player to continue to play the game or quit the game.

<img width="545" alt="quitting game" src="https://user-images.githubusercontent.com/88341568/200438857-9c9301ed-0a37-4bbb-bded-c5242b10b888.png">

To update the player throughout the game so that they are aware of how many of their ships have been destroyed and the enemies ships have been destroyed.

<img width="545" alt="enemy hits and destroys ship" src="https://user-images.githubusercontent.com/88341568/200438803-3d1bf4bb-8c0d-4866-9620-051919b08365.png">


## Features

### Welcome to Battleship

The first thing the player will see is the welcome message and the player board. It is a 10X10 board with letter A-J on the x-axis and numbers 0-9 on the y-axis. The board is populated with **'x'** to represent the ships and **'-'** to represent area void of ships.

<img width="542" alt="home screen" src="https://user-images.githubusercontent.com/88341568/200529960-bf9edff8-c243-4f23-b757-efe2b64bf949.png">

### Instructions

The player is asked to select a target on their enemy's board and is given an example 'A5'. If lowercase for example 'a5' is selected the game accepts this an entry and capitilises the letter 'a' to 'A' in this example. However, if the player enters the wrong format such as 'aa', '55' or '5a' and so on. A helper message of how to enter the data will appear.

<img width="545" alt="helper message" src="https://user-images.githubusercontent.com/88341568/200528899-d14eee8d-dc1a-4125-9859-182a14d4bd99.png">

### Game

Once the player has entered the coordinates they want to attack, the message 'You launch an attack' will appear. If the player misses, a 'Miss!' message will appear. If the player hits they will see the message 'Direct Hit!'. The same is true for the opponent except for the opponents message wil be 'Your enemy launches an attack'. If the same coordinates are chosen again the player is prompted by the 'That position has already been attacked!' message. If the battleship was destroyed the message 'Battleship Destroyed! appears.


<img width="547" alt="general game play" src="https://user-images.githubusercontent.com/88341568/200438924-75a990ba-a4f3-4d54-876a-e14953fe03c4.png">


### Winning Message

Victory! Enemy ships destroyed.

### Losing Message

Game Over! Players ships destroyed.

<img width="549" alt="Test Game Over" src="https://user-images.githubusercontent.com/88341568/200537942-1e0145c6-ffe0-46d1-8c90-2c44a9f4bccc.png">


### Extra Features

There is a count feature. When a battleship is destroyed for either the player or opponent is prompted with the message 'You have or your enemy has X number of ships remaining' depending on how many ships have been sunk out of the original fleet.

When the players ship is hit. The target is removed from the players displayed board.

<img width="554" alt="ship count" src="https://user-images.githubusercontent.com/88341568/200538670-0f6a745f-9ce8-4e57-9018-ff2608017e67.png">

## Testing

### Manual Testing

To validate the input I entered invalid coordinates.

The quit feature was checked and validated.

I validated that all the message prompts were accurate and appeared at the correct time.

I validated that the count feature was working properly and that the player target was removed from the board.

I player the game to the end to ensure that the 'Game Over!' and 'Victory!' features were present.

<img width="549" alt="Test Game Over" src="https://user-images.githubusercontent.com/88341568/200542621-a78d571b-d8cf-4e2c-87df-e6b44182dd48.png">

### Bugs

I had trouble trying to update the score of the battleship destroyed count. Using the len function I was able to return the number of ships remaining.

<img width="459" alt="bug pro-3" src="https://user-images.githubusercontent.com/88341568/200540564-4690cdf0-8ba6-487a-9ba8-7d906f81b8e0.png">

## Deployment

<img width="937" alt="heroku dashboard" src="https://user-images.githubusercontent.com/88341568/200442610-203209c2-321f-4178-a63e-bda2a10acb27.png">



There were many steps to deploying this project to **Heroku**:

1. On the Heroku dashboard click on 'create a new app'.
2. Choose a unique name for the app.
3. Select region and click create app. 
4. Click the settings tab at the top of the page. 
5. Add the buildpacks required by clicking on the buildpack button.
 - select relevant buildpack eg. python, nodejs.
 - The order in which the buildpacks are needed can be arranged accordingly.
6. click the deploy tab.
7. Select github as the deployment method and click connect to github.
8. Once this is selected, search for the relevant github repository name, and connect to the correct repository.
9. Scroll down and there were two options.
 - The first option - to enable automatic deployment, which means that Heroku will rebuild the app every time a change is pushed to github.
 - The other option - to manually deploy, where the build logs can be seen.
10. When all the code is received from github, click the view button that links to the running app.


## Credits

**The code content**

https://learn.codeinstitute.net/login?next=/

https://www.youtube.com/



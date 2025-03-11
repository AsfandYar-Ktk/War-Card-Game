# War - A Card Game (OOP)  

This is an object-oriented implementation of the classic card game **War**, developed as part of the *Python and Django Full Stack Web Developer Bootcamp 2023* course. The game is played between a user and the computer, following a structured set of rules.  

## **Game Rules (Implementation-Specific)**  
- Each player draws **one card** from their deck. The player with the higher card wins and takes both cards.  
- If both cards are **equal**, a **War** occurs:  
  - Each player draws **three additional cards** face down.  
  - Then, they draw **one more card** and compare it.  
  - The player with the higher last-drawn card wins **all the cards** in the War pile.  
  - If a tie happens again, another War follows the same process.  
- The game continues until one player **runs out of cards**, and the other player is declared the winner.  

## **Technologies Used**  
- Python  
- Object-Oriented Programming (OOP) Concepts  

## **How to Play**  
1. Run the Python script.  
2. Enter your name when prompted.  
3. The game progresses automatically, displaying each round’s results.  
4. The winner is declared when one player has all the cards.  

## **Features**  
✅ OOP-based structure with `Deck`, `Hand`, `Player`, and `War` classes  
✅ Fair, randomized deck shuffling  
✅ Automatic game logic with round-by-round updates  
✅ War mechanics for resolving ties  

Enjoy playing **War**! 🚀
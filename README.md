The code you provided is a simple implementation of a Tic-Tac-Toe game in Python. It allows two players to take turns entering their moves until the game ends in either a win or a draw. The game board is displayed using a 3x3 grid, and players input their moves using (X, Y) coordinates.

Here's a brief overview of the code:

list_cordinates: This is a 2D list representing the game board. It is initialized with empty spaces.

add_to_list(xy, xo): This function takes the input coordinates xy and the current player's symbol xo and adds the move to the game board if the chosen position is not already occupied. If the position is already taken, it asks the player to input again.

check_result_game(list_cordinates, xo): This function checks if the current player with symbol xo has won the game by matching three symbols in a row (horizontally, vertically, or diagonally).

print_result_game(): This function displays the current state of the game board.

main_game(xo, ilosc_ruchow, list_cordinates): This is the main function that handles the game loop. It alternates between player O and player X, taking their input and updating the game board accordingly until the game ends.

The game loop continues until all nine positions on the board are filled, resulting in a draw. If a winning condition is met, the game ends, and the player who achieved it is declared the winner.

To play the game, you can run the code in a Python environment. It will prompt players for input and display the game board after each move. To stop the game at any point, you can use Ctrl+C in the terminal.

Please note that this implementation lacks input validation for some cases (e.g., handling non-integer input, out-of-bounds input, etc.). Additionally, the implementation uses recursion to handle incorrect inputs, which might not be the most efficient way to handle such cases.

Overall, this is a basic implementation, and you can further enhance it by adding more features, error handling, or creating a graphical interface for a better user experience.



# Tic-Tac-Toe Game

This is a simple implementation of the classic Tic-Tac-Toe game in Python. Two players can take turns to make their moves until the game ends in a win or a draw.

## How to Play

1. The game board is displayed as a 3x3 grid.
2. Players take turns entering their moves using (X, Y) coordinates.
3. The game ends when either one player achieves three symbols in a row (horizontally, vertically, or diagonally) or all positions on the board are filled without a winner, resulting in a draw.

## How to Run

1. Clone this repository to your local machine.
2. Open a terminal or command prompt and navigate to the project directory.
3. Run the game using the following command:

```bash

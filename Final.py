import numpy as np
import matplotlib.pyplot as plt

def my_scoreboard(score_board, pixel_left):  
    """
    Display the scoreboard with player names, scores, and pixels left.

    Args:
        score_board (dict): Dictionary containing player names as keys and their scores as values.
        pixel_left (dict): Dictionary containing player names as keys and the number of pixels left as values.
    """
    print("\t--------------------------------")  
    print("\t         The SCOREBOARD for Concave Combat  PYTHON GAME       ")  
    print("\t--------------------------------")  
   
    list_of_the_two_players = list(score_board.keys())  
    pixel_left_list = list(pixel_left.keys())
    
    print("\t   ", "Player Name", "|", "Score board", "|", "Pixel Left")
    print("\t   ", list_of_the_two_players[0], "\t", score_board[list_of_the_two_players[0]], "\t", pixel_left[pixel_left_list[0]])  
    print("\t   ", list_of_the_two_players[1], "\t", score_board[list_of_the_two_players[1]], "\t", pixel_left[pixel_left_list[1]])  
   
    print("\t--------------------------------\n")

def CheckConcave(grid, x, y):
    """
    Check if an orthogonal concave shape is formed in the grid.

    Args:
        grid (2D array): The grid representing the game board.
        x (int): The x-coordinate of the last pixel placed.
        y (int): The y-coordinate of the last pixel placed.

    Returns:
        bool: True if an orthogonal concave shape is formed, False otherwise.
    """
    n = len(grid)
    m = len(grid[0])
    flag1 = flag2 = False

    for j in range(m):
        if j == y:
            continue
        if grid[x][j] == 1:
            for k in range(j+1, y):
                if grid[x][k] == 1:
                    break
                if k == y-1:
                    flag1 = True

            if flag1:
                for k in range(j, y+1):
                    if x-1 >= 0 and grid[x-1][k] == 0:
                        break
                    if k == y and x-1 >= 0:
                        flag2 = True

                for k in range(j, y+1):
                    if x+1 < n and grid[x+1][k] == 0:
                        break
                    if k == y and x+1 < n:
                        flag2 = True

    if flag1 and flag2:
        return True

    flag3 = flag4 = False
    for i in range(n):
        if i == x:
            continue
        if grid[i][y] == 1:
            for k in range(i+1, x):
                if grid[k][y] == 1:
                    break
                if k == x-1:
                    flag3 = True

            if flag3:
                for k in range(i, x+1):
                    if y-1 >= 0 and grid[k][y-1] == 0:
                        break
                    if k == x and y-1 >= 0:
                        flag4 = True

                for k in range(i, x+1):
                    if y+1 < m and grid[k][y+1] == 0:
                        break
                    if k == x and y+1 < m:
                        flag4 = True

    if flag3 and flag4:
        return True

    return False


def right_to_left(grid, p, q):
    """
    Flip the grid from right to left.

    Args:
        grid (2D array): The grid representing the game board.
        p (int): The x-coordinate of the last pixel placed.
        q (int): The y-coordinate of the last pixel placed.

    Returns:
        bool: True if an orthogonal concave shape is formed after flipping, False otherwise.
    """
    n = len(grid)
    m = len(grid[0])
    x = p
    y = m-1-q

    for i in range(n):
        grid[i] = np.flip(grid[i])
    return CheckConcave(grid, x, y)


def top_to_bottom(grid, p, q):
    """
    Invert the grid from top to bottom.

    Args:
        grid (2D array): The grid representing the game board.
        p (int): The x-coordinate of the last pixel placed.
        q (int): The y-coordinate of the last pixel placed.

    Returns:
        bool: True if an orthogonal concave shape is formed after inverting, False otherwise.
    """
    n = len(grid)
    m = len(grid[0])
    x = n-1-p
    y = q

    grid = np.flip(grid)

    return CheckConcave(grid, x, y)


# Main code

# Create an empty grid
data1 = np.zeros([10,10])
fig, ax = plt.subplots()

# Prompt for player names
print("The First Player's name")
player_first = input("Please mention your name: ")
print("\n")
print("The Second Player's name")
player_second = input("Please mention your name: ")
print("\n")

# Initialize pixel and score trackers for each player
pixel_left = {player_first: 10, player_second: 10}
score_board = {player_first: 0, player_second: 0}
player_current = player_first

# Main game loop
while pixel_left[player_first] != 0 or pixel_left[player_second] != 0:
    # Set up the plot
    ax.set_xlabel('Y')
    ax.set_ylabel('X')
    ax.set_title("Concave_combat")

    # Prompt the current player for coordinates
    print(player_current, " your Turn ")
    user = input("Enter the coordinates x and y - ")
    pixel_left[player_current] = pixel_left[player_current] - 1
    axis = tuple(int(item) for item in user.split())
    x = int(axis[0])
    y = int(axis[1])

    # Update the grid with the placed pixel
    data1[x, y] = 1

    # Show the updated grid
    ax.imshow(data1, cmap='Greys_r')
    ax.plot()
    plt.show(block=False)

    # Check for concave shape formation and update scores accordingly
    ans1 = CheckConcave(data1, x, y)
    ans2 = right_to_left(np.copy(data1), x, y)
    ans3 = top_to_bottom(np.copy(data1), x, y)
  
    if int(ans1 or ans2 or ans3):
        score_board[player_current] = score_board[player_current] - 1
        print("Score Deducted")
        my_scoreboard(score_board, pixel_left)
        data1[x, y] = 0
    else:
        score_board[player_current] = score_board[player_current] + 1
        print("Score Added")
        my_scoreboard(score_board, pixel_left)
   
    # Prompt for continuing or quitting the game
    op = input("Do you want to continue or quit the game? (C/Q): ")
    if op.lower() == 'q':
        break
   
    # Switch to the other player's turn
    if player_current == player_first:
        player_current = player_second
    else:
        player_current = player_first

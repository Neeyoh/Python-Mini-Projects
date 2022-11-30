# lets create a board object to represent the minesweeper game
# this is so that we can just say "create a new board object", or
# "dig here", or "render this game for this object"

class Board:
    def __init__(self, dim_size, num_bombs):

# play the game
def play(dim_size = 10, num_bombs = 10):
    # Step 1: create the board and plant the bombs
    # Step 2: show the user the baord and ask for where they want to dig
    # Step 3a: if location is a bomb, show game over message
    # Step 3b: if location is not a bomb, dig recursively until each square is at least next to a bomb
    # Step 4: repeat steps 2 and 3a/b until there are no more places to dig -> VICTORY!
    pass
# Langston's Ant Class
# 11/27/2021
# Coding it for fun


class Ant:
    '''This class will create an object of type Ant that will traverse a grid
    and depending on what type of square it lands on it will have an affect on
    the grid.
    - a white space is indicated with a - char
    - a black space is indicated with a # char
    - the space with the ant is indicated with a * char
    '''

    def __init__(self, num_columns, num_rows,
                 num_steps, ant_loc_row,
                 ant_loc_col, direction):
        '''initialize some varaibles right off the bat including
        - current location
        - number of steps to execute
        - direction ant is facing
        - board size
        '''
        self._num_columns = num_columns
        self._num_rows = num_rows
        self._num_steps = num_steps
        self._ant_loc_row = ant_loc_row
        self._ant_loc_col = ant_loc_col
        self._ant_direction = direction
        self._game_board = []
        self._counter = 0
        self._under_ant = '#'

    def rotate_ant(self):
        '''Rotate the ant 90 degrees right if white and rotate
        90 degrees left if black
        '''

    def flop_color(self):
        '''This function is used to change the color that
        the ant is on to the appropriate color
        '''
        if self._under_ant == '#':
            self._under_ant = '.'
        else:
            self._under_ant = '#'

        self._game_board[self._ant_loc_row - 1][self._ant_loc_col - 1] = self._under_ant

    def move_ant(self):
        '''This method will control the movement of the ant. It will take
        count as a parameter, and will return the count which will control
        if the ant keeps moving
        '''
        # up = 0
        # right = 1
        # down = 2
        # left = 3
        self.flop_color()
        if self._ant_direction == 0:
            self._ant_loc_row -= 1
            if self._ant_loc_row < 1:
                self._ant_loc_row = self._num_rows

        elif self._ant_direction == 1:
            self._ant_loc_col += 1
            if self._ant_loc_col > self._num_columns:
                self._ant_loc_col = 1

        elif self._ant_direction == 2:
            self._ant_loc_row += 1
            if self._ant_loc_row > self._num_rows:
                self._ant_loc_row = 1

        elif self._ant_direction == 3:
            self._ant_loc_col -= 1
            if self._ant_loc_col < 1:
                self._ant_loc_col = self._num_columns

        self._under_ant = self._game_board[self._ant_loc_row - 1][self._ant_loc_col - 1]
        if self._under_ant == '#':
            if self._ant_direction == 0:
                self._ant_direction = 3
            else:
                self._ant_direction -= 1
        elif self._under_ant == '.':
            if self._ant_direction == 3:
                self._ant_direction = 0
            else:
                self._ant_direction += 1

        self._game_board[self._ant_loc_row - 1][self._ant_loc_col - 1] = '*'

    def draw_board(self):
        '''Draw the board at the beginning of the game and after every move
        of the ant. Use the * unpacking operator to print all of the elements
        in the list.
        '''
        for row in self._game_board:
            print(*row)

    def build_board(self):
        '''Use this method to construct a board of all white spaces and
        use the data members for the board size
        '''

        # build the game board
        self._game_board = [['.' for x in range(self._num_columns)
                             ]for y in range(self._num_rows)]

        # check the color under the ant and store it for later
        self._under_ant = self._game_board[self._ant_loc_row - 1][self._ant_loc_col - 1]

        # Set ant icon for initial location
        self._game_board[self._ant_loc_row - 1][self._ant_loc_col - 1] = '*'

        # Start the steps and run them while counting down to zero
        while self._counter != self._num_steps:
            self._num_steps -= 1
            self.draw_board()
            self.move_ant()


def begin_ant(play_decision):
    '''Star Langstons Ant. Take play_decision as a parameter to
    decide if it should continue or end
    '''
    if play_decision == 'yes' or play_decision == 'y':
        # num_columns = int(input('how many rows? :'))
        # num_rows = int(input('how many columns? :'))
        # num_steps = int(input('how many moves (steps)? :'))
        # ant_loc_row = int(input('whats the many starting rows? :'))
        # ant_loc_col = int(input('whats the starting column? :'))
        # ant_direction = randrange(4)
        # ant_map = Ant(num_columns, num_rows,
        #               num_steps, ant_loc_row,s
        #               ant_loc_col, ant_direction)

        # USE THE BELOW FOR TESTING AND REVERT TO ABOVE FOR FINISH
        ant_map = Ant(100, 128,
                      500, 50,
                      64, 1)
        ant_map.build_board()


def menu():
    '''This menu is outside of the class and we should be able to reuse this
    menu for future programs. This menu will take no parameters and will
    not return anything
    '''
    start_or_end = ''
    choice = ["y", "n", "yes", "no"]
    while start_or_end not in choice:
        start_or_end = input('Start Langston\'s Ant? :').lower()
    return start_or_end


play_decision = menu()
begin_ant(play_decision)

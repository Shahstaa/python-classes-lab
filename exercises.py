class Game:
    next_game_id = 1
    
    def __init__(self):
        self.turn = 'X' 
        self.tie = False
        self.winner = None
        self.board = {
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None,
        }
        self.game_id = Game.next_game_id
        Game.next_game_id += 1

    def print_board(self):
        b = self.board
        print(f"""
            A   B   C
        1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
            ----------
        2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
            ----------
        3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
        """)

    def print_message(self):
        if self.tie:
            print("It's a tie!")
        elif self.winner:
            print(f"Player {self.winner} wins the game!")
        else:
            print(f"It's player {self.turn}'s turn!")

    def render(self):
        self.print_board()
        self.print_message()

    def get_move(self):
        while True:
            move = input(f"Player {self.turn}, enter a valid move (example: A1): ").lower()
            if move not in self.board:
                print("Invalid move! Please enter a valid position like A1, B2, etc.")
            elif self.board[move] is not None:
                print("That space is already taken. Try again.")
            else:
                return move

    def check_for_winner(self):
        win_conditions = [
            ['a1', 'b1', 'c1'], ['a2', 'b2', 'c2'], ['a3', 'b3', 'c3'],  # Rows
            ['a1', 'a2', 'a3'], ['b1', 'b2', 'b3'], ['c1', 'c2', 'c3'],  # Columns
            ['a1', 'b2', 'c3'], ['a3', 'b2', 'c1']  # Diagonals
        ]
        for condition in win_conditions:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] != None:
                self.winner = self.board[condition[0]]
                return True
        return False

    def check_for_tie(self):
        if all(space is not None for space in self.board.values()) and self.winner is None:
            self.tie = True
            return True
        return False

    def switch_turn(self):
        self.turn = 'O' if self.turn == 'X' else 'X'

    def play_game(self):
        print("Welcome to Tic-Tac-Toe!")
        while not self.winner and not self.tie:
            self.render()  
            move = self.get_move()  
            self.board[move] = self.turn  
            if self.check_for_winner():  
                break
            if self.check_for_tie():  
                break
            self.switch_turn()  
        
        self.render() 

    @classmethod
    def get_total_games(cls):
        return cls.next_game_id - 1

    def __str__(self):
        return f"Tic-Tac-Toe Game #{self.game_id}: Turn: {self.turn}, Winner: {self.winner if self.winner else 'None'}, Tie: {self.tie}"

# Create and start the game
game = Game()
game.play_game()
print(f"Total games played: {Game.get_total_games()}")

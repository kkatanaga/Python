import sys

class Board():
    def __init__(self):
        self.player1 = Player()
        self.player2 = Player()
        self.player1.opponent(self.player2)
        self.create_board()
    
    def start(self):
        player = 0
        while True:
            self.print_board()
            
            if 'valid_move' in locals():
                winner = self.check_winner()
                if winner == self.player1:
                    self.print_board()
                    print('Player 1 Wins!')
                    return
                elif winner == self.player2:
                    print('Player 2 Wins!')
                    return
            
            valid_move = False

            if player == 0:
                print('Player 1\'s turn')
                while not valid_move:
                    valid_move = self.player1.move(self.board)
                player = 1
            else:
                print('Player 2\'s turn')
                while not valid_move:
                    valid_move = self.player2.move(self.board)
                player = 0
                
    def create_board(self, width=3, height=3):
        if hasattr(self, 'board'):
            return
        
        self.board = [[' ' for j in range(width)] for i in range(height)]
        self.width = width
        self.height = height
    
    def check_winner(self):
        player1_horizontal_check = True
        player2_horizontal_check = True

        player1_vertical_check = [True, True, True]
        player2_vertical_check = [True, True, True]

        player1_diagonal_check = [True, True]
        player2_diagonal_check = [True, True]

        for i, row in enumerate(self.board):
            for j, col in enumerate(row):
                player1_horizontal_check &= col == self.player1.sign
                player2_horizontal_check &= col == self.player2.sign

                player1_vertical_check[j] &= col == self.player1.sign
                player2_vertical_check[j] &= col == self.player2.sign

                if i == j:
                    player1_diagonal_check[0] &= col == self.player1.sign
                    player2_diagonal_check[0] &= col == self.player2.sign
                elif i + j == self.width - 1:
                    player1_diagonal_check[1] &= col == self.player1.sign
                    player2_diagonal_check[1] &= col == self.player2.sign

                if i < self.height - 1:
                    continue
                elif player1_vertical_check[j]:
                    return self.player1
                elif player2_vertical_check[j]:
                    return self.player2
            
            if player1_horizontal_check:
                return self.player1
            elif player2_horizontal_check:
                return self.player2
            
            player1_horizontal_check = True
            player2_horizontal_check = True
        
        for c1, c2 in zip(player1_diagonal_check, player2_diagonal_check):
            if c1:
                return self.player1
            elif c2:
                return self.player2
    
    def print_board(self):
        print('   0 1 2 ')
        print('  -------')
        for i, row in enumerate(self.board):
            print(f'{i} |', end='')
            for col in row:
                print(f'{col}|', end='')
            print()
        print('  -------')
    
    def print_players(self):
        print(f'Player 1: {self.player1.sign}')
        print(f'Player 2: {self.player2.sign}')


class Player():
    def __init__(self, player_sign=''):
        self.sign = player_sign
    
    def opponent(self, opponent):
        if self.sign != '':         # Both players have a sign
            return
        
        self.sign = 'X' if opponent.sign == 'O' else 'O'

        opponent.opponent(self)

    def move(self, board):
        try:
            x = int(input('Row: '))
            y = int(input('Column: '))

            if board[x][y] == ' ':
                board[x][y] = self.sign 
                return True
            
            return False
        except KeyboardInterrupt:
            sys.exit()
        except:
            return False

def main():
    game = Board()
    # game.print_board()
    # game.print_players()
    game.start()

main()
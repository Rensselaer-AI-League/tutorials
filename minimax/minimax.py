import random
import copy
import six

def posToIndex(pos, size):
    '''
    @param pos - (x, y)
    @param size - (width, height)
    '''
    
    index = pos[1]*size[0] + pos[0]
    
    if index >= size[0] * size[1]:
        raise IndexError
    return index

def indexToPos(index, size):
    x = index % size[0]
    y = index // size[0]
    if x < 0 or y < 0 or x >= size[0] or y >= size[1]:
        raise IndexError
    return x,y

class TicTacToeNode:
    def __init__(self):
        self.width, self.height = 3, 3
        self.board = ['.'] * self.width * self.height
        self.win_states = (\
            [0,1,2], [3,4,5], [6,7,8],\
            [0,3,6], [1,4,7], [2,5,8],\
            [0,4,8], [2,4,6]\
        )
        
        # X goes first
        self.allocations = {'X': 'Human', 'O': 'Cpu'}
        self.turn = self.allocations['X']
        self.numEmptyCells = self.width * self.height
        
    def reset(self):
        self.board = ['.'] * self.width * self.height
        self.turn = self.allocations['X']
        self.numEmptyCells = self.width * self.height
        
    def __repr__(self):
        return '%2d%2d\t%s%s%s%s%s%s%s%s%s\t%s' % ((self.width, self.height) + tuple(self.board) + self.turn())
        
    def __str__(self):
        return '%s|%s|%s\n------\n%s|%s|%s\n------\n%s|%s|%s' % tuple(self.board)
    
    def place(self, position):
        if self.numEmptyCells <= 0:
            return False
            
        if self.board[position] != '.':
            return False
        else:
            self.numEmptyCells -= 1
            if self.turn == 'Human':
                self.turn = 'Cpu'
                piece = 'X'
            else:
                self.turn = 'Human'
                piece = 'O'
            self.board[position] = piece
            return True
            
    def whoWon(self):
        for state in self.win_states:
            piece = self.board[state[0]]
            if piece == '.':
                continue
                
            for position in state:
                if self.board[position] != piece:
                    break
            else: # if the loop breaks, else doesn't happen
                return self.allocations[piece]
        
        if self.numEmptyCells <= 0:
            return "Draw"
        else:
            return "No one"
    
    def __copy__(self):
        clone = TicTacToeNode()
        clone.board = self.board[:]
        clone.turn = self.turn
        clone.numEmptyCells = self.numEmptyCells
        return clone
        
    def __deepcopy__(self, data = None):
        clone = TicTacToeNode()
        clone.board = [copy.deepcopy(i) for i in self.board]
        clone.turn = self.turn
        clone.numEmptyCells = self.numEmptyCells
        return clone
    
    def __call__(self, *args):
        l = len(args)
        if l < 1 or l > 2:
            raise TypeError('Needs x,y value or tuple')
        elif l == 1:
            x = args[0][0]
            y = args[0][1]
        else:
            try:
                x = args[0]
                y = args[1]
            except TypeError:
                return self.board[args]
        return self.board[args]
    
    def __getitem__(self, *args):
        return self(*args)
        
    # Return a list with the game state after each possible move
    def children(self):
        child_nodes = [i for i in self.childGenerator()]
            
        return child_nodes
    
    def childGenerator(self):
        for i, tile in enumerate(self.board):
            if tile == '.':
                yield copy.deepcopy(makeCopy)
                
    def heuristic(self):
        return 0
        
    def makeAIMove(self):
        moves = []
        for i, tile in enumerate(self.board):
            if tile == '.':
                moves.append(i)
        return game.place(random.choice(moves))
    
if __name__ == "__main__":
    from six.moves import input
    
    game = TicTacToeNode()     
    
    try:
        while True:
            six.print_(game)
            move = -1
            while move < 0 or move > 8:
                try:
                    move = int(input('What is your move? (0 - 8): '))
                except ValueError:
                    pass
                
            worked = game.place(move)
            victory = game.whoWon()
            
            if worked and victory == 'No one':
                game.makeAIMove()
            else:
                six.print_('That is not a legal move!')
                
            victory = game.whoWon()
            if victory == 'No one':
                continue
            else:
                six.print_(game)
                game.reset()
                if victory == 'Human':
                    six.print_('Human Wins')
                elif victory == 'Cpu':
                    six.print_('Computer Wins')
                else:
                    six.print_('It is a draw')
    except (KeyboardInterrupt, EOFError):
        pass
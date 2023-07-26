import sys,random
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QIcon
from PyQt6 import uic, QtGui, QtCore, QtWidgets

uifile = 'Sudoku.ui'
form, base = uic.loadUiType(uifile)

class MainWindow(base, form):
    def __init__(self):
        super(base, self).__init__()

        # Setup UI
        self.auto_change = True # Used to prevent the event class from triggering when the board is being created
        self.setWindowIcon(QtGui.QIcon('assets/icons/Sudoku.png'))
        self.setupUi(self)
        self.setWindowTitle("SUDOKU")
                
        self.setFixedHeight(445)
        self.setFixedWidth(935)

        # Global properties
        self.board = None
        self.solved_board = None
        self.counter = 0
        self.widgets = [self.tableWidget, self.tableWidget_2, self.tableWidget_3, 
                        self.tableWidget_4, self.tableWidget_5, self.tableWidget_6, 
                        self.tableWidget_7, self.tableWidget_8, self.tableWidget_9]
        self.ids = [i.objectName() for i in self.widgets]
        self.mistakes = self.findChildren(QtWidgets.QLabel)[1]
        
        self.widgets.installEventFilter(self, self.event, QtCore.QEvent.Type.Enter)

        # Create the game
        self.createGame([])
        
    def createGame(self,board):
        self.auto_change = True
        if board == []:
            game = Sudoku([])
            game.create_board()
            self.board = game.board
        else:
            game = Sudoku(board)

        game.print_board()
        self.setTable()
        game.solve()
        game.print_board()
        self.solved_board = game.board
        self.auto_change = False

    def resetBoard(self):
        self.createGame(self.board)

    def setTable(self):
        for k in range(9):
            widget = self.widgets[k]

            for i in range(3):
                h = i + 3 * (k // 3) # Need to increment rows for each widget
                for j in range(3):
                    l = j + 3 * (k % 3) # Need to repeat 3 columns for each widget but increment as well
                    if self.board[h][l] != 0:
                        widget.setItem(i, j, QtWidgets.QTableWidgetItem(str(self.board[h][l])))
                    else:
                        widget.setItem(i, j, QtWidgets.QTableWidgetItem(""))    

    def editCell(self,i,j):
        if self.auto_change:
            return
        id = self.sender().objectName()
        widget = self.whichWidget(id)
        k = self.ids.index(id)
        h = i + 3 * (k // 3)
        l = j + 3 * (k % 3)

        if widget.item(i,j).text() != str(self.solved_board[h][l]):
            widget.item(i,j).setBackground(QtGui.QColor(255,25,25))
            self.counter += 1
            QtWidgets.QLabel.setText(self.mistakes, str(self.counter))

    def whichWidget(self,id):
        if id in self.ids:
            return self.widgets[self.ids.index(id)]
        
    def event(self, event):
        # if event.type() == QtCore.QEvent.Type.KeyPress:
        if event.type() == QtCore.QEvent.Type.Enter:
            self.editCell(i,j)
            
        
        return super(MainWindow, self).event(event)
class Sudoku:
    '''Creating a Sudoku game using OOP and a backtracking algorithm'''
    def __init__(self, board):
        self.board = board

    def print_board(self):
        for i in range(9):
            # For every 3 rows, print a line
            if i % 3 == 0 and i != 0:
                print("---------------------")

            # For every 3 columns, print a wall
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")

                # Print the number with a space unless at the end of the row
                if j != 8:
                    print(str(self.board[i][j]) + " ", end="")
                else:
                    print(self.board[i][j])

    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return (i, j)
        return None
        
    def validate(self, num, pos):
        # Rows
        for i in range(9):
            if self.board[pos[0]][i] == num and pos[1] != i:
                return False

        # Columns
        for i in range(9):
            if self.board[i][pos[1]] == num and pos[0] != i:
                return False

        # Cells
        x = pos[1] // 3
        y = pos[0] // 3

        for i in range(y * 3, y * 3 + 3):
            for j in range(x * 3, x * 3 + 3):
                if self.board[i][j] == num and (i,j) != pos:
                    return False

        return True

    def solve_board(self):
        find = self.find_empty()
        if not find:
            return True
        else:
            row, col = find

        # Only need to check 1-9
        for i in range(1,10):
            if self.validate(i, (row, col)):
                self.board[row][col] = i

                if self.solve_board():
                    return True

                self.board[row][col] = 0
                
        return False
    
    def solve(self):
        if self.solve_board():
            return self.board
        else:
            return False
    
    def clear_board(self):
        self.board = [[0 for i in range(9)] for j in range(9)]

    def shuffle_board(self):
        # Shuffle rows
        for i in range(3):
            for j in range(3):
                if random.randint(0,1) == 1:
                    temp = self.board[i]
                    self.board[i] = self.board[j]
                    self.board[j] = temp

        # Shuffle columns
        for i in range(3):
            for j in range(3):
                if random.randint(0,1) == 1:
                    for k in range(9):
                        temp = self.board[k][i]
                        self.board[k][i] = self.board[k][j]
                        self.board[k][j] = temp

    def create_board(self):
        # Create a randomly generate board
        # First clear the board
        self.clear_board()

        # Add random num to cell
        i = random.randint(0,8)
        j = random.randint(0,8)
        num = random.randint(1,9)
        self.board[i][j] = num

        # Solve the board
        self.solve_board()

        # Shuffle board
        # random.shuffle(self.board)
        self.shuffle_board()

        # Remove numbers
        self.remove_numbers()

    def remove_numbers(self):
        for i in range(9):
            for j in range(9):
                if random.randint(0,1) == 1:
                    self.board[i][j] = 0


def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())

    # game = Sudoku([])
    # game.create_board()
    # game.print_board()
    # game.solve()
    # print("______________________________________________________")
    # game.print_board()

if __name__ == "__main__":
    main()
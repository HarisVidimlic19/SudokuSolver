from copy import deepcopy
from sys import argv, exit
from random import randint, shuffle
from PySide6 import QtGui, QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QTableWidgetItem
from PySide6.QtGui import QIcon
from new_ui_Sudoku import Ui_MainWindow

uifile = 'Sudoku.ui'

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Setup UI
        self.auto_change = True # Used to prevent the event class from triggering when the board is being created
        self.setWindowIcon(QIcon('assets/icons/Sudoku_white.png'))
        self.setupUi(self)
        self.setWindowTitle("SUDOKU")
        self.setFixedHeight(445)
        self.setFixedWidth(935)

        # Global properties
        self.board = None
        self.solved_board = None
        self.counter = 0
        self.difficulty = 0
        self.widgets = [self.tableWidget, self.tableWidget_2, self.tableWidget_3, 
                        self.tableWidget_4, self.tableWidget_5, self.tableWidget_6, 
                        self.tableWidget_7, self.tableWidget_8, self.tableWidget_9]
        self.ids = [i.objectName() for i in self.widgets]
        self.mistakes = self.findChildren(QLabel)[1]
        
        # Create the game
        self.createGame([])
        
    def createGame(self,board):
        self.auto_change = True
        if board == []:
            game = Sudoku([])
            game.create_board(self.difficulty)
            self.board = game.board
            solved = 0
        else:
            game = Sudoku(board)
            self.solved_board = deepcopy(board)
            game.remove_numbers(self.difficulty)
            solved = 1

        game.print_board()
        self.setTable()
        if solved == 0:
            game.solve()
            self.solved_board = game.board
        else:
            game.board = self.solved_board

        game.print_board()
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
                        widget.setItem(i, j, QTableWidgetItem(str(self.board[h][l])))
                    else:
                        widget.setItem(i, j, QTableWidgetItem(""))    

    def editCell(self,i,j):
        if self.auto_change:
            return
        id = self.sender().objectName()
        widget = self.whichWidget(id)
        widget.blockSignals(True) # Prevents the event class from triggering once we change bckg color
        k = self.ids.index(id)
        h = i + 3 * (k // 3)
        l = j + 3 * (k % 3)

        # If the input is wrong, change the background color to red and add to mistakes counter
        if widget.item(i,j).text() != str(self.solved_board[h][l]):
            widget.item(i,j).setBackground(QtGui.QColor(255,25,25))
            self.counter += 1
            QtWidgets.QLabel.setText(self.mistakes, str(self.counter))
        else:
            widget.item(i,j).setBackground(QtGui.QColor(255,255,255))

        widget.blockSignals(False)

    def whichWidget(self,id):
        if id in self.ids:
            return self.widgets[self.ids.index(id)]
        
    def newBoard(self):
        self.createGame([])
    
    def autoSolve(self):
        for k in range(9):
            widget = self.widgets[k]

            for i in range(3):
                h = i + 3 * (k // 3) # Need to increment rows for each widget
                for j in range(3):
                    l = j + 3 * (k % 3) # Need to repeat 3 columns for each widget but increment as well
                    widget.setItem(i, j, QTableWidgetItem(str(self.solved_board[h][l])))
    
    def selectDifficulty(self,i):
        self.difficulty = i
        self.createGame(self.solved_board)
        
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
        print("\n")

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
        cells = [1,2,3,4,5,6,7,8,9]
        shuffle(cells) # Randomize the order of the numbers for variability in board creation
        for i in cells:
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
                if randint(0,1) == 1:
                    temp = self.board[i]
                    self.board[i] = self.board[j]
                    self.board[j] = temp

        # Shuffle columns
        for i in range(3):
            for j in range(3):
                if randint(0,1) == 1:
                    for k in range(9):
                        temp = self.board[k][i]
                        self.board[k][i] = self.board[k][j]
                        self.board[k][j] = temp

    def create_board(self, d=0):
        # Create a randomly generate board
        # First clear the board
        self.clear_board()

        # Add random num to cell
        i = randint(0,8)
        j = randint(0,8)
        num = randint(1,9)
        self.board[i][j] = num

        # Solve the board
        self.solve_board()

        # Shuffle board
        # random.shuffle(self.board)
        self.shuffle_board()

        # Remove numbers
        self.remove_numbers(d)

    def remove_numbers(self, d):

        for i in range(9):
            for j in range(9):
                # Remove numbers based on difficulty
                if d == 0:
                    selector = randint(0,1)
                elif d == 1:
                    selector = randint(0,2)
                elif d == 2:
                    selector = randint(0,3)
                elif d == 3:
                    selector = randint(0,4)

                if selector >= 1:
                    self.board[i][j] = 0

def main():
    app = QApplication(argv)

    window = MainWindow()

    app.setStyle('Fusion')
    # app.UniversalTheme('Dark')

    window.show()
    exit(app.exec())

if __name__ == "__main__":
    main()
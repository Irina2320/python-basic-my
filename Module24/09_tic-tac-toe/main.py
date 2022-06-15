from tkinter import *


class Cell:

    def __init__(self, column, row):
        self.text = ''
        self.column = column
        self.row = row

        def change_state():
            if board.flag:
                self.button['text'] = 'O'
                board.flag = False
            else:
                self.button['text'] = 'X'
                board.flag = True
            self.button['state'] = DISABLED
            board.check_winner()

        self.button = Button(window, command=change_state, text = self.text)
        self.button.grid(row=row, column=column)
        self.button.config(width=10, height=5, font=("Arial", 14, "bold"))


class Board:

    cells = []

    def __init__(self):
        self.flag = False
        for column in range(3):
            for row in range(3):
                cell = Cell(column, row)
                self.cells.append(cell)

    def check_winner(self):
        for element in ('X', 'O'):
            for check in range(3):
                if all([(True if cell.button['text'] == element else False)
                        for cell in self.cells if cell.row == check]):
                    for cell in self.cells:
                        cell.button['state'] = DISABLED
                        if cell.row == check:
                            cell.button['bg'] = 'red'
                elif all([(True if cell.button['text'] == element else False)
                            for cell in self.cells if cell.column == check]):
                    for cell in self.cells:
                        cell.button['state'] = DISABLED
                        if cell.column == check:
                            cell.button['bg'] = 'red'

            if all([(True if cell.button['text'] == element else False)
                    for cell in (self.cells[0], self.cells[4], self.cells[8])]):
                for cell in self.cells:
                    cell.button['state'] = DISABLED
                    for cell in (self.cells[0], self.cells[4], self.cells[8]):
                        cell.button['bg'] = 'red'

            elif all([(True if cell.button['text'] == element else False)
                        for cell in (self.cells[2], self.cells[4], self.cells[6])]):
                for cell in self.cells:
                    cell.button['state'] = DISABLED
                    for cell in (self.cells[2], self.cells[4], self.cells[6]):
                        cell.button['bg'] = 'red'


window = Tk()
window.title("Говно-Крестики-Нолики на Python v_1.0.0")
flag = False
board = Board()

window.mainloop()

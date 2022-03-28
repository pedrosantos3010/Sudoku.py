class Cell:
    def __init__(self, row, column, value):
        self.row = row
        self.column = column
        self.value = value


class GameInput:
    def get_input(self) -> Cell:
        user_input = input(
            "Digite o input no formato uma (linha,coluna)=valor[ex:(1,2)=3] ")
        user_input = user_input.replace(" ", "")
        return Cell(int(user_input[1]) - 1, int(user_input[3]) - 1, int(user_input[6]))

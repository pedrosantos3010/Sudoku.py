import math

# TODO: Verificar como utilizar cores no terminal para informar coisas como
# "Célula gerada", "Acertou" e etc, etc


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class GameView:
    def __init__(self, cell_size):
        self.cell_size = cell_size
        self.half_cell_size = math.ceil(self.cell_size / 2)

        self.cell_height = self.cell_size / 2
        self.half_cell_height = math.ceil(self.cell_height / 2)

        self.cell_width = self.cell_size
        self.half_cell_width = math.ceil(self.cell_size / 2)

    def _get_column_text(self, row_data, default_row_text, is_middle_of_cell_height):
        row_content = ''
        for idx, data in enumerate(row_data):
            cell_content = default_row_text
            if data and is_middle_of_cell_height:
                cell_content = default_row_text[:(self.half_cell_width - 1)] + \
                    str(data) + default_row_text[self.half_cell_width:]

            border_right = ("‖" if (idx + 1) % 3 == 0 else "|")
            row_content += cell_content + border_right
        return row_content

    def _draw_columns_of_row(self, row, under_character, row_content_number):
        cell_height = math.ceil(self.cell_size / 2)
        for line in range(1, cell_height + 1):
            is_last_line = line == cell_height
            default_row_content = (
                under_character if is_last_line else " "
            ) * self.cell_width

            is_middle_of_cell_height = line == self.half_cell_height
            row_border_left = (
                str(row_content_number) if is_middle_of_cell_height else " "
            ) + "‖"

            row_content = self._get_column_text(
                row,
                default_row_content,
                is_middle_of_cell_height
            )

            print(row_border_left + row_content)

    def _draw_rows(self, game_data):
        for idx, content_row in enumerate(game_data):
            under_character = "‗" if (idx + 1) % 3 == 0 else "_"
            row_content_number = (idx + 1)
            self._draw_columns_of_row(
                content_row, under_character, row_content_number)

    def display_game(self, game_data):
        game_cell_length = len(game_data[0])

        column_border_up = "‗" * self.cell_size + " "
        print(" " * 2 + column_border_up * game_cell_length)

        self._draw_rows(game_data)

        column_footer = [
            " " * (self.half_cell_width - 1) + str(i + 1) +
            " " * (self.cell_size - self.half_cell_width)
            for i in range(game_cell_length)
        ]

        print(" " * 2 + " ".join(column_footer))

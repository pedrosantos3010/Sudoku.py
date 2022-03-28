import math
import random

from game_input import Cell


class LevelGenerator:
    def create_level(self):

        self.level = [[0 for i in range(9)] for i in range(9)]
        self.possible_values_per_cell = self._create_all_possible_values()

        for row in range(9):
            for column in range(9):
                if self.level[row][column] != 0:
                    continue

                possible_numbers = self.possible_values_per_cell[row][column]
                random_index = random.randrange(len(possible_numbers))
                number = possible_numbers.pop(random_index)
                self.level[row][column] = number
                self.possible_values_per_cell[row][column] = []

                self._update_all_related_cells(
                    row,
                    column,
                    number
                )

        return self.level

    def get_hints(self, number):
        cells = [
            Cell(i, j, self.level[i][j])
            for i in range(9)
            for j in range(9)
        ]
        randomCell = [
            cells.pop(random.randrange(len(cells)))
            for i in range(number)
        ]
        return randomCell

    def _remove_possible_value_from(self, row, column, value_to_remove):
        if self.level[row][column] != 0:
            return

        if value_to_remove not in self.possible_values_per_cell[row][column]:
            return

        current_cell_possible_values = self.possible_values_per_cell[row][column]
        current_cell_possible_values.remove(value_to_remove)
        if len(current_cell_possible_values) == 1:
            only_value_possible = current_cell_possible_values.pop()
            self.level[row][column] = only_value_possible
            self._update_all_related_cells(row, column, only_value_possible)

    def _update_all_related_cells(self, row, column, value_to_remove):

        self._update_all_related_rows(column, value_to_remove)
        self._update_all_related_columns(row, value_to_remove)
        self._update_all_related_quadrant_cells(row, column, value_to_remove)

    def _update_all_related_rows(self, column, value_to_remove):
        for row in range(9):
            self._remove_possible_value_from(row, column, value_to_remove)

    def _update_all_related_columns(self, row, value_to_remove):
        for column in range(9):
            self._remove_possible_value_from(row, column, value_to_remove)

    def _update_all_related_quadrant_cells(self, row, column, value_to_remove):
        min_row = self._get_min_index_of_quadrant(row)
        min_column = self._get_min_index_of_quadrant(column)

        for current_row in range(min_row, min_row + 3):
            for current_column in range(min_column, min_column + 3):
                if current_row == row or current_column == column:
                    continue

                self._remove_possible_value_from(
                    current_row,
                    current_column,
                    value_to_remove
                )

    def _get_min_index_of_quadrant(self, row_or_column_index):
        return (math.ceil((row_or_column_index + 1) / 3) - 1) * 3

    def _create_all_possible_values(self):
        return [[[v for v in range(1, 10)] for i in range(9)] for j in range(9)]

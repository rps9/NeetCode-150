class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [{}, {}, {}, {}, {}, {}, {}, {}, {}] 
        columns = [{}, {}, {}, {}, {}, {}, {}, {}, {}] 
        # Easier to find what cell you're in when you divide the three by threes into x and y rather than give them each a specific value
        three_by_threes = [[{}, {}, {}], 
                           [{}, {}, {}], 
                           [{}, {}, {}]] 

        # Try all of the cases, return false if there is multiple in any hash
        for row_number in range(9):
            for column_number in range(9):
                cell_value = board[row_number][column_number]
                if cell_value != '.':
                    x_coord = int(column_number / 3)
                    y_coord = int(row_number / 3)
                    
                    try:
                        rows[row_number][cell_value] += 1
                        return False
                    except:
                        rows[row_number][cell_value] = 1
                    try:
                        columns[column_number][cell_value] += 1
                        return False
                    except:
                        columns[column_number][cell_value] = 1
                    try:
                        three_by_threes[y_coord][x_coord][cell_value] += 1
                        return False
                    except:
                        three_by_threes[y_coord][x_coord][cell_value] = 1

        return True

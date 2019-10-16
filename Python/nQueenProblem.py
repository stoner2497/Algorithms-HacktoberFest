def put_queen(self,positions,target_row):
    if target_row == self.size:
        self.show_full_board(positions)
        self.solutions += 1
    else:
        for column in range(self.size):
            if self.check_place(positions,target_row,column):
                positions[target_row] = column
                self.put_queen(positions,target_row + 1)
def check_place(self,positions,occupied_row,column):
    for i in range(occupied_row):
        if positions[i] == column or/
           positions[i] - i == column - occupied_row or/
           positions[i] + i == column + occupied_row:
        return False
    return True
def show_full_board(self,positions):
    for row in range(self.size):
        line=""
        for column in range(self.size):
            if positions[row] == column:
                line += "Q"
            else:
                line += "."
            print(line)
        print("/n")
def main():
    NQueens(8)

if __name__ == "__main__":
    main()
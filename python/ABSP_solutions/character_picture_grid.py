# sample grid for testing:
# grid = [['.', '.', '.', '.', '.', '.'],
#         ['.', 'O', 'O', '.', '.', '.'],
#         ['O', 'O', 'O', 'O', '.', '.'],
#         ['O', 'O', 'O', 'O', 'O', '.'],
#         ['.', 'O', 'O', 'O', 'O', 'O'],
#         ['O', 'O', 'O', 'O', 'O', '.'],
#         ['O', 'O', 'O', 'O', '.', '.'],
#         ['.', 'O', 'O', '.', '.', '.'],
#         ['.', '.', '.', '.', '.', '.']]

def character_picture_grid(grid):
    x_len=len(grid)
    y_len=len(grid[0])
    transposed=[[' ' for _ in range(x_len)] for _  in range(y_len)]
    for x in range(x_len):
        for y in range(y_len):
            transposed[y][x]=grid[x][y]
    for row in transposed:
        print(''.join(row))


def main():
    grid=[]
    print("Enter the character picture grid row by row.")
    
    # take input for the number of rows and columns
    while True:
        try:
            rows,cols = map(int, input("Enter the number of rows and columns separated by space: ").split(" "))
            if rows<=0 or cols<=0:
                print("Please enter positive integers for rows and columns.")
                continue
            break
        except ValueError:
            print("Please enter valid integers for rows and columns.")

    while True:
        row_values=input(f"Enter row {len(grid)+1} (values should be separacted by space): ").split(" ")
        if len(row_values)!=cols:
            print("Please enter the correct number of values for the row.")
            continue
        grid.append(row_values)
        if(len(grid)==rows):
            print("\nAll rows entered successfully.\n")
            break


    character_picture_grid(grid)

    

if __name__=="__main__":
    main()
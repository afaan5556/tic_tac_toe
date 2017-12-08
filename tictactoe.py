'''
PSUEDOCODE
Display new board
Loop (up to) 9 times
	Ask user for input
	Various checks on user input (between 1 and 9, spot free or not)
		Ask for input again if checks fail
	Convert input into alternating x or o
	Update board
	Check for winner
		Winner message
		break
	Display new board
Display tie message

PSUEDOCODE WITH FUNCTION LIST
0. Display a new board
Loop
	1. Get user input
	2.1 Check user input for 1 through 9 only TODO: Also check if it is an int and not say, a string
	2.2 Check board to see if user entered spot is free or not
	3. Alternate user input to place x then o then x then o
	4. Update borad
	5. Check board for winner 
	6. Display current board
X. Master function that runs other functions in order

And finally....call the master function
'''

# CONSTANTS
#1 MAP BOARD STRING INDEX TO BOARD LIST INDEX
board_position = {1:0, 3:1, 5:2, 8:3, 10:4, 12:5, 15:6, 17:7, 19:8}
#2 MAP BOARD LIST INDEX TO BOARD STRING INDEX
position_board = {1:1, 2:3, 3:5, 4:8, 5:10, 6:12, 7:15, 8:17, 9:19}
#3 MAP BOARD GRID INDEX TO BOARD STRING INDEX
board_grid = {1:0, 2:2, 3:4, 4:6 , 5:7 , 6:9 , 7:11 , 8:13 , 9:14 , 10:16 , 11:18 , 12:20}
#4 STARTING NUMBERED BOARD LIST
board_list = list(i for i in range(1, 10))
#5 WINNING COMBINATIONS GIVEN BOARD LIST STRUCTURE
winning_combos = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

#0 DISPLAY NEW BOARD
def board_display(list_board, dict_board_position, dict_board_grid):
	board_string = ''
	for i in range(3):
		for j in range(7):
			if j in dict_board_grid.values():
				board_string += '|'
			else:
				board_string += str(list_board[dict_board_position[7*i + j]])
		board_string += '\n'
	print(board_string)

#1 GET USER INPUT
def get_input(player):
	user_input = int((input('Player %s enter number corresponding to where you want to place your move:' %player)))
	return user_input

#2.1 CHECK USER INPUT FOR 1 THROUGH 9 ONLY
def check_input(user_input):
	if user_input < 1 or user_input > 9:
		print('###### Invalid entry. Please enter between 1 and 9 ######')
		return False
	return True

#2.2 CHECK BOARD TO SEE IF USER INPUT SPOT IS FREE OR NOT 
def check_free(list_board, dict_position_board, dict_board_position, int_user_input):
	if list_board[dict_board_position[dict_position_board[int_user_input]]] == 'x' or list_board[dict_board_position[dict_position_board[int_user_input]]] == 'o':
		print('###### That spot is already taken. Pick a free spot ######')
		return False
	else:
		return True

#3 ALTERNATE USER INPUT FROM X TO O TO X TO O
def alternate_turns(count):
	if count % 2 == 0:
		return 'o'
	else:
		return 'x'

#4 UPDATE BOARD
def update_board(list_board, int_user_input, turn, dict_position_board):
	if turn == 'x':
		list_board[int_user_input - 1] = 'x'
	else:
		list_board[int_user_input - 1] = 'o'
	return list_board

#5 CHECK BOARD FOR WINNER
def check_winner(list_board, list_winning_combos):
	for i in list_winning_combos:
		string_check = ''
		for j in i:
			string_check += str(list_board[j])
		if string_check == 'xxx' or string_check == 'ooo':
			return string_check[0]
	return True

# MASTER FUNCTION THAT RUNS OTHER FUNCTIONS IN ORDER
def run_game(list_board, dict_position_board, dict_board_position, dict_board_grid, list_winning_combos):
	turn_count = 1
	while turn_count <= 9:
		turn = alternate_turns(turn_count)
		board_display(list_board, dict_board_position, dict_board_grid)
		user_input = get_input(turn)
		if check_input(user_input) and check_free(list_board, dict_position_board, dict_board_position, user_input):
			list_board = update_board(list_board, user_input, turn, dict_position_board)
			if check_winner(list_board, list_winning_combos) == True:
				turn_count += 1
			else:
				print('>>>>>>>>%s wins<<<<<<<<' %check_winner(list_board, list_winning_combos))
				board_display(list_board, dict_board_position, dict_board_grid)
				return
	board_display(list_board, dict_board_position, dict_board_grid)
	print('Game was a tie!')

# CALL MASTER FUNCTION
run_game(board_list, position_board, board_position, board_grid, winning_combos)
import random
def print_board(array_of_choices = []):
    print("-------------------------")
    print(f"|  {array_of_choices[0]}  |  {array_of_choices[1]}  |  {array_of_choices[2]}  |  {array_of_choices[3]}  |")
    print("-------------------------")
    print(f"|  {array_of_choices[4]}  |  {array_of_choices[5]}  |  {array_of_choices[6]}  |  {array_of_choices[7]}  |")
    print("-------------------------")
    print(f"|  {array_of_choices[8]}  |  {array_of_choices[9]} | {array_of_choices[10]}  |  {array_of_choices[11]} |")
    print("-------------------------")
    print(f"|  {array_of_choices[12]} |  {array_of_choices[13]} | {array_of_choices[14]}  |  {array_of_choices[15]} |")
    print("-------------------------")

def check_winner(array_of_the_player = []):
    player_start_index = 0
    isWinner = False
    array_of_the_player_length = len(array_of_the_player)
    array_of_combination_choices_length = len(combination_choices)
    if(len(array_of_the_player) == 3):
        combination_start_index = 0
        while combination_start_index < 4:
            # print(f"I reached here=={combination_start_index}")
            current_array_in_combination_choices = combination_choices[combination_start_index]
            # print(f"This is current array {current_array_in_combination_choices}")
            item_ocurrence = 0
            for index in range(3):#index of individual array in array of combination_choice
                for player_start_index in range(array_of_the_player_length):
                    # print(f"current array {current_array_in_combination_choices[combination_start_index]}")
                    if array_of_the_player[player_start_index] == current_array_in_combination_choices[index]:
                        item_ocurrence +=1
                        break
            if(item_ocurrence == 3):
                isWinner = True
                return isWinner

            combination_start_index +=1
        return isWinner
    elif(len(array_of_the_player) >= 4):
        combination_start_index = 4
        while combination_start_index < array_of_combination_choices_length:
            # print(f"I reached here=={combination_start_index}")
            current_array_in_combination_choices = combination_choices[combination_start_index]
            # print(f"This is current array {current_array_in_combination_choices}")
            item_ocurrence = 0
            for index in range(4):#index of individual array in array of combination_choice
                for player_start_index in range(array_of_the_player_length):
                    # print(f"current array {current_array_in_combination_choices[combination_start_index]}")
                    if array_of_the_player[player_start_index] == current_array_in_combination_choices[index]:
                        item_ocurrence +=1
                        break
            if(item_ocurrence == 4):
                isWinner = True
                return isWinner

            combination_start_index +=1
        return isWinner
    else:
        return isWinner

     
if __name__ == "__main__":
    combination_choices = [[2, 7, 12],[3, 6, 9],[5, 10, 15]
,[8, 11, 14], [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16], [1, 5,
9, 13], [2, 6, 10, 14], [3, 7, 11, 15], [4, 8, 12, 16], [1, 6, 11, 16], [4, 7, 10, 13]]
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    moves_counter = 0
    next_player = "p" # c for computer p for player
    computer_moves_array = [] #computer choices
    player_moves_array = [] #player choices
    remaining_choices_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    array_of_choices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    isWinnerFound = False
    while(moves_counter < 16):
        if next_player == 'p':
            print_board(array_of_choices)
            while True:
                data = int(input(f"Please choose a number among the following list {remaining_choices_array} :\n"))
                if(remaining_choices_array.count(data) > 0):#check if the input exist in remaining choices array
                    player_moves_array.append(data) #append the player choice in player moves array
                    index = remaining_choices_array.index(data) #find index of item the player chose in the remaining choice array
                    array_of_choices[data-1] = "O" # Replace the number with O in array of choices
                    del remaining_choices_array[index] #remove the input selected in remaining choices
                    break
            if(check_winner(player_moves_array)): #check in the player has one of the combination to succeed
                isWinnerFound = True
                break
            next_player = 'c' #switch to computer turn
            moves_counter += 1
        else:
            rand_item  = random.choice(remaining_choices_array) #computer choose one item in remaining choices
            computer_moves_array.append(rand_item) #add the random item chose by a computer into computer moves array
            index = remaining_choices_array.index(rand_item) #find index of item the computer chose in the remaining choice array
            array_of_choices[rand_item-1] = "X" # Replace the number with X in array of choices
            del remaining_choices_array[index] #remove the chosen input selected in remaining choices
            if(check_winner(computer_moves_array)): #check in the player has one of the combination to succeed
                isWinnerFound = True
                break
            next_player = 'p' #switch to player turn
            moves_counter += 1   
    if(next_player == 'p' and isWinnerFound):
        print("Player won the game")
    elif(next_player == 'c' and isWinnerFound):
        print("Computer won the game")
    else: print("It's a tie")
    print_board(array_of_choices)
        
                       
            
                
                
    

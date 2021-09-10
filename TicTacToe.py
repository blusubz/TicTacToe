# This is a 2 player TicTacToe game. 

def instructions():
    print("\nEste es un juego de TicTacToe. Cada jugador tiene un turno por movimiento.")
    print("Los jugadores X y O se turnan para marcar los espacios vacíos del tablero 3x3.")
    print("El primer jugador que obtenga tres del mismo símbolo seguidos en cualquier")
    print("dirección - horizontal, vertical o diagonalmente - gana el juego.\n")

    
    print("Las posibles posiciones de entrada se muestran a continuación.\n")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 \n")

    print("Empezar juego")
    clear_board()
    

def position_choice(row):
    # Input Validation
    position = "false"

    if row == 1:
        while position.isdigit() == False:
            position = input("Ingrese una posición 1 - 3: ")

            if position.isdigit() == False:
                print("Asegúrese de ingresar un dígito real.")

            if position.isdigit() == True:
                position = int(position)
                if position < 1 or position > 3:
                    print("Asegúrese de ingresar una posición en el rango 1 - 3.")
                    position = "false"
            position = str(position)

    if row == 2:
        while position.isdigit() == False:
            position = input("Ingrese una posición 4 - 6: ")

            if position.isdigit() == False:
                print("Asegúrese de ingresar un dígito real.")

            if position.isdigit() == True:
                position = int(position)
                if position < 4 or position > 6:
                    print("Asegúrese de ingresar una posición en el rango 4 - 6.")
                    position = "false"
            position = str(position)

    if row == 3:
        while position.isdigit() == False:
            position = input("Ingrese una posición 7 - 9: ")

            if position.isdigit() == False:
                print("Asegúrese de ingresar un dígito real.")

            if position.isdigit() == True:
                position = int(position)
                if position < 7 or position > 9:
                    print("Asegúrese de ingresar una posición en el rango 7 - 9.")
                    position = "false"
            position = str(position)
    
    return int(position)

def row_choice():
    # Input Validation

    row = "false"

    while row.isdigit() == False:
        row = input("\nIngrese una fila 1 - 3: ")

        if row.isdigit() == False:
            print("\nAsegúrese de ingresar un dígito real.")

        if row.isdigit() == True:
            row = int(row)
            if row < 1 or row > 3:
                print("\nAsegúrese de ingresar una fila en el rango 1 - 3.")
                row = "false"
        row = str(row)
    
    return int(row)


def replacement_choice(game_list_row1, game_list_row2, game_list_row3, position, row):
    user_placement = 'false'
    while user_placement != 'X' or user_placement != 'O':
        user_placement = input("Escriba su pieza (X u O) para colocarla en la posición: ")
        user_placement = user_placement.upper()

        if user_placement == 'X' or user_placement == 'O':
            break

        if user_placement != 'X' or user_placement != 'O':
            print("Introduzca la pieza correspondiente.")

    if row == 1:
        game_list_row1[position - 1] = user_placement
        return game_list_row1
    if row == 2:
        if position == 4:
            position = 1
        elif position == 5:
            position = 2
        else:
            position = 3
        game_list_row2[position - 1] = user_placement
        return game_list_row2
    if row == 3:
        if position == 7:
            position = 1
        elif position == 8:
            position = 2
        else:
            position = 3
        game_list_row3[position - 1] = user_placement
        return game_list_row3
    
    
# try the board as a string ???
def display_gameboard(game_list_row1, game_list_row2, game_list_row3):
    print(f" {game_list_row1[0]} | {game_list_row1[1]} | {game_list_row1[2]} ")
    print("---+---+---")
    print(f" {game_list_row2[0]} | {game_list_row2[1]} | {game_list_row2[2]} ")
    print("---+---+---")
    print(f" {game_list_row3[0]} | {game_list_row3[1]} | {game_list_row3[2]} ")

def game_on_choice():
    continue_playing = 'no'
    
    while continue_playing not in ['SI','NO']:
        continue_playing = input("\nSigue jugando (Si o No):")
        continue_playing = continue_playing.upper()
        if continue_playing not in ['SI','NO']:
            print("Lo siento, elija Si o No.")
    if continue_playing == "SI":
        clear_board()
        return True
    else:
        print("\nGracias por jugar.\n")
        return False
    
def game_logic(game_list_row1, game_list_row2, game_list_row3):

    # CHECK PLAYER X WINNER 

    # Horizontal 
    if game_list_row1[0] == 'X' and game_list_row1[1] == 'X' and game_list_row1[2] == 'X':
        print("\n¡Felicidades X, tú ganas!")
        return True
    if game_list_row2[0] == 'X' and game_list_row2[1] == 'X' and game_list_row2[2] == 'X':
        print("\n¡Felicidades X, tú ganas!")
        return True
    if game_list_row3[0] == 'X' and game_list_row3[1] == 'X' and game_list_row3[2] == 'X':
        print("\n¡Felicidades X, tú ganas!")
        return True

    # Vertical
    if game_list_row1[0] == 'X' and game_list_row2[0] == 'X' and game_list_row3[0] == 'X':
        print("\n¡Felicidades X, tú ganas!")
        return True
    if game_list_row1[1] == 'X' and game_list_row2[1] == 'X' and game_list_row3[1] == 'X':
        print("\n¡Felicidades X, tú ganas!")
        return True
    if game_list_row1[2] == 'X' and game_list_row2[2] == 'X' and game_list_row3[2] == 'X':
        print("\n¡Felicidades X, tú ganas!")
        return True

    # Diagonal 
    if game_list_row1[0] == 'X' and game_list_row2[1] == 'X' and game_list_row3[2] == 'X':
        print("\n¡Felicidades X, tú ganas!")
        return True
    if game_list_row1[2] == 'X' and game_list_row2[1] == 'X' and game_list_row3[0] == 'X':
        print("\n¡Felicidades X, tú ganas!")
        return True

    # CHECK PLAYER O WINNER 

    # Horizontal 
    if game_list_row1[0] == 'O' and game_list_row1[1] == 'O' and game_list_row1[2] == 'O':
        print("\n¡Felicidades O, tú ganas!")
        return True
    if game_list_row2[0] == 'O' and game_list_row2[1] == 'O' and game_list_row2[2] == 'O':
        print("\n¡Felicidades O, tú ganas!")
        return True
    if game_list_row3[0] == 'O' and game_list_row3[1] == 'O' and game_list_row3[2] == 'O':
        print("\n¡Felicidades O, tú ganas!")
        return True

    # Vertical
    if game_list_row1[0] == 'O' and game_list_row2[0] == 'O' and game_list_row3[0] == 'O':
        print("\n¡Felicidades O, tú ganas!")
        return True
    if game_list_row1[1] == 'O' and game_list_row2[1] == 'O' and game_list_row3[1] == 'O':
        print("\n¡Felicidades O, tú ganas!")
        return True
    if game_list_row1[2] == 'O' and game_list_row2[2] == 'O' and game_list_row3[2] == 'O':
        print("\n¡Felicidades O, tú ganas!")
        return True

    # Diagonal 
    if game_list_row1[0] == 'O' and game_list_row2[1] == 'O' and game_list_row3[2] == 'O':
        print("\n¡Felicidades O, tú ganas!")
        return True
    if game_list_row1[2] == 'O' and game_list_row2[1] == 'O' and game_list_row3[0] == 'O':
        print("\n¡Felicidades O, tú ganas!")
        return True

def clear_board():
    print("\n   |   |   ")
    print("---+---+---")
    print("   |   |   ")
    print("---+---+---")
    print("   |   |   \n")

def main():
    instructions()
    game_on = True
    game_list_row1 = [' ',' ',' ']
    game_list_row2 = [' ',' ',' ']
    game_list_row3 = [' ',' ',' ']
    prev_pos = -1
    total_moves = 0

    while game_on:

        if total_moves >= 9:
            print("\nEl juego termina en empate.")
            if game_on_choice() == True:
                # clear_board
                game_list_row1 = [' ',' ',' ']
                game_list_row2 = [' ',' ',' ']
                game_list_row3 = [' ',' ',' ']
                total_moves = 0
                prev_pos = -1
                continue
            else:
                break
        
        # GAME START
        row = row_choice()
        position = position_choice(row)
        # Validate the position ! can't place an X or O into occupied position!
        if position == prev_pos:
            print("\n¡Esta posición ya está ocupada!")
            print("Ingrese una nueva posición disponible.\n")
            #prev_pos = position
            continue
        prev_pos = position
        
        replacement_choice(game_list_row1, game_list_row2, game_list_row3, position, row)
        print()
        display_gameboard(game_list_row1, game_list_row2, game_list_row3)

        total_moves += 1

        game_finished = game_logic(game_list_row1, game_list_row2, game_list_row3)

        if game_finished == True:
            #clear_board
            game_list_row1 = [' ',' ',' ']
            game_list_row2 = [' ',' ',' ']
            game_list_row3 = [' ',' ',' ']
            game_on = game_on_choice()
            total_moves = 0
            prev_pos = -1

        if total_moves >= 1 and total_moves < 9 and game_finished == False:
            print("\nSiguiente jugador gire.\n")
            
main()
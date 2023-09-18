import os
import textwrap
import entities.BoardGames as BoardGames
import entities.Options as Options
import controllers.ConnectorBD as Connector
from dao.BoardQueries import BoardQueries

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_user_input():
	elements = input("Insert on the following order, separated by comma: name,rank,rating,complexity,maxplayers,style\n")
	elements = elements.split(",")

	if len(elements) != 6:
		print("Invalid input. Please provide all six values separated by commas.")
	else:
		name = elements[0].strip()  
		rank = int(elements[1])
		rating = float(elements[2])
		complexity = float(elements[3])
		max_players = int(elements[4])
		style = elements[5].strip()  
	return elements


def main(connector: Connector):
    while(True):

        menu_text = textwrap.dedent("""\
			Welcome to the Board Games Program!
			Select what you want to do:
              
				1- Board Games List,
				2- Add Board Game,             
				3- Import Board Games from JSON,
				4- Delete Board Games,
				5- Exit Program
            """)
        print(menu_text)
        
        try:
            option = int(input("Select your option: "))
        except:
            input("Invalid Option. You need to choose a number. Press Enter to go back to Menu")
            continue
        finally:
            clear()
            
        if option < 1 or option > 6:
            print("Invalid number")

        elif option == Options.MenuPrincipal.BOARD_LIST:
            BoardQueries.get_table_elements(connector,"BoardGames")
            
        elif option == Options.MenuPrincipal.BOARD_ADD:
            BoardQueries.add_table_elements(connector, get_user_input(),"BoardGames")
            
        elif option == Options.MenuPrincipal.BOARD_IMPORT_JSON:
            pass
        elif option == Options.MenuPrincipal.BOARD_DELETE:
            pass
        elif option == Options.MenuPrincipal.LEAVE:
            input("Good bye!!! Press enter to finish the program\n")
            clear()
            break
        input("Press Enter to go back to the main menu\n")
        clear()



if __name__ == "__main__":
    connector = Connector.Connector()
    main(connector)





import os
import textwrap
import entities.Options as Options
import controllers.ConnectorBD as Connector
from dao.BoardQueries import BoardQueries
from entities.BoardGames import BoardGames as BoardGames

def clear():
	os.system('cls' if os.name == 'nt' else 'clear')


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
			try:
				BoardQueries.get_table_elements(connector,"BoardGames")
			except Exception as e:
				print(e)

		elif option == Options.MenuPrincipal.BOARD_ADD:
			try:
				BoardQueries.add_table_elements(connector, BoardGames.get_user_input(),"BoardGames")
			except Exception as e:
				print(e)

		elif option == Options.MenuPrincipal.BOARD_IMPORT_JSON:
			board_instances_list = BoardGames.import_from_json()
			if len(board_instances_list)>0:
				for new_board in board_instances_list:
					BoardQueries.add_table_elements(connector, new_board,"BoardGames")

		elif option == Options.MenuPrincipal.BOARD_DELETE:
			try:
				BoardQueries.delete_element_by_name(connector, "BoardGames")
			except Exception as e:
				print(e)

		elif option == Options.MenuPrincipal.LEAVE:
			input("Good bye!!! Press enter to finish the program\n")
			clear()
			break
		input("Press Enter to go back to the main menu\n")
		
		clear()


#MoreFakeData.json
if __name__ == "__main__":
	connector = Connector.Connector()
	main(connector)





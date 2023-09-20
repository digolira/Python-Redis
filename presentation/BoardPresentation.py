from dao.BoardQueries import BoardQueries
from entities.BoardGames import BoardGames as BoardGames

class BoardPresentation:
		
	@classmethod
	def get_all_board_elements(cls, connector, table_name:str):
		print(f"Those are the Board Games saved in the List:\n")
		headers = ("ID", "Name","Rank", "Rating", "Complexity","Max Players", "Style")
		print(f'{headers[0].ljust(6)} | {headers[1].ljust(20)} | {headers[2].ljust(8)} | {headers[3].ljust(8)} |'\
				f' {headers[4].ljust(10)} | {headers[5].ljust(12)} | {headers[6]}')
		try:
			results = BoardQueries.get_table_elements(connector, table_name)
			if len(results)>0:
				for element in results:
						print(f'{str(element[0]).ljust(6)} | {element[1].ljust(20)} | {str(element[2]).ljust(8)} | {str(element[3]).ljust(8)} |'\
								f' {str(element[4]).ljust(10)} | {str(element[5]).ljust(12)} | {element[6]}')
		except Exception as e:
			print(e)

	@classmethod
	def get_user_input(cls,connector, table_name):
		elements = input("Insert new Board Game info separated by comma. Follow the order: name,rank,rating,complexity,maxplayers,style\n")
		elements = elements.split(",")
		if len(elements) != 6:
			return "Input should contain exactly 6 elements separated by commas." 
		try:
			new_board = BoardGames.generator_from_string_list(elements)
			BoardQueries.add_board_elements(connector, new_board, table_name)
			print(f"Board Game: {new_board.name} Added with Success")
		except Exception as e:
			print(e)

	@classmethod
	def delete_board_by_name(cls, connector, table_name: str):
		board_name = input("Insert Board Game Name: ")
		result = BoardQueries.find_board_by_name(connector, board_name, table_name)
		if result != None:
			opt = input("Board name: %s will be deleted. Press Y to confirm, any other key to leave.\n"%(result))
			if (opt.lower() == 'y'):
				try:
					BoardQueries.delete_board_by_name(connector,board_name, table_name)
					print("Delete done! ")
					return
				except Exception as e:
					print(e)
					input("Something wrong deleting data at the Database. Press enter to continue.")
			else:
				print("Ok, Delete operation aborted.")
				return
		else:
			return "Couldn't find this register. Press enter to continue"
		
	@classmethod
	def import_from_json(cls,connector, table_name, file_name=None):
		if file_name == None:
			file_name = input("Insert name of file\n *Remember that the file must be inside the data folder:\n")
		try:
			board_instances_list = BoardGames.import_from_json(file_name)
			if len(board_instances_list)>0:
				for new_board in board_instances_list:
					BoardQueries.add_board_elements(connector, new_board, table_name)
				print(f"{len(board_instances_list)} Board Games added with success")
			else:
				print("File not found or Empty")
		except Exception as e:
			print(e)

	



	

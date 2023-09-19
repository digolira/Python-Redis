from entities.BoardGames import BoardGames as BoardGames

class BoardQueries():
    def __init__(self):
        pass

    def __count_table_elements(connector, table_name: str):
        query = f'SELECT COUNT(*) from {table_name}'
        try:
            connector.mycursor.execute(query)            
            res = connector.mycursor.fetchone() 
            return res[0]
        except Exception as e:
            print(e) 

    def __find_element_by_name(connector, board_name, table_name: str):
        query = "SELECT * FROM %s WHERE name = '%s'"%(table_name,board_name.title())
        connector.mycursor.execute(query)
        res = connector.mycursor.fetchone()
        if res[0]== 0:
            print(f"BoardGame {board_name} not found")
            return None
        else:
            return res[1]

    @classmethod
    def get_table_elements(cls, connector, table_name:str):
        print(f"Those are the Board Games saved in the List:\n")
        if (cls.__count_table_elements(connector, table_name) > 0):
            query = f'SELECT * FROM {table_name}'
            try:
                connector.mycursor.execute(query)
                headers = ("ID", "Name","Rank", "Rating", "Complexity","Max Players", "Style")
                print(f'{headers[0].ljust(6)} | {headers[1].ljust(20)} | {headers[2].ljust(8)} | {headers[3].ljust(8)} |'\
                      f' {headers[4].ljust(10)} | {headers[5].ljust(12)} | {headers[6]}')
                for element in connector.mycursor:
                    print(f'{str(element[0]).ljust(6)} | {element[1].ljust(20)} | {str(element[2]).ljust(8)} | {str(element[3]).ljust(8)} |'\
                          f' {str(element[4]).ljust(10)} | {str(element[5]).ljust(12)} | {element[6]}')
            except Exception as e:
                print(e)
        else:
            print("No registers found.\n")

    @classmethod
    def add_table_elements(cls, connector, board_game: BoardGames, table_name:str):
        query = f'INSERT INTO {table_name}(name, `rank`, rating, complexity, max_players, style) VALUES ' \
                f'("{board_game.name}", {board_game.rank}, {board_game.rating}, {board_game.complexity}, {board_game.max_players}, "{board_game.style}")'
        try:
            connector.mycursor.execute(query)
            connector.db.commit()
            print("Board Game created.")
        except Exception as e:
            print(e)

    @classmethod
    def delete_element_by_name(cls, connector, table_name: str):
        board_name = input("Insert Board Game Name: ")
        result = cls.__find_element_by_name(connector, board_name, table_name)
        if result != None:
            opt = input("Board name: %s will be deleted. Press Y to confirm, any other key to leave.\n"%(result))
            if (opt.lower() == 'y'):
                try:
                    query = """
                    DELETE FROM %s
                    WHERE
                       name= '%s'
                    """ %(table_name, board_name)
                    connector.mycursor.execute(query)
                    connector.db.commit()
                    input("Delete done! Press enter to continue. ")
                except Exception as e:
                    print(e)
                    input("Something wrong deleting data at the Database. Press enter to continue.")
            else:
                return "Leaving. Press enter to continue"
        else:
            return input ("Couldn't find this register. Press enter to continue")
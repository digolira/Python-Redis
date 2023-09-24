from entities.BoardGames import BoardGames as BoardGames
from dao.GeneralQueries import GeneralQueries as GeneralQueries

class BoardQueries(GeneralQueries):
    def __init__(self):
        pass

    @classmethod
    def add_board_elements(cls, connector, board_game: BoardGames, table_name:str):
        super().check_legit_table_names(table_name)
        query = f'INSERT INTO {table_name}(name, `rank`, rating, complexity, max_players, style) VALUES (%s, %s, %s, %s, %s, %s)'
        values = (board_game.name, board_game.rank, board_game.rating, board_game.complexity, board_game.max_players, board_game.style)
        try:
            connector.mycursor.execute(query, values)
            connector.db.commit()
            return 
        except Exception as e:
            raise e

    @classmethod
    def find_board_by_name(cls, connector, board_name, table_name: str):
        super().check_legit_table_names(table_name)
        query = f"SELECT * FROM {table_name} WHERE name = %s"
        try:
            connector.mycursor.execute(query, (board_name.title(),))  #query ,  variables
            res = connector.mycursor.fetchall() 
            if res:
                return res[0][1]
            return None
        except Exception as e:
            raise e
        
    @classmethod
    def delete_board_by_name(cls, connector, board_name: str, table_name: str):
            super().check_legit_table_names(table_name)
            query = f'DELETE FROM {table_name} WHERE name = %s LIMIT 1'
            try:
                connector.mycursor.execute(query, (board_name.title(),))
                connector.db.commit()
                return
            except Exception as e:
                raise e


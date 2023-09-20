from entities.BoardGames import BoardGames as BoardGames
from dao.GeneralQueries import GeneralQueries as GeneralQueries

class BoardQueries(GeneralQueries):
    def __init__(self):
        pass

     
    @classmethod
    def add_board_elements(cls, connector, board_game: BoardGames, table_name:str):
        query = f'INSERT INTO {table_name}(name, `rank`, rating, complexity, max_players, style) VALUES ' \
                f'("{board_game.name}", {board_game.rank}, {board_game.rating}, {board_game.complexity}, {board_game.max_players}, "{board_game.style}")'
        try:
            connector.mycursor.execute(query)
            connector.db.commit()
            return 
        except Exception as e:
            raise e


    @classmethod
    def find_board_by_name(cls, connector, board_name, table_name: str):
        query = "SELECT * FROM %s WHERE name = '%s'"%(table_name,board_name.title())
        try:
            connector.mycursor.execute(query)
            res = connector.mycursor.fetchone()
            if res[0]== 0:
                return None
            else:
                return res[1]
        except Exception as e:
            raise e
        
    @classmethod
    def delete_board_by_name(cls, connector, board_name: str, table_name: str):
            query = """
                DELETE FROM %s
                WHERE
                    name= '%s'
                """ %(table_name, board_name)
            try:
                connector.mycursor.execute(query)
                connector.db.commit()
                return
            except Exception as e:
                raise e


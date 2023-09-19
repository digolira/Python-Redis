import json
import os

class BoardGames:
    def __init__(self, name: str, rank:int, rating: float, complexity: float, max_players: int, style: str):
        assert rank >= 0, f"Rank {rank} needs to be greater than or equal to zero!!"
        assert rating >= 0 and rating <= 10, f"Rating {rating} needs to be between 0-10!"
        assert complexity >= 0 and complexity <= 5, f"Complexity {complexity} needs to be in the range 0-5!"
        assert max_players > 0, f"You need to have at least one player"

        self.name = name
        self.rank = rank
        self.rating = rating
        self.complexity = complexity
        self.max_players = max_players
        self.style=style

    @classmethod
    def get_user_input(cls):
        elements = input("Insert new Board Game info separated by comma. Follow the order: name,rank,rating,complexity,maxplayers,style\n")
        elements = elements.split(",")
        if len(elements) != 6:
            return "Input should contain exactly 6 elements separated by commas."     
        try:
            new_board = BoardGames(
                name=elements[0].strip().title(),
                rank = int(elements[1]),
                rating = float(elements[2]),
                complexity = float(elements[3]),
                max_players = int(elements[4]),
                style = elements[5].strip()
            )
            return new_board
        except ValueError as e:
            return f"Error: {e}"
        
    @classmethod
    def import_from_json(cls, file_name=None):
        if file_name is None:
            file_name = input("Insert name of file\n *Remember that the file must be inside the data folder:\n")
        class_dir = os.path.dirname(os.path.abspath(__file__)) 
        json_dir = os.path.abspath(os.path.join(class_dir, '..', 'data'))
        json_file_path = os.path.join(json_dir, file_name) 

        try:
            with open(json_file_path, 'r') as file:
                data = json.load(file)

            board_instances_list = []
            for item in data:
                new_board = cls(
                    name=item['name'],
                    rank=item['rank'],
                    rating=item['rating'],
                    complexity=item['complexity'],
                    max_players=item['max_players'],
                    style=item['style']
                )
                board_instances_list.append(new_board)             
            return board_instances_list
        except FileNotFoundError:
            print(f"File '{file_name}' not found.")
            return []

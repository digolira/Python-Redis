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
            newBoard = BoardGames(
                name=elements[0].strip().title(),
                rank = int(elements[1]),
                rating = float(elements[2]),
                complexity = float(elements[3]),
                max_players = int(elements[4]),
                style = elements[5].strip()
            )
            return newBoard
        except ValueError as e:
            return f"Error: {e}"

class BoardGames:
    def __init__(self, name: str, rank:int, rating: float, complexity: float, max_players: int, style: str):
        # Validations
        assert rank >= 0, f"Rank {rank} needs to be greater than or equal to zero!!"
        assert rating >= 0 and rating <= 10, f"Rating {rating} needs to be between 0-10!"
        assert complexity >= 0 and complexity <= 5, f"Complexity {complexity} needs to be in the range 0-5!"

        # Assigning
        self.name = name
        self.rank = rank
        self.rating = rating
        self.complexity = complexity
        self.max_players = max_players
        self.style=style



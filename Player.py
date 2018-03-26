"""Player class: all the information available on the player"""
from typing import Iterable


class Player:
    def __init__(self, name: str, title, rating: int, rating_type, tie_breaks: Iterable, score=0):
        self.pairing_number = None
        self.name = name
        self.title = title
        self.rating = rating
        self.rating_type = rating_type
        self.score = score
        self.tie_breaks = list(tie_breaks)
    
    def __repr__(self):
        return f"{self.title if self.title else ' '} {self.name}\t#{self.pairing_number}\t{self.rating}\t{self.rating_type}" \
               f"{self.score} pts\t{self.tie_breaks}"


class DutchPlayer(Player):
    def __init__(self, name: str, title, rating: int, rating_type, tie_breaks: Iterable, score=0, float_status=None,
                 opponents=None, colour_history=None):
        super().__init__(name, title, rating, rating_type, tie_breaks, score)
        
        self.float_status = float_status
        self.opponents = list(opponents) if opponents is not None else list()
        self.colour_history = list(colour_history) if colour_history is not None else list()
    
    def __repr__(self):
        return super().__repr__() + f'\t{self.score} pts\t{self.float_status}\t{self.opponents}\t{self.colour_history}'

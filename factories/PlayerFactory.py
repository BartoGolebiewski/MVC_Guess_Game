from model.Player import Player


class PlayerFactory():
    def __init__(self):
        pass

    def create(self, name, score_point, lifes, account, temp_point) -> Player:
        return Player(
            name=name,
            score_point=score_point,
            lifes=lifes,
            account=account,
            temp_point=temp_point
        )

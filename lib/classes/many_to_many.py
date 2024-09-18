class Game:
    def __init__(self, title):
        self.title = title
        self._results = []

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self,title):
        if isinstance (title,str) and len(title) > 0:
            self._title=title


    def results(self):
        return [result for result in Result.all if result.game == self]

    def players(self):
        return list({result.player for result in self.results()})
        

    def average_score(self, player):
        scores = [result.score for result in self.results() if result.player == player]
        if scores:
            return sum(scores) / len(scores)
        return None

        pass

class Player:
    def __init__(self, username):
        self.username = username
        self._results = [] 

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self,username):
        if isinstance(username,str) and 2 <= len(username) <= 16:
            self._username=username
        # else:
        #     raise ValueError("Name must be a string between 2 and 16 characters.")


    def results(self):
        return [result for result in Result.all if result._player == self]
        pass

    def games_played(self):
        return list({result.game for result in self.results()})
        pass

    def played_game(self, game):
        return any(result.game == game for result in self.results())

        pass

    def num_times_played(self, game):
        return sum(1 for result in self.results() if result.game == game)

        pass

class Result:

    all = []

    def __init__(self, player, game, score):
        self._player = player
        self._game = game
        self._score = score
        Result.all.append(self)

    @property
    def player(self):
        return self._player
    
    @property
    def game(self):
        return self._game
    
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self,value):
        if isinstance(value,(int,len())) and  (1 <= value<= 5000):
            self._score=value
        else:
            raise ValueError("Score must be an integer between 1 and 5000.")
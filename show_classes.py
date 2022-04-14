class Show:
    def __init__(self, name, episodes, length, start_year, end_year, genre, status):
        self.name = name
        self.episodes = episodes
        self.length = length
        self.start_year = start_year
        self.end_year = end_year
        self.genre = genre
        self.status = status

    def new_show(self):

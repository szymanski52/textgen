from pymongo import MongoClient


class Player():
	def __init__(self, rank, name, age, elo, elo_hard, elo_clay, elo_grass, peak_age, peak_elo):
		self.rank = rank
		self.name = name
		self.age = age
		self.elo = elo
		self.elo_hard = elo_hard
		self.elo_clay = elo_clay
		self.elo_grass = elo_grass
		self.peak_age = peak_age
		self.peak_elo = peak_elo
		client = MongoClient()
		db = client['capper']
		inf = {
			   'rank': rank, 
			   'name': name, 
			   'age': age, 
			   'elo': elo, 
			   'elo_hard': elo_hard, 
			   'elo_clay': elo_clay, 
			   'elo_grass': elo_grass, 
			   'peak_age': peak_age, 
			   'peak_elo': peak_elo
			  }
		players = db.players
		players.insert(inf)

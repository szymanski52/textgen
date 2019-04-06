# coding: utf-8
from player import Player
from bs4 import BeautifulSoup
from urllib.request import urlopen


'''class tennis_parser():
	def __init__(self, arg):
		super(tennis_parser, self).__init__()
		self.arg = arg


	def get_soup_html(url):
		response = requests.get(url)
		soup = BeautifulSoup(response.text, 'lxml')
		return soup


	def get_main_table_data(data_file_name, url):
		stats = list()
		full_file_name = data_file_name + '.txt'
		file = open(full_file_name, 'w')
		file.write('rank@player@age@elo@elo_hard@elo_clay@elo_grass@peak_elo\n')
		player_pull_soup_html = tennis_parser.get_soup_html(url)
		table_tds = player_pull_soup_html.find_all('td')
		k = 0
		for i in table_tds[6:]:
			stats.append(i.text)
			k += 1
			if k==12:
				k = 0
				file.write('%s@%s@%s@%s@%s@%s@%s\n' % (stats[0],stats[1],stats[2],stats[4],stats[5],stats[6],stats[10]))
		file.close()


	def parse_main_table():
		tennis_parser.get_main_table_data('atp_main_players_table', 'http://tennisabstract.com/reports/atp_elo_ratings.html')
		tennis_parser.get_main_table_data('wtp_main_players_table', 'http://tennisabstract.com/reports/atp_wta_ratings.html')
'''

class Parser():
	def __init__(self):
		pass


	def get_soup(url):
		response = urlopen(url)
		soup = BeautifulSoup(response, 'html.parser')
		return soup


	def parse_elo(self):
		stats = list()
		atp_file = open('atp_elo.txt', 'w')
		wta_file = open('wta_elo.txt', 'w')
		atp_soup = Parser.get_soup('http://tennisabstract.com/reports/atp_elo_ratings.html')
		atp_tds = atp_soup.find_all('td')
		wta_soup = Parser.get_soup('http://tennisabstract.com/reports/wta_elo_ratings.html')
		wta_tds = wta_soup.find_all('td')
		k = 0
		for i in atp_tds[6:]:
			stats.append(i.text)
			k += 1
			if k == 12:
				k = 0
				Player(stats[0],
					   stats[1],
					   stats[2],
					   stats[3],
					   stats[5],
					   stats[6],
					   stats[7],
					   stats[10],
				   	   stats[11])
				stats = list()
		k = 0
		for i in wta_tds[6:]:
			stats.append(i.text)
			k += 1
			if k == 12:
				k = 0
				Player(stats[0],
					   stats[1],
					   stats[2],
					   stats[3],
					   stats[5],
					   stats[6],
					   stats[7],
					   stats[10],
					   stats[11])
				stats = list()


if __name__ == '__main__':
	parser = Parser()
	parser.parse_elo()
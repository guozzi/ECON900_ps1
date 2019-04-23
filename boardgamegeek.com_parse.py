from bs4 import BeautifulSoup
import os
import glob
import pandas as pd

if not os.path.exists("parsed_files"):
	os.mkdir("parsed_files")

df = pd.DataFrame()

for one_file_name in glob.glob("html_files/*.html"):
	print("parsing " + one_file_name)
	Parsed_From = os.path.basename(one_file_name) 
	f = open(one_file_name, "r", encoding = 'utf-8')
	soup = BeautifulSoup(f.read(), 'html.parser')
	f.close()
	game_rows = soup.find_all("tr", {"id": "row_"})
	
	for r in game_rows:
		Rank = r.find("td", {"class": "collection_rank"}).text
		Name = r.find("td", {"class": "collection_objectname"}).text
		Geek_Rating = r.find("td", {"class": "collection_bggrating"}).text
		Avg_Rating = r.find("td", {"class": "collection_bggrating"}).find_next_sibling("td").text
		Votes = r.find("td", {"class": "collection_bggrating"}).find_next_sibling("td").find_next_sibling("td").text



		df = df.append({
			'Parsed_From': Parsed_From, # Indicates the corresponding html file 
			'Rank': Rank, # Overall rank of the game, N/A means not ranked
			'Name': Name, # Name of the game
			'Geek_Rating': Geek_Rating, # Rating given by boardgamegeek.com
			'Avg_Rating': Avg_Rating, # Average rating given by users
			'Votes': Votes # Total user votes
			}, ignore_index=True)




df.to_csv("parsed_files/boardgamegeek_dataset.csv")
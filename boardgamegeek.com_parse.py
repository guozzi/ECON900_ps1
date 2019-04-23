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
		Game_Rank = r.find("td", {"class": "collection_rank"}).text
		
		df = df.append({
			'Parsed_From': Parsed_From, #Indicates the corresponding html file 
			'Game_Rank': Game_Rank, # Overall rank of the game, N/A means not ranked
			
			}, ignore_index=True)




df.to_csv("parsed_files/boardgamegeek_dataset.csv")
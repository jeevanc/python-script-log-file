import re
import os
from datetime import datetime
from bs4 import BeautifulSoup

import pandas 

def file_read(path):
	with open(path, 'r') as file:
		content = file.read()
	return content


working_directory = os.getcwd()
source_folder = os.path.join(working_directory, 'folder-name')


def text_extract():
	pattern = "::(.*?)::"
	a = []
	for file in os.listdir(source_folder):
		file_path = os.path.join(source_folder, file)
		strings = file_read(file_path)
		

		soup = BeautifulSoup(strings,'html.parser').text

		substring = re.findall(pattern, soup)
		

		substring = re.findall(pattern, strings, re.DOTALL)
		
		a.append(substring)
		
	return a





def text_process():
	text = text_extract()
	return text


if __name__ == "__main__":
	text = text_process()
	pd = pandas.DataFrame(text)
	pd.to_csv("myfile.csv", index=False, header=False)
	
	
	
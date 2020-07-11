import requests 
from bs4 import BeautifulSoup
import wget
import os

archive_url = input("Paste the url here: ")


FILETYPE = '.mp4'

dir_name = archive_url.split('/')[-2] 
dir_name = dir_name.upper()


def create_dir(path):
	
	try:
		isFile = os.path.exists(path)
		if isFile:
			os.chdir(path)
			print("Directory has been changed to " +path)
		
		else:
			os.makedirs(path)
			print ("Successfully created the directory %s" % path)
			os.chdir(path)

	except OSError:
			print ("Creation of the directory %s failed" % path)
create_dir(path=dir_name)



def get_video_links(): 

	# CREATE A LIST FOR STORING LINKS
	video_links = list()
	
	# create response object 
	r = requests.get(archive_url) 
	
	# # create beautiful-soup object 
	soup = BeautifulSoup(r.content,'lxml') 
	
	# find all links on web-page 
	# links = soup.find_all('a') 


	for link in soup.find_all('a'):
		file_link = link.get('href', "")
		if FILETYPE in file_link:
			print(file_link) 
			# ADD ANY VALID LINKS TO THE LIST
			video_links.append(file_link)
	
	return video_links
			

	# filter the link sending with .mp4 
	# video_links = [archive_url + link.get('href') for link in links if link('href').endswith('mp4')] 


def download_video_series(video_links): 

	for link in video_links: 

		'''iterate through all links in video_links 
		and download them one by one'''
		
		# obtain filename by splitting url and getting 
		# last string 
		file_name = link.split('/')[-1] 

		if os.path.exists(file_name):
			print(file_name, "already downloaded")

		else:
			print(f"Downloading file {file_name}" )
			
			# start Download
			wget.download(link)
			
			print(f"\nDownloaded! {file_name} ") 
			print()

	print("All videos downloaded!")
	return


if __name__ == "__main__": 

	# getting all video links 
	video_links = get_video_links() 
	
	
	# download all videos 
	download_video_series(video_links) 
	

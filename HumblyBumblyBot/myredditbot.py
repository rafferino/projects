import praw
import config
import requests
import time
import re
from lxml import html
from bs4 import BeautifulSoup
from rake_nltk import Rake

def bot_login():
	r = praw.Reddit(username = config.username,
			password = config.password,
			client_id = config.client_id,
			client_secret = config.client_secret,
			user_agent = "rafferino's humbly bumbly bot v0.1")
	print("Authenticated as {}".format(r.user.me()))
	return r

def main():
	humblybumbly = bot_login()
	while True:
		try:
			run_bot(humblybumbly)
		except Exception as e:
			parse_error(str(e))

def parse_error(e):
	err_msg = e
	wait_time = re.findall('\d+', err_msg)[0].rstrip()
	unit = ""
	if "seconds" in err_msg:
		unit = "second(s)"
	else:
		unit = "minute(s)"
	print("Sleeping for {0} {1}...".format(wait_time, unit))
	print(err_msg)
	if unit == "minute(s)":
		wait_time = int(wait_time)*60
	time.sleep(wait_time)
		

def run_bot(reddit):
	print(get_humble_bundles())
	for comment in reddit.subreddit('humblebundles').comments(limit = 100):
		for i in range(0, len(name_list)):
			if any(name_check in comment.body.lower() for name_check in name_list[i].lower().split(' ')):
				if comment.author != reddit.user.me() and comment.id not in open('comments.txt').read():
					print("Found a bumbly!!!")
					urltail = ""
					if "software" in name_list[i].lower():
						urltail = "software/" + name_list[i].replace(" ", "-")
					elif "book" in title_list[i].lower():
						urltail = "books/" + name_list[i].replace(" ", "-") + "-books/"
					else:
						urltail = title_list[i].replace(" ", "-")
					comment.reply("I'm humblybumblybot! I recognize that: {0}! [Here is the link to it](http://www.humblebundle.com/{1})!".format(title_list[i], urltail))
					with open("comments.txt", "a") as text_file:
						text_file.write(comment.id + "\n")
					print("Replied to comment " + comment.id)

def get_humble_bundles():
	page = requests.get('http://www.humblebundle.com/')
	tree = html.fromstring(page.content)
	title = tree.xpath('//div[@class = "primary info-section"]/text()')
	print(title)
	title = [string.rstrip() for string in title]
	names = [string.rstrip().split('Bundle')[0].rstrip() for string in title]
	print(names)
	return (title, names)

def get_humble_games():
	page = requests.get('http://www.humblebundle.com/')
	tree = html.fromstring(page.content)
	title = tree.xpath('//div[@id="subtab-container"]/a/text()')
	title = [string.rstrip() for string in title]
	print(title)
	names = [string.rstrip().split('Bundle')[0].rstrip() for string in title]
	print(names)
	return (title, names)

def get_humble_software():
	page = requests.get('http://www.humblebundle.com/software/')
	tree = html.fromstring(page.content)
	title = tree.xpath('//title/text()')
	title = [string.rstrip().split(' (')[0] for string in title]
	print(title)
	names = [string.rstrip().split('Bundle')[0].rstrip() for string in title]
	print(names)
	return (title, names)

def get_humble_books():
	page = requests.get('https://www.humblebundle.com/books/')
	tree = html.fromstring(page.content)
	title = tree.xpath('//div[@id="subtab-container"]/a/text()')
	title = [string.rstrip() for string in title]
	print(title)
	names = [string.rstrip().split(' presented')[0] for string in title]
	print(names)
	return (title, names)
	

print("Prior to import: {}".format(__name__))

from myredditbot import run_bot

print("About to run bot")

if __name__ == '__main__':
	main()




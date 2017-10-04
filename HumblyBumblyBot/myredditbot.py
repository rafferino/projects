import praw
import config
import requests
import re
from lxml import html

def bot_login():
	r = praw.Reddit(username = config.username,
			password = config.password,
			client_id = config.client_id,
			client_secret = config.client_secret,
			user_agent = "rafferino's humbly bumbly bot v0.1")
	print("Authenticated as {}".format(r.user.me()))
	return r

def run_bot(reddit):
	title_list = get_humble_title()[0]
	name_list = get_humble_title()[1]
	for comment in reddit.subreddit('humblebundles').comments(limit = 25):
		for i in range(0, len(name_list)):
			if name_list[i] in comment.body:
				print("Found a Bundle!!!")
				if comment.author != reddit.user.me():
					comment.reply("I'm humblybumblybot! I recognize that Bundle! [Here](http://www.humblebundle.com/{}) is the link to it!".format(title_list[i].replace(" ", "-")))

def get_humble_title():
	page = requests.get('http://www.humblebundle.com/')
	tree = html.fromstring(page.content)
	title = tree.xpath('//div[@id="subtab-container"]/a/text()')
	title = [string.rstrip() for string in title]
	names = [string.rstrip().split('Bundle')[0].rstrip() for string in title]
	print(names)
	return (title, names)

humblybumbly = bot_login()
run_bot(humblybumbly)
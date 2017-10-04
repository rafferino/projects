import praw
import config
import requests
import time
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

def main():
	humblybumbly = bot_login()
	while True:
		try:
			run_bot(humblybumbly)
		except Exception as e:
			err_msg = str(e)
			wait_time = re.findall('\d+', str(e))[0]
			print("Sleeping for {} minute(s)...".format(wait_time))
			print(err_msg)
			time.sleep(int(wait_time)*60)
		

def run_bot(reddit):
	title_list = get_humble_title()[0]
	name_list = get_humble_title()[1]
	for comment in reddit.subreddit('humblebundles').comments(limit = 25):
		for i in range(0, len(name_list)):
			if name_list[i] in comment.body:
				if comment.author != reddit.user.me():
					print("Found a bumbly!!!")
					comment.reply("I'm humblybumblybot! I recognize that Bundle! [Here is the link to it](http://www.humblebundle.com/{})!".format(title_list[i].replace(" ", "-")))
					print("Replied to comment " + comment.id)
	print("Sleeping for 5 minutes...")
	time.sleep(60*5)

def get_humble_title():
	page = requests.get('http://www.humblebundle.com/')
	tree = html.fromstring(page.content)
	title = tree.xpath('//div[@id="subtab-container"]/a/text()')
	title = [string.rstrip() for string in title]
	names = [string.rstrip().split('Bundle')[0].rstrip() for string in title]
	print(names)
	return (title, names)

print("Prior to import: {}".format(__name__))

from myredditbot import run_bot

print("About to run bot")

if __name__ == '__main__':
	main()




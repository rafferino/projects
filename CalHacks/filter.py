import json

from pprint import pprint

with open('restaurant1.json') as restaurant_file:
	large_map=json.load(restaurant_file)
pprint(large_map)
restaurant_list = large_map["items"]
for restaurant in restaurant_list:
	with open('filtered_restaurants.json', 'w') as f:
		json.dump(restaurant, f)
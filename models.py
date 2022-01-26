import json
import hashlib

#ROOT = path.dirname(path.relpath((__file__)))

def create_post(name, content):
	post = {"name":name, "content":content}
	hash = hashlib.sha3_256(str(post).encode('utf-8')).hexdigest()
	data = {}
	try:
		with open('posts.json', 'r') as f:
			data = json.load(f)
	except:
		with open('posts.json', 'w') as f:
			json.dump({}, f)
	number_of_posts = len(data)
	previous_hash = "0"
	if number_of_posts > 0:
		previous_hash = data[str(number_of_posts-1)]["hash"]
	post["hash"] = hash
	post["previous_hash"] = previous_hash
	data[number_of_posts] = post

	with open('posts.json', 'w') as f2:
		json.dump(data,f2)
	f.close()
	f2.close()

def get_posts():
	data = {}
	try:
		with open('posts.json', 'r') as f:
			data = json.load(f)
	except:
		with open('posts.json', 'w') as f:
			json.dump({}, f)
			
	#list = [[data[i]["name"], data[i]["content"]] for i in data] 
	#for i in data:
	#	list.append(data[i]["name"])
	#	list.append(data[i]["content"])
	return data





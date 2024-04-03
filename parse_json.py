import json
import os
import hashlib


# Opening JSON file
f = open('data.json',)

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
for i in data['samples']:
  f = open("./files/"+i['id']+".txt","w")
  f.write(i['name'])
  f.close()

  with open("./files/"+i['id']+".txt", 'rb') as in_f:
    file_hash = hashlib.sha256(in_f.read()).hexdigest()
  try:
    if file_hash == i['id']: #hashlib.sha256(i['id'].encode('utf-8')).hexdigest:
      print(f"File {i['id']+'.txt'} created and SHA256 sum matches id!")
    else:
      print(f"WARNING: File {i['id']+'.txt'} content hash ({file_hash}) does not match id!")
  except FileNotFoundError:
    in_f.close()

# Python program to read
# json file
  
  
import json
from pprint import pprint
  
# Opening JSON file
f = open('/home/nsl50/Desktop/Mredul_vai/Json_Extraction/merged_data.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)
  
# Iterating through the json
# list

pprint(data)
#for i in data:
    #print(i)
  
# Closing file
f.close()

#if __name__== '__main__':
    
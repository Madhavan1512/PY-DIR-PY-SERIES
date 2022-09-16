import json
book = {}
book['tom']={
    'name': 'Tom', 
    'address': '1 red street , NY',   
    'phone': 8217091016
}
book['bob']={
    'name': 'Bob',  
    'address': '2 red street , NY',   
    'phone': 9448950282
}
s=json.dumps(book)
print(s)
with open("C:/users/maddy/Book.json","w") as f : 
   f.write(s)  
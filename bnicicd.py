import requests 
from datetime import datetime

print ("Hello world")
print ("testng CI CD BNI") 

response = requests.get("https://google.com")

waktu = datetime.now()

with open ("tempResponse/"+str(waktu)+".txt","w")  as f:
    f.write(response.text)
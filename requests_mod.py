import requests
from pprint import pprint
# I used this url from xkcd webside 
#url='https://imgs.xkcd.com/comics/coronavirus_polling.png'
url2=' https://imgs.xkcd.com/comics/emotion.png'
url='http://httpbin.org/get'
payload={"name":"prakash","characterstrength":1}
r=requests.get(url,params=payload)
#with open("emotion.png",'wb') as png:
 #   png.write(r.content)
  #  print("Image is downloaded")

print(r.text)
print(r.url)


post_url='http://httpbin.org/post'
dataload={"username":"ksprakash",'password':"&#4aoidsod213ka"}
p=requests.post(post_url,data=dataload)

print(p.json())


auth_url='http://httpbin.org/basic-auth/ksp/@Pr@k@h'

auth=requests.get(auth_url,auth=('ksp','@Pr@k@h'))
print(auth.text)



github_api_url='https://api.github.com/user'

github1=requests.get(github_api_url, auth=("ksprakash","Iaia#1"))

pprint(github1.text)
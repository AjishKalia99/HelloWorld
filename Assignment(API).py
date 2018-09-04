#Question 1
#Use the "https://api.forismatic.com/api/1.0/" api to get random quotes using the correct endpoints.
import requests
import json
parameters={'method':'getQuote','format':'json','lang':"en",'key':''}
response=requests.get("https://api.forismatic.com/api/1.0/getQuote.json",params=parameters)
res=response.json()
print("The Random Quote for you is: {} \nThe Author of the Quote is: {}".format(res['quoteText'],res['quoteAuthor']))
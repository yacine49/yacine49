import speech_recognition as sr
import requests,os,json
from fon_lib import speak,recognize
from bs4 import BeautifulSoup 

speak(("Coronavirus cases and deaths . Just Tell me the country ! made by Yaseen "))
print(("Coronavirus cases and deaths . Just Tell me the country ! made by Yaseen "))

country = recognize()
country = country+"/"
country_url = "https://www.worldometers.info/coronavirus/country/"+country
result = requests.get(country_url)
country_soup = BeautifulSoup(result.content,'html.parser')
cases = country_soup.find_all(id="maincounter-wrap")
text = str()
if cases==[]:
    speak(" Could not understand you ? or there isn't such country")
else:
	for column in cases:
		
		text = text + ('{}').format(column.text)	
		
	print (text)
	speak((('in {} ').format(country))+text)


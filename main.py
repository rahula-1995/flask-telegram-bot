
import requests
import json
from flask import Flask
from flask import request
from flask import Response
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os
TOKEN = os.environ["TOKEN"]
GOOGLE_CHROME_PATH = '/app/.apt/usr/bin/google_chrome'
CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'
#chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument('--disable-gpu')
#chrome_options.add_argument('--no-sandbox')
#chrome_options.binary_location = GOOGLE_CHROME_PATH
#driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)

service = Service(CHROMEDRIVER_PATH)
service.start()
driver = webdriver.Remote(service.service_url)
app=Flask(__name__)
def write_json(data ,filename='response.json'):
	with open(filename ,'w') as f:
		json.dump(data ,f ,indent=4 ,ensure_ascii=False)


def geth(all):
	tex='Namaste ''\nThis is Coronavirus (COVID-19) Helpdesk developed by Rahul Anand to create awareness and help you and your family stay safe.\n''For any emergency \n''📞 Helpline: 011-23978046 | Toll-Free Number: 1075\n''✉️ Email: ncov2019@gov.in\n''Please choose from the following options 👇\n''1. Latest Update and Alerts on Coronavirus\n''2. What is Coronavirus and what are its symptoms?\n''3. How does Coronavirus spread?\n''4. How to reduce the risk of Coronavirus?\n''5. Professional Advice by Doctors\n''6. Where to get help?\n''7. News on coronavirus across the globe\n''💡 Tip: You can type 1, 2, 3, 4, 5, 6, 7 to make a selection of the menu options or\n''👉 To check details of your state. Please type the name of your state below 👇\n''For eg. Maharashtra\n''👉 To check details of your District. Please type the name of your District below 👇\n''For eg. Patna\n'
	return tex
def get1(all):
	q,ni=getd('Gaya')

	qq=str(ni[0])
	qw=str(ni[2])
	qe=str(ni[3])
	tex='COVID-19 Updates 👇\n''▪️ Active Cases:'+qq+'\n''▪️ Cured/Discharged/Migrated cases:'+qw+'\n''▪️ Death cases:'+qe+'\n''For donation to Prime Minister''s Citizen Assistance & Relief in Emergency Situations (PM CARES) Fund (Donation is tax exempted) https://www.pmindia.gov.in\n''21 days Lockdown duration : From 25.03.2020 to 14.04.2020 Please stay at home. Essential commodities, medicines, etc would be available during Lockdown\n''Useful Alerts 👇\n''▪️ Fact : Claim that Government will extend 21 Day Lockdown when it expires is baseless\n''▪️ All 24 classes of medical devices are regulated under Drug Price Control regime from 1 April 2020\n''▪️ Capacity utilization of ICMR labs 38%, its lab network stands at 126\n''▪️ Health actions to be taken at place of congregation of migrant workers\n''▪️ CBSE to promote all students of classes I-VIII to the next grade\n''▪️ Students of classes IX & XI to be promoted on school-based assessments\n''▪️ Trained counselors & community leaders to provide psycho-social support to migrants in relief camps\n''▪️ Fact: COVID-19 does not spread from Mosquito bites\n''For Corona Volunteer Opportunities - https://self4society.mygov.in/volunteer/\n''Testing Facilities for COVID-19 in the Country 👇\n''▪️ Operational Govt. Laboratories: 126\n''▪️ Govt. Laboratories (being operationalized): +9\n''▪️ Authorized Private Laboratories: 51\n''For Pledge to Stay at Home -\n''https://pledge.mygov.in/stayathome/\n''For detailed information on coronavirus, please check the link below 👇\n''https://www.mygov.in/covid-19\n''https://www.mohfw.gov.in\n''👉 Type 2 for Symptoms\n''👉 Type 3, 4, 5, 6, 7 to see other options\n''👉 Type Menu to view the Main Menu\n''👉 To check details of your state. Please type the name of your state below 👇\n''For eg. Maharashtra\n''👉 To check details of your District. Please type the name of your District below 👇\n''For eg. Patna\n'
	return tex
def get2(all):
	tex='Coronaviruses are a large family of viruses, some causes illness in people. Its symptoms in humans are\n''🤒 Fever\n''😐 Breathing problem\n''🤧 Coughing\n''😫 Tightness of chest\n''👃 Running Nose\n''😨 Headache\n''🌡️ Feeling unwell\n''😷 Pneumonia\n''💉 Kidney Failure\n''It can be difficult to identify the disease based on symptoms alone. Check when you should get tested 👇\n''https://www.mohfw.gov.in/pdf/FINAL_14_03_2020_ENg.pdf\n''You can also view the video on symptoms by Director,AIIMS-Delhi 👇\n''https://youtu.be/E8-UoeWewFI\n''👉 Type 3 to know more on How does Coronavirus spread?\n''👉 Type 1, 4, 5, 6, 7 to see other options\n''👉 Type Menu to view the Main Menu\n''👉 To check details of your state. Please type the name of your state below 👇\n''For eg. Maharashtra\n''👉 To check details of your District. Please type the name of your District below 👇\n''For eg. Patna\n'
	return tex
def get3(all):

	tex='Coronavirus spreads from an infected person through 👇\n''♦️ Small droplets from the nose or mouth which are spread when a person coughs or sneezes\n''♦️ Touching an object or surface with these droplets on it and then touching your mouth, nose, or eyes before washing your hands\n''♦️ Close personal contact, such as touching or shaking hands\n''Please watch the video for more information 👇\n''https://youtu.be/0MgNgcwcKzE\n''👉 Type 4 to check the Preventive Measures \n''👉 Type 1, 2, 5, 6, 7 to see other options\n''👉 Type Menu to view the Main Menu\n''👉 To check details of your state. Please type the name of your state below 👇\n''For eg. Maharashtra\n''👉 To check details of your District. Please type the name of your District below 👇\n''For eg. Patna\n'
	return tex

def get4(all):
	tex='Coronavirus infection can be prevented through the following means 👇\n''✔️ Clean hand with soap and water or alcohol-based hand rub\n'' https://youtu.be/EJbjyo2xa2o\n''✔️ Cover nose and mouth when coughing & sneezing with a tissue or flexed elbow\n''https://youtu.be/f2b_hgncFi4\n''✔️ Avoid close contact & maintain 1-meter distance with anyone who is coughing or sneezing\n''https://youtu.be/mYyNQZ6IdRk\n''✔️ Isolation of persons traveling from affected countries or places for at least 14 days\n''✔️ Quarantine if advised\n''https://www.mohfw.gov.in/pdf/Guidelinesforhomequarantine.pdf\n''👉 Type 5 to check the Professional Advice by Doctors \n''👉 Type 1, 2, 3, 6, 7 to see other options\n''👉 Type Menu to view the Main Menu\n''👉 To check details of your state. Please type the name of your state below 👇\n''For eg. Maharashtra\n''👉 To check details of your District. Please type the name of your District below 👇\n''For eg. Patna\n'
	return tex

def get5(all):
	tex='Please watch the videos by Doctors to clear your doubts on Coronavirus 👇\n'' Stay Home, Stay Safe\n''https://youtu.be/yZd8bPTfYOg\n''Connecting with children during lockdown\n''https://youtu.be/OYD9bogtJlU\n''Advice on Prevention\n''https://youtu.be/E8-UoeWewFI\n''Advice for Senior Citizen\n''https://youtu.be/I6F1I7_4gDI\n''Advice for Children\n''https://youtu.be/mnNghi8m3l4\n''👉 Type 6 for any other help\n''👉 Type 1, 2, 3, 4, 7 to see other options\n''👉 Type Menu to view the Main Menu\n''👉 To check details of your state. Please type the name of your state below 👇\n''For eg. Maharashtra\n''👉 To check details of your District. Please type the name of your District below 👇\n''For eg. Patna\n'
	return tex
def gets(state):
	driver.get('https://www.covid19india.org/')
	content1=driver.page_source
	soup1 = BeautifulSoup(content1)
	ty = soup1.find_all('tr', attrs={'class': 'state'})
	dd = []
	for ele in ty:
		for t in ele:
			for y in t:
				dd.append(y)
	ee = []
	i = 0
	j = 1
	while i < len(dd):
		if j == i:
			j = j + 6
		else:
			ee.append(dd[i])
		i = i + 1
	i = 0
	ff=[]
	while i < len(ee):
		if ee[i] == state:
			ff.append(ee[i + 1])
			ff.append(ee[i + 2])
			ff.append(ee[i+3])
			ff.append(ee[i+4])
			break
		i=i+1
	return ff

def get6(all):
	tex='For medical help in India please reach out to the 24/7 Control Room.\n''📞 Phone: +91-11-23978046\n''☎️ Toll-Free Number: 1075\n''✉️ Email: ncov2019@gov.in\n''For Behavioural Health: Psycho-Social\n'' 📞 08046110007\n''For queries from a person outside India. Please contact Ministry of External Affairs(MEA), GOI\n''📞 1800118797\n''✉️ covid19@mea.gov.in\n''For Visa related queries\n''📞 01124300666\n''✉️ support.covid19-boi@gov.in\n''👉 Type 7 for global news on coronavirus\n''👉 Type 1, 2, 3, 4, 5 to see other options\n''👉 Type Menu to view the Main Menu\n''👉 To check details of your state. Please type the name of your state below 👇\n''For eg. Maharashtra\n''👉 To check details of your District. Please type the name of your District below 👇\n''For eg. Patna\n'
	return tex




def get8(state):
	ff=gets(state)
	k={'Andhra Pradesh': '0866-2410978', 'Arunachal Pradesh': 9436055743, 'Assam': 6913347770, 'Bihar': 104, 'Chhattisgarh': 104, 'Goa': 104, 'Gujarat': 104, 'Haryana': 8558893911, 'Himachal Pradesh': 104, 'Jharkhand': 104, 'Karnataka': 104, 'Kerala': '0471-2552056', 'Madhya Pradesh': 104, 'Maharashtra': '020-26127394', 'Manipur': 3852411668, 'Meghalaya': 108, 'Mizoram': 102, 'Nagaland': 7005539653, 'Odisha': 9439994859, 'Punjab': 104, 'Rajasthan': '0141-2225624', 'Sikkim': 104, 'Tamil Nadu': '044-29510500', 'Telangana': 104, 'Tripura': '0381-2315879', 'Uttarakhand': 104, 'Uttar Pradesh': 18001805145, 'West Bengal': '1800313444222, 03323412600,', 'Name of Union Territory (UT)': 'Helpline Nos.', 'Andaman and Nicobar\nIslands': '03192-232102', 'Chandigarh': 9779558282, 'Dadra and Nagar Haveli and Daman & Diu': 104, 'Delhi': '011-22307145', 'Jammu & Kashmir': '01912520982, 0194-2440283', 'Ladakh': 1982256462, 'Lakshadweep': 104, 'Puducherry': 104}

	tex='The helpline number for'+' '+str(state)+' '+'is'+' '+str(k[state])+'\n''COVID-19 Updates 👇\n''▪️ Total Cases:'+str(ff[0])+'\n''▪️ Active Cases:'+str(ff[1])+'\n''▪️ Cured/Discharged/Migrated cases:'+str(ff[2])+'\n''▪️ Death cases:'+str(ff[3])+'\n''Please check the PDF given below to check the helpline numbers of other states 👇\n''https://www.mohfw.gov.in/pdf/coronvavirushelplinenumber.pdf\n''👉 Type 1, 2, 3, 4, 5, 6 to see other options\n''👉 Type Menu to view the Main Menu\n''👉 To check details of your state. Please type the name of your state below 👇\n''For eg. Maharashtra\n''👉 To check details of your District. Please type the name of your District below 👇\n''For eg. Patna\n'
	return tex

def get7(all):

	driver.get("https://timesofindia.indiatimes.com/india/coronavirus-india-live-updates-madhya-pradesh-covid-19-tally-rises-to-20-five-test-positive-in-indore/liveblog/74820018.cms")
	content1=driver.page_source
	soup1 = BeautifulSoup(content1)
	s = []

	for a in soup1.findAll('div', attrs={'class': '_1KydD'}):

		s.append(a.text)
	tex=''
	for ele in s:
		tex=tex+str(ele)+'\n'
	return tex+'👉 Type 1, 2, 3, 4, 5, 6 to see other options\n''👉 Type Menu to view the Main Menu\n''👉 To check details of your state. Please type the name of your state below 👇\n''For eg. Maharashtra\n''👉 To check details of your District. Please type the name of your District below 👇\n''For eg. Patna\n'

def get9(district):
	fg,b=getd(district)
	if fg=='invalid district name':
		tex='sorry i did not understand or there is no case in this district\n'
	else:
		tex='COVID-19 Updates 👇\n''▪️ Total Cases:'+str(fg)+'\n'
	return tex+'1. Latest Update and Alerts on Coronavirus\n''2. What is Coronavirus and what are its symptoms?\n''3. How does Coronavirus spread?\n''4. How to reduce the risk of Coronavirus?\n''5. Professional Advice by Doctors\n''6. Where to get help?\n''7. News on coronavirus across the globe\n''👉 Type 1, 2, 3, 4, 5, 6 to see other options\n''👉 Type Menu to view the Main Menu\n''👉 To check details of your state. Please type the name of your state below 👇\n''For eg. Maharashtra\n''👉 To check details of your District. Please type the name of your District below 👇\n''For eg. Patna\n'





def getd(district):
	k=str(district)
	if k:
		pass
	else:
		k='Gaya'
	driver.get('https://www.covid19india.org/')
	content1 = driver.page_source

	soup1 = BeautifulSoup(content1)

	dis = soup1.find_all('tr', attrs={'class': 'district'})
	w=[]
	for row in dis:
		flag = False
		for ele in row:

			if ele.text == k:
				flag = True
			if flag:
				for e in ele:
					w.append(e)

		if flag:
			break
	if len(w)>0:
		w.pop(1)
	rows = soup1.find_all('div', attrs={'class': 'Level fadeInUp'})
	rt=rows[0].find_all('h1')
	li = []
	for ele in rt:
		li.append(ele.text)
	if len(w)<2:
		return 'invalid district name',li
	else:
		return w[1],li


def parse_message(message):
	chat_id=message['message']['chat']['id']
	txt=message['message']['text']

	return chat_id,txt
def send_message(chat_id,text='blabla'):
	url='https://api.telegram.org/bot'+str(TOKEN)+'/sendMessage'
	payload={'chat_id':chat_id,'text':text}

	r=requests.post(url,json=payload)
	return r




@app.route('/',methods=['POST','GET'])
def index():
	ki=['Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jharkhand', 'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura', 'Uttarakhand', 'Uttar Pradesh', 'West Bengal', 'Name of Union Territory (UT)', 'Andaman and Nicobar\nIslands', 'Chandigarh', 'Dadra and Nagar Haveli and Daman & Diu', 'Delhi', 'Jammu & Kashmir', 'Ladakh', 'Lakshadweep', 'Puducherry']
	if request.method=='POST':
		msg=request.get_json()
		chat_id,symbol=parse_message(msg)
		if not symbol:
			send_message(chat_id,'wrong data')
			return Response('ok',status=200)
		if symbol=='hi' or symbol=='Hi' or symbol=='Menu':
			price=geth(symbol)
		elif symbol=='1':
			price=get1(symbol)
		elif symbol=='2':
			price=get2(symbol)
		elif symbol=='3':
			price=get3(symbol)
		elif symbol=='4':
			price=get4(symbol)
		elif symbol=='5':
			price=get5(symbol)
		elif symbol=='6':
			price=get6(symbol)
		elif symbol=='7':
			price=get7(symbol)

		elif symbol in ki:
			price=get8(symbol)
		else:
			price=get9(symbol)
		send_message(chat_id,price)

		write_json(msg,'telegram_request.json')
		return Response('ok',status=200)
	else:

		return '<h1>corona virus is very deadly</h1>'




if __name__ == '__main__':
	app.run(debug=True)
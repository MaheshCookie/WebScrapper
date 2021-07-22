from bs4 import BeautifulSoup
import requests
import time

print('Put some skill tha you are not familiar with' )
#unfamiliar_skill=[]
#unfamiliar_skill = input('>')
unfamiliar_skill = str(input().split()).lower()
print(f'Filtering out {unfamiliar_skill}')
#print(unfamiliar_skill)

def find_jobs():
    #print("Begins")
    html_text =requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text,'lxml')
    jobs = soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
    for job in jobs:
        pub_date = job.find('span',class_ ='sim-posted').text
        if 'few' in pub_date:
            company_name = job.find('h3',class_ ='joblist-comp-name').text.replace(' ','')
            skills = []
            skills = job.find('span', class_ ='srp-skills').text.replace(' ','')
            more_info = job.header.h2.a['href']
            tskills = list(skills.strip().split(','))
            #if unfamiliar_skill  not in skills:
            result = any(elem in unfamiliar_skill for elem in tskills )
            if result != True:
                print(f'Company Name: {company_name.strip()}')
                print(f'Skills: {skills.strip()}')
                print(f'More_Info: {more_info}')
                print('')
                
if __name__ == '__main__':
    #print("main")
    while True:
        print("main")
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} minutes.')
        time.sleep(time_wait * 60)
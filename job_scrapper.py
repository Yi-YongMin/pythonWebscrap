#웹사이트에서 데이터를 추출하는 작업. beautifulsoup가 필요하다.
from requests import get
from bs4 import BeautifulSoup
base_url = "https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term="
search_term="react" #여기를 바꿈으로써 여러 직종을 찾아볼 수 있다.
response=get(f"{base_url}{search_term}") # 위에 두 문자열을 합치는 작업.
if response.status_code !=200:
    print("Can't request website")
else:
    results=[]
    soup=BeautifulSoup(response.text,"html.parser") #.text는 html코드를 갖게 해주고, BeautifulSoup는 우리가 가진 코드를 파이썬이 다룰수 있는 코드로 바꿔준다.
    jobs=soup.find_all('section',class_="jobs") #class_="jobs" 를 이용하는 이유는 find_all 이라는 함수가 매개변수를 너무 많이 갖고있기 때문에.(find_all은 list를 줘요)
    for job_section in jobs:
        job_posts = job_section.find_all('li')
        job_posts.pop(-1)
        for post in job_posts:
            anchors = post.find_all('a')
            anchor=anchors[1]
            link=anchor['href']
            company,position,region=anchor.find_all('span',class_="company")
            title=anchor.find('span',class_='title')
            print(company.string,position.string,region.string,title.string)
            job_data={
                'company':company.string,
                'region':region.string,
                'title':title.string
            }
            results.append(job_data)
    for result in results:
        print(result)
        print("/////////")

#파이썬 문법중 하나. 리스트의 요소개수를 알면, 변수를 빠르게 부여할 수 있다.

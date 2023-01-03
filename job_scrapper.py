#웹사이트에서 데이터를 추출하는 작업. beautifulsoup가 필요하다.
from requests import get
from bs4 import BeautifulSoup
base_url = "https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term="
search_term="python"
response=get(f"{base_url}{search_term}") # 위에 두 문자열을 합치는 작업.
if response.status_code !=200:
    print("Can't request website")
else:
    soup=BeautifulSoup(response.text,"html.parser")
    jobs=soup.find_all('section',class_="jobs") #class_="jobs" 를 이용하는 이유는 find_all 이라는 함수가 매개변수를 너무 많이 갖고있기 때문에.
    for job_section in jobs:
        job_posts = job_section.find_all('li')
        job_posts.pop(-1)
        for post in job_posts:
            print(post)
            print("//////////////////////////////////////////////////")
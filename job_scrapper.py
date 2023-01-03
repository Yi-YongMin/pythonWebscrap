#웹사이트에서 데이터를 추출하는 작업. beautifulsoup가 필요하다.
from requests import get
from bs4 import BeautifulSoup
base_url = "https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term="
search_term="python"
response=get(f"{base_url}{search_term}") # 위에 두 문자열을 합치는 작업.
if response.status_code !=200:
    print("Can't request website")
else:
    print(response.text)
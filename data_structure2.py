from requests import get
websites=[
    "google.com",
    "airbnb.com",
    "https://twitter.com",
    "facebook.com",
    "https://tiktok.com"
]
results={} #딕셔너리이다.

for website in websites:
    if not website.startswith("https://"):
    #if website.startswith("https://")==False : 와 동치이다.
        website=f"https://{website}" #f"를 기억하자. string에 변수를 추가하는 방법이다.
        response=get(website) # 만일 print(response)를 한다면 Response[200] 이라는 문장이 나온다. 이는 error404라는 흔히본 오류코드와 같은 이치.
        # if response.status_code==200:
        #     print(f"{website} is okay")
        # else:
        #     print(f"{website} is NOT okay")
    if response.status_code==200:
        results[website]='OK'
    else:
        results[website] = 'FAILED'
print(results)




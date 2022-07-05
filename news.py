import requests
from datetime import datetime
from pprint import pprint
import json

limit = int(input('limit of news: '))
URL = (f"http://newsline.kg/getNews.php?limit={limit}&last_dt={datetime.now()}")

'''
etot function beret is URL dannye i zapisyvaet v new file s formate json, s ukazaniem tekushei daty (format daty dd/mm/yy) s otstupom 4 shaga
'''

def get_news():
    t_date = datetime.now().strftime('%d_%m_%Y')
    response = requests.get(url = URL)

    with open(f'news for the date: {t_date}.json', 'w') as file:
        json.dump(response.json(), file, indent=4, ensure_ascii=False)


def main():
    get_news()


if __name__ == "__main__":
    main()
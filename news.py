import requests
from datetime import datetime
import json

limit = int(input('limit of news: '))
URL = (f"http://newsline.kg/getNews.php?limit={limit}&last_dt={datetime.now()}")


def get_news():
    t_date = datetime.now().strftime('%d_%m_%Y')
    response = requests.get(url = URL)

    with open(f'news for the date: {t_date}.json', 'w') as file:
        json.dump(response.json(), file, indent=4, ensure_ascii=False)


def main():
    get_news()


if __name__ == "__main__":
    main()
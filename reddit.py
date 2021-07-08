from datetime import time
import requests
import json

def format_date(timestamp_obj):
    from datetime import datetime
    datetime_obj = datetime.fromtimestamp(timestamp_obj)
    return str(datetime_obj)


def get_data(url):
    r = requests.get(url, headers={'User-agent': 'your bot 0.1'})
    python_obj = json.loads(r.text)
    news = python_obj['data']['children']
    filtered_data = []
    number = 1
    for new in news:
        news_data = {
            f'News number {number}': {
                'title': new['data']['title'],
                'author': new['data']['author'],
                'created': format_date(new['data']['created'])
            }
        }
        filtered_data.append(news_data)
        number +=1

    return filtered_data
    
def write_to_json(data):
    with open('RedditNews.json', 'w') as f:
        json.dump(data, f, indent=4)

def main(url):
    data = get_data(url)
    write_to_json(data)


main('https://www.reddit.com/r/DotA2/.json')
import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get("https://news.ycombinator.com")

html_text = BeautifulSoup(res.text, "html.parser")

links = html_text.select(".titlelink")
subtext = html_text.select(".subtext")


def sort_stories_by_votes(hacker_news_list):
    return sorted(hacker_news_list, key=lambda k: k["votes"], reverse=True)


def create_custom_hacker_news(links, subtext):
    hacker_news = []
    for index, item in enumerate(links):
        title = links[index].getText()
        href = links[index].get("href", None)
        vote = subtext[index].select(".score")
        if len(vote):
            points = int(vote[0].getText().replace(" points", ""))
            if points > 99:
                hacker_news.append(
                    {"title": title, "link": href, "votes": points})
    return sort_stories_by_votes(hacker_news)


pprint.pprint(create_custom_hacker_news(links, subtext))

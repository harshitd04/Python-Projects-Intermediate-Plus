from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
response.raise_for_status()
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

articles = soup.find_all(name="tr", class_="athing")
article_texts = []
article_links = []
article_upvotes = []

for article in articles:
    title_tag = article.find(name="span", class_="titleline").find("a")
    if title_tag:
        text = title_tag.getText()
        link = title_tag.get("href")
        article_texts.append(text)
        article_links.append(link)

        subtext = article.find_next_sibling("tr").find(name="td", class_="subtext")
        if subtext:
            score_tag = subtext.find(name="span", class_="score")
            if score_tag:
                upvotes = int(score_tag.getText().split()[0])
            else:
                upvotes = 0
            article_upvotes.append(upvotes)

if len(article_texts) != len(article_upvotes):
    print("Mismatch between articles and upvotes. Please verify the HTML structure.")
    exit()

if article_upvotes:
    largest_no = max(article_upvotes)
    index_largest_no = article_upvotes.index(largest_no)

    print("Most Popular News on Hacker News right now is:")
    print(article_texts[index_largest_no])
    print(article_links[index_largest_no])
    print(f"Upvotes: {article_upvotes[index_largest_no]}")
else:
    print("No upvotes found. There might be an issue with data extraction.")

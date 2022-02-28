from bs4 import BeautifulSoup
import requests

page = 'https://nl.linkedin.com/in/kobus-bijker-0692901a'

page_source=  requests.get(page).text

soup = BeautifulSoup(page_source, 'lxml')
reviews = []
reviews_selector = soup.find_all('div', class_='reviewSelector')
for review_selector in reviews_selector:
    review_div = review_selector.find('div', class_='dyn_full_review')
    if review_div is None:
        review_div = review_selector.find('div', class_='basic_review')
    review = review_div.find('div', class_='entry').find('p').get_text()
    review = review.strip()
    reviews.append(review)

print(reviews)


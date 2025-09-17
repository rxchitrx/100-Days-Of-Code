import requests
from bs4 import BeautifulSoup
from twilio.rest import Client

account_sid = "TWILIO_ACCOUNT_SID"
auth_token = "TWILIO_AUTH_TOKEN"


response = requests.get("https://news.ycombinator.com/")
y_c_web_page = response.text
soup = BeautifulSoup(y_c_web_page, "html.parser")


articles = soup.find_all("span", class_="titleline")
titles = []
links = []
for article_tag in articles:
    whole_tag = article_tag.find("a")
    title = whole_tag.string
    titles.append(title)
    link = whole_tag.get("href")
    links.append(link)
scores = [int(score.string.split(" ")[0]) for score in soup.find_all("span", class_="score")]
scores.sort(reverse=True)
sorted_scores = scores[:5]
print(sorted_scores)


articles_with_score = list(zip(sorted_scores, titles, links))
messages = []

idx = 1
for score, title, link in articles_with_score[:5]:
    messages.append(f"{idx}. {title} ({score}) : {link}")
    idx += 1

message_body = "\n".join(messages) 


client = Client(account_sid, auth_token)
message = client.messages.create(
        from_="whatsapp:TWILIO_NUMBER",
        body=message_body,
        to="whatsapp:PERSONAL_NUMBER"
    )

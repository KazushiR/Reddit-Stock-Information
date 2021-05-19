import yfinance as yf
import json

with open("config_cred.json") as f:
    data = json.load(r)
    reddit = praw.Reddit(client_id = data["client_id"],
                         client_secret = data["client_secret"],
                         username = data["username"],
                         password = data["password"],
                         user_agent = data["user_agent"])
    r.close()

while True:
    for message in reddit.inbox.unread(limit=None):
        if subject == "username mention":
            pattern = re.compile("#\w+")
            stock_messages = (pattern).findall((message.body).lower())
            reply = message.id
            if len(stock_messages) == 1:
                ticker = ("".join(stocks_message)).strip("#")
                try:
                    stock = finvizfinance(f"{ticker}")
                    

"""GTA Trilogy Scraper"""

import requests
import ast

from bs4 import BeautifulSoup
import tweepy


def get_html(url):
    """Get HTML from a URL"""
    response = requests.get(url)
    return response.text


def update_last_value(price):
    """Update last value"""
    with open("last_value.txt", "w") as file:
        file.write(str(price))
        print("Last value updated!")


# consumer_key = "CONSUMER_KEY"
# consumer_secret = "CONSUMER_SECRET"
# access_token = "ACCESS_TOKEN"
# access_secret = "ACCESS_SECRET"

# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_secret)

# api = tweepy.API(auth)

# api.update_status("GTA Trilogy Scraper: \nPrice is lower!")


def main():
    """Main function"""
    print("GTA Trilogy Scraper")
    url = "https://store.rockstargames.com/es-419/game/buy-grand-theft-auto-the-trilogy-the-definitive-edition"
    html = get_html(url)
    soup = BeautifulSoup(html, "html.parser")
    id = "hero-buy-button"
    button = soup.find(id=id)
    price = ast.literal_eval(button.text.split()[-1])

    if isinstance(price, tuple):
        price = [str(price[i]) for i in range(len(price))]
        price = int(ast.literal_eval("".join(price)))

    print(f"Price: {price}")

    # read last_value.txt
    with open("last_value.txt", "r") as file:
        last_value = int(file.read())
        print(f"Last value: {last_value}")

    if price < last_value:
        print("Price is lower!")
        update_last_value(price)
    elif price == last_value:
        print("Price is the same!")
    else:
        print("Price is higher!")
        update_last_value(price)


if __name__ == "__main__":
    main()

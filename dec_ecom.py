import requests
from bs4 import BeautifulSoup
import pandas as pd
response = requests.get("https://www.flipkart.com/search?q=redmi+note+12+pro+5g&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_13_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_13_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=redmi+note+12+pro+5g%7CMobiles&requestId=729aae0d-3632-4e01-9b6f-d0fcf3c48205")
print(response)
soup = BeautifulSoup(response.content,'html.parser')
print(soup)


names = soup.find_all('div',class_='RG5Slk')
#print(names)
name = []
for i in names[0:10]:
    d = i.get_text()
    name.append(d)
print(name)


prices = soup.find_all('div',class_='hZ3P6w DeU9vF')
#print(prices)
price = []
for i in prices[0:10]:
    d = i.get_text().replace("₹","").strip()
    price.append(d)
print(price)



ratings = soup.find_all('div',class_='MKiFS6')
#print(ratings)
rate = []
for i in ratings[0:10]:
    d = i.get_text()
    rate.append(float(d))
print(rate)

images = soup.find_all('img',class_='UCc1lI')
#print(images)
image = []
for i in images[0:10]:
    d = i['src']
    image.append(d)
print(image)

df = pd.DataFrame()
print(df)

df['Names'] = name
df['Prices'] = price
df['Ratings'] = rate
df['Images'] = image
print(df)

df.to_csv("Mobiles.csv")
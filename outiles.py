print("Jesus is the way and the truth and the life , Amen")
# باسم الثالوث القدوس اميني يا رب بشفاعة ام النور الطاهرة مريم و شفاعة جميع النفوس و شفاعة جميع القديسين و شفتعة جميع الملاءكة و شفاعة جميع التلاميذ و شفاعة جميع الاباء الكهنة و شفاعة جميع الاباء الرهبان و شفاعة جميع الرسل امين
import random
import requests
from bs4 import BeautifulSoup
from string import ascii_lowercase
from string import ascii_uppercase
random_number = random.choice([i for i in range(0,6)])
x = [i for i in ascii_lowercase ]
y = [i for i  in ascii_uppercase]
x.extend(y)
z = random.sample(x,5)
View = ["sea", "mountain", "city", "forest"]
Food = ['Pizza', 'Burger', 'Shawarma', 'Kabsa', 'Sushi', 'Pasta', 'Cupcake', 'Falafel', 'Koshari', 'Kebab', 'Taco', 'Biryani', 'Pie', 'Ramen', 'Samosa', 'Doner', 'Steak', 'Fried Fish', 'Molokhia', 'Ice Cream']

# Default locations if web scraping fails
Location = ["Egypt", "USA", "UK", "France", "Germany", "Japan", "China", "India", "Brazil", "Canada"]

try:
    # Try to get more locations from web
    response = requests.get("https://history.state.gov/countries/all", timeout=5)
    if response.status_code == 200:
        html_code = response.content
        tree_of_html = BeautifulSoup(html_code, 'html.parser')
        location_links = tree_of_html.find_all("a", href=True)
        Location = [link.text.capitalize() for link in location_links if link.text.strip()]
except:
    # Keep using default locations if web request fails
    pass

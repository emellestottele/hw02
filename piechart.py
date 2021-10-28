import matplotlib
import json
from matplotlib import pyplot as plt

with open('USD.json', encoding='ascii') as f:
    usd1 = f.read()
usd = json.loads(usd1)

countries = usd['rates'].keys()
countries = list(countries)
rates = usd['rates'].values()
rates = list(rates)

countries = countries[155:]
rates = rates[155:]

fig, ax = plt.subplots()
ax.pie(rates, labels=countries, autopct='%1.1f%%', shadow=True, startangle=90)
ax.axis('equal')
plt.title('Exchange Rate of USD')

plt.show()
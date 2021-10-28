import json
import matplotlib
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import rcParams as params

with open('GBP.json', encoding='ascii') as f:
    gbp1 = f.read()
gbp = json.loads(gbp1)

with open('USD.json', encoding='ascii') as f:
    usd1 = f.read()
usd = json.loads(usd1)

currency1 = {}
currency1['GBP'] = gbp['rates']['GBP']
currency1['AED'] = gbp['rates']['AED']
currency1['AFN'] = gbp['rates']['AFN']
currency1['AZN'] = gbp['rates']['AZN']
currency1['BGN'] = gbp['rates']['BGN']

currency2 = {}
currency2['USD'] = usd['rates']['GBP']
currency2['AED'] = usd['rates']['AED']
currency2['AFN'] = usd['rates']['AFN']
currency2['AZN'] = usd['rates']['AZN']
currency2['BGN'] = usd['rates']['BGN']

width = 0.25
x = np.arange(len(currency1.keys()))
fig, ax = plt.subplots()
rects1 = ax.bar(x - width / 2, currency1.values(), width, label = 'GBP Exchange Rates', color="blue")
rects1 = ax.bar(x - width / 2, currency2.values(), width, label = 'USD Exchange Rates', color="red")

ax.set_xlabel('Different Currencies')
ax.set_ylabel('Exchange Rate')
ax.set_xticks(x)
ax.set_xticklabels(currency1.keys())
ax.legend()
plt.title('GBP and US Exchange Rates')
params['font.family'] = 'fantasy'

plt.show()
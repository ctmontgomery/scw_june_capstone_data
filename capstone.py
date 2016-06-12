...
Chris and Swapnil
...

import pandas as pd
from matplotlib import pyplot as plt
dat = pd.read_csv("data/gapminder-FiveYearData.csv")

import pandas as pd
from matplotlib import pyplot as plt
dat = pd.read_csv("data/gapminder-FiveYearData.csv")
dat.head()
zim_dat = dat[dat['country'] == "Zimbabwe"]
zim_dat.plot (x='year', y='lifeExp')
zim_dat.hist()


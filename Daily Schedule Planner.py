#using panda library for the automation...

import pandas as pd
from datetime import datetime

df pd.read_csv('Planner.csv')

cd datetime.now()

filename = "Scheduler Export on + cd.strftime('%d-%m-%Y-%H-%M-%S.csv')

df.to_csv(filename, index = False)
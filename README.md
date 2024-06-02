# Daily-Schedule-Planner
The project I made using python for daily task schedule.

The following code is what I have used :-
import pandas as pd

from datetime import datetime

df pd.read_csv('Planner.csv')

cd datetime.now()

filename = "Scheduler Export on + cd.strftime('%d-%m-%Y-%H-%M-%S.csv')

df.to_csv(filename, index = False)

Then, just have to open Task Planner on Windows and schedule the tasks accordingly
Just put in the location of Python (which can be obtained by entering 'where python' in the code editor), location of file and name of the file.

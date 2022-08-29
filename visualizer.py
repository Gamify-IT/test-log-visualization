import matplotlib
matplotlib.use('TkAgg')
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import re


def testcase_to_minigame(testcase: str) -> str:
    return re.sub(r'^\s*u\.(.*)-\d+\s*$', r'\1', testcase)

tests = pd.read_csv('test-log.csv') # Read
tests['minigame'] = tests['Testcase'].apply(testcase_to_minigame) # "Group by" Testcase

sns.set(rc={"figure.figsize":(10, 2)}) #width=10, height=2
sns.color_palette("husl", 9) # More distinctive color palette
sns.catplot(x='Datum', y='Erfolg', hue='minigame', data=tests, s=15, kind="strip")
plt.show(block = True)

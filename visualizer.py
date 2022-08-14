import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import re


def testcase_to_minigame(testcase: str) -> str:
    return re.sub(r'^\s*u\.(.*)-\d+\s*$', r'\1', testcase)

tests = pd.read_csv('test-log.csv') # Read
tests['minigame'] = tests['Testcase'].apply(testcase_to_minigame) # "Group by"


sns.color_palette("husl", 9) # More distinctive color palette
sns.catplot(x='Datum', y='Erfolg', hue='minigame', data=tests)
plt.show(block = True)

# This file is created by Edwin
# For any changes please email me: edwin@git.com
# I added this file even more
import pandas as pd
import numpy as np

df = pd.read_csv("/usr/edwin/thefile.csv")
a = df.groupby("TEST")["Name"].sum()

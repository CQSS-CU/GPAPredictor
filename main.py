import pandas as pd
import numpy as np

# Headers derrived from: https://doi.org/10.7910/DVN/O35FW8
column_headers = ([
  "gender", 
  "race", 
  "physics", 
  "biology", 
  "history", 
  "foreign language", 
  "geography", 
  "literature", 
  "portuguese",
  "math",
  "chemistry",
  "mean GPA"
  ])

data = pd.read_csv("data/UFRGS_exam_gpa.csv", header = 0, names = column_headers)

from sklearn.model_selection import train_test_split

train_set, test_set = train_test_split(data, test_size=0.2)


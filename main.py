import pandas as pd
import numpy as np

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


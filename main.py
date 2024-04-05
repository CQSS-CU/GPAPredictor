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

# Adapted from "Hands-On Machine Learning" by Aurelian Geron (Ch. 2)
def shuffle_and_split_data(data, test_ratio):
    shuffled_indices = np.random.permutation(len(data))
    test_set_size = int(len(data) * test_ratio)
    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]

train_set, test_set = shuffle_and_split_data(data, 0.2)
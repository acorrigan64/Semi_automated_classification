from sklearn.svm import SVC
import re
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.multiclass import OneVsRestClassifier
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import seaborn as sns

"""
FILE IMPORTS
"""

path = #FILEPATH REMOVED FOR SECURITY REASONS
master_nvivo_df = pd.read_pickle(path)


"""
DATA CLEANING
"""

#Reading flags from the database, flags correspond to labels
nvivo_flags = master_nvivo_df.select_dtypes(include=['float64'])

# Get counts of code label use across database
nvivo_flags_counts = nvivo_flags.sum(axis = 0, skipna = True).to_frame(0).reset_index()
nvivo_flags_counts.columns=[['label','number']]

# need to get_level_values as comes from a created multui-index df
nvivo_flags_counts.columns=nvivo_flags_counts.columns.get_level_values(0)
label_count_df = nvivo_flags_counts.sort_values(['number'], ascending=False)
label_count_df.to_csv('label_count_df.csv',index=False)


"""
SORTING AND SELECTING TARGET LABELS
"""

#Sort codes from most to least popular
label_count_df_sorted = label_count_df.sort_values(by = 'number',ascending=False)

#Select the top 150 codes
label_count_df_sorted = label_count_df_sorted.iloc[1:150]
index_sorted = range(149)
label_sorted = label_count_df_sorted['label'].tolist()
target_dict = dict(zip(label_sorted, index_sorted))

#Assign text to the selected labels
numbers = []
texts_list = []

for var in target_dict.keys():
    print(' variable is ',var)
    # get columns of flag and text strings from coding
    var_df = master_nvivo_df[[var,var+'_atext']]
    # select only those rows with flag=1 (i.e. actual text)
    var_flag1_df = var_df[var_df[var] == 1]
    text = var_flag1_df[var+'_atext'].tolist()
    texts_list.append(text)
    
    x = len(var_flag1_df)
    print('number is ',target_dict[var])
    # create list from integer and copied by number of elements 
    l = [target_dict[var] ] * x
    numbers.append(l)
    
"""
PREPARING DATA FOR CLASSIFIER TRAINING
""" 

flat_list = [item for sublist in numbers for item in sublist]
variables_array = np.asarray(flat_list)
flat_texts_list = [item for sublist in texts_list for item in sublist]

#Using a simple count vectoriser
count_vect = CountVectorizer(max_df=0.95,min_df=2)
x_train_counts = count_vect.fit_transform(flat_texts_list)

#TF-IDF Transform to the word counts
tfidf_transformer = TfidfTransformer()
x_train_tfidf = tfidf_transformer.fit_transform(x_train_counts)
x_train_tfidf.shape

#Training and exporting model
from sklearn.svm import SVC
clf = SVC(kernel='linear',probability=True).fit(train_x, train_y)

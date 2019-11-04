import pickle
import sys
import pandas as pd
import numpy as np
import csv
from preprocess import process
from sklearn.linear_model import LogisticRegression

FILENAME = 'movie_metadata_filtered_aftercsv.csv'
np.set_printoptions(threshold=sys.maxsize)

def take_input():
    # imdb_score | num_critic_for_reviews | duration | director_facebook_likes |
    # actor_3_facebook_likes | cast_total_facebook_likes | budget | gross
    attributes = ["imdb_score","num_critic_for_reviews","duration","director_facebook_likes","actor_3_facebook_likes","movie_facebook_likes","num_voted_users","cast_total_facebook_likes","budget","gross"]
    means = [6, 140, 107, 686, 645,7500, 83500 ,9700, 39700000, 48460000]
    data = []
    for i in range(len(attributes)):
        print("Enter data (integer format) for {0} which has a mean of {1} -".format(attributes[i], means[i]))
        inp = str(input())
        while not inp.isdigit():
            print("please enter in integer format")
            inp = str(input())
        data.append(int(inp))
    with open("newdata.csv", "w") as newdata:
        newdata_writer = csv.writer(newdata)
        newdata_writer.writerow(attributes)
        newdata_writer.writerow(data)

def main():
    model = pickle.load(open('models/LogRegression_thre1'))
    # provide your filename here
    # take_input()
    process(filename='newdata.csv')
    datadf = pd.read_csv(FILENAME)
    datadf = datadf.drop(datadf.columns[[0]],axis=1)
    datadf_clean = pd.read_csv('cleaned_data.csv')
    datadf_clean = datadf_clean.drop(datadf_clean.columns[[0]],axis=1)
    datadf = (datadf-datadf_clean.mean())/(datadf_clean.max()-datadf_clean.min())
    print(datadf)
    X = np.array(datadf)
    print(X)
    predictions = model.predict(X)
    # consider the predicted rating to be in the range of +.- 1
    # for example of predicted is 7 then it may be between 6-8
    print predictions

if __name__ == '__main__':
    main()
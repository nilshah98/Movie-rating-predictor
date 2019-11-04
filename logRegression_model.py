import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle

np.random.seed(0)

FILENAME = 'movie_metadata_filtered_aftercsv.csv'
THRESHOLD_PREDICTION = 1

def _make_in_format(filename):
    datadf = pd.read_csv(filename)
    # separate classes and stuffs
    y = np.array(datadf['imdb_score'])
    # dropping the columns that we don't need in X
    datadf = datadf.drop(datadf.columns[[0]],axis=1)
    # normalizing the data- ie. between -1 and +1
    datadf = (datadf-datadf.mean())/(datadf.max()-datadf.min())
    X = np.array(datadf)
    return X,y

# pickling the data (model) -
'''
ie. storing it in a different file so as to not create model each time
stored at `models` folder
'''
def _pickle_it(model,filename):
    a = pickle.dumps(model)
    write_file = open('models/'+filename,'w')
    write_file.write(a)

def accuracy_score(y_test,predictions):
        correct = []
        for i in range(len(y_test)):
            if y_test[i]>=predictions[i]-THRESHOLD_PREDICTION and y_test[i]<=predictions[i]+THRESHOLD_PREDICTION:
                correct.append(1)
            else:
                correct.append(0)

        accuracy = sum(map(int,correct))*1.0/len(correct)
        return accuracy

# Creating and pickling Logistic regression model
def LogRegression():
    X,y = _make_in_format(FILENAME)
    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=1)
    model = LogisticRegression(solver='newton-cg',multi_class='ovr',max_iter=200,penalty='l2')
    model.fit(X_train,y_train)
    predictions = model.predict(X_test)
    _pickle_it(model,"LogRegression_thre1")
    print "LogRegression ",accuracy_score(y_test,predictions)*100

def main():
    LogRegression()

if __name__ == '__main__':
    main()
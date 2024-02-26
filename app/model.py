# -*- coding: UTF-8 -*-
import pickle
import gzip

#載入Model
with gzip.open('app/model/DecisionTree_1.pgz', 'r') as f:
    DecisionTree = pickle.load(f)

def predict(input):
    pred = DecisionTree.predict(input)[0]
    print(pred)
    return pred
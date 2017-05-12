#!/bin/bash

# Downloads the Tamilnadu Electricity Board Hourly Readings Data Set
# from UC Irvine Machine Learning repository
wget http://archive.ics.uci.edu/ml/machine-learning-databases/00290/eb.arff

# Move to Data Folder
mv eb.arff data/

#!/bin/bash

# Shuffle the data so that it's not organized by ID
shuf data/eb_stripped > data/eb_shuffled_stripped

# Split after every 2000 data points
split -l 2000 data/eb_shuffled_stripped

# Move files to data folder
find -name "x*" -exec mv -i {} -t data/split/ \;

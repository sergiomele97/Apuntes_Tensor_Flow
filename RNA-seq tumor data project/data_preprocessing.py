import pandas as pd
import numpy as np
import random


np.set_printoptions(precision=3, suppress=True)     # setting up numpy display
test_size = 200


training_data = pd.read_csv("data.csv")   # we charge the .csv using pandas
training_labels = pd.read_csv("labels.csv")

training_data.pop("Unnamed: 0")     # gets rid of the first column
training_labels.pop("Unnamed: 0")


training_data = np.array(training_data)     # converts pandas table into a numpy array
training_labels = np.array(training_labels)


tumordict = {
    "BRCA": 0,
    "KIRC": 1,
    "COAD": 2,
    "LUAD": 3,
    "PRAD": 4,
}


processed_labels = np.zeros((len(training_labels)), dtype=int)    # creates array full of 0's


for count1, label in enumerate(training_labels):                    # translates labels
    processed_labels[count1] = tumordict[label[0]]


testing_data = np.zeros((test_size, training_data.shape[1]))
testing_labels = np.zeros(test_size,  dtype=int)


random_pick = random.sample(range(801), test_size)      # Creating training and testing set
random_pick.sort(reverse=True)                          # We delete from bigger to smaller values
for count2, pick in enumerate(random_pick):

    testing_data[count2] = training_data[pick]
    testing_labels[count2] = processed_labels[pick]

    training_data = np.delete(training_data, pick, 0)
    processed_labels = np.delete(processed_labels, pick, 0)


np.save("training_data", training_data)
np.save("testing_data", testing_data)
np.save("training_labels", processed_labels)
np.save("testing_labels", testing_labels)

# loading = np.load("training_data.npy")

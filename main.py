from datasets import load_dataset
import numpy as np
import itertools
import text2vec

dataset = load_dataset("sst2")
train = np.array(dataset["train"].data["sentence"])
val = np.array(dataset["validation"].data["sentence"])
test = np.array(dataset["test"].data["sentence"])
print(train[0])

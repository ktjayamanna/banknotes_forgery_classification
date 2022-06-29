The dataset is from https://www.kaggle.com/datasets/ritesaluja/bank-note-authentication-uci-data Kaggle challenge.
The dataset was created by applying wavelet transform to photographs of banknotes and then calculate the features mentioned in the dataset by deriving the histogram of the dataset.
For the sake of this project, we limit the analysis of the data; We just derive a good enough model using random forest classification.
Then, we pickle the model and load into the Flask backend.
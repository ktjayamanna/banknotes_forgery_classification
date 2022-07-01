The dataset is from https://www.kaggle.com/datasets/ritesaluja/bank-note-authentication-uci-data Kaggle challenge.
The dataset has been created by applying wavelet transform to photographs of banknotes and then calculating the features mentioned in the dataset by deriving the histogram of the dataset.
For the sake of this project, we limit the analysis of the data; We just derive a good enough model using random forest classification (which already got ~98% accuracy).
Then, we pickle the model and load into the Flask backend.
We have created a quick UI with flasgger.
Then, we dockerized it.

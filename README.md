Recommender System

This tool for getting Recommender System like videos count prediction. A Random Forest model was used for training on a large dataset of 70 videos. Feature engineering, Data cleaning, Data selection. I've used many other techniques for this task.
Random Forest was chosen as the learning algorithm for modeling the Like counts predictions. It is an ensemble method were multiple base estimators (tree) are trained on subsamples of input data and give output after averaging the result of all estimators. Considering the size of dataset, computational power available and ability of estimator to fit data, this model was considered. The parameters of an algorithm always have an effect on it's performance. Grid Search and Cross Validation were used to tune the parameters for the model.

Tools Used
Python 3.6
Pandas
Sklearn
NumPy
Visualize ML

Create the dataset
1. Download the Recommender System case study videos from Google drive. Run python download_videos.py which relies on recommender system videos. Change the save dir in the script to where you want the full videos saved.
2. To extract the continuous video clips, run python videos and change input directory to be the directory containing the full videos and output directory to be the location to save the extracted clips.



Experiments
I have provided my code to train and evaluate the models in the experiments directory. I have the various models implemented in clip.py, a script to load the dataset, and a script to train the models as well.
I also include PyTorch implementation to the output clipoutput.py.
This script is used for training the model over training data (dataset/clipdata.csv) Because of Bootstrap Sampling in random forest the results might vary after every training process.

Issues
A very common issue comes with the pickling process which sometime leads to loss of information and different results every time.

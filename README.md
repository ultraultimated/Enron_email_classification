# csc522_project
ALDA Project code and reports

## Dataset
You can download the dataset from https://www.cs.cmu.edu/~enron/ 
We have used the May 7,2015 version of the dataset. Unzip the tar file and create a folder called dataset containing the folders present in the zip file.

## Data Extraction
For data extraction run extraction.ipynb which will load files from dataset folder and generate a strucutred csv file.
## Data preprocessing
This is used to ensure we do not have any forwarded chains in the emails.
1) processing.py
## Feature extraction
Follwing files are used for extraction of relevant features based on the 7 categories.

1) character_feature_extraction.py
2) paragraph_feature_extraction.py
3) punctutation_feature_extraction.py
4) word_feature_extraction.py
5) word_feature_ttr.py
6) sentence_feature_extraction.py
7) syntactic_feature_extraction.py
8) semantic_feature_extraction.py

## Hyperparameter tuning
* Enron_hyperparameter_tuning.ipynb

## Final models
### SVC, XGBoost, KNN, RFC
* Enron_report_generation.ipynb

### Hierarchical Attention Networks
HierBiLSTM_stylo.ipynb

## Final File
Run the following script to generate all the csv files and generate results for SVM,KNN and Random Forest Classifier.
* Enron_main.ipynb

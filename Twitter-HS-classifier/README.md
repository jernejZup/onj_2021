This is a POS tagging based program for offensive language detection.
The program classifies tweets from the provided dataset into three classes:
  - Offensive
  - Hatefull
  - Neither
The results of the algorithm using different models on the provided dataset is available in the [Reports](Reports/) directory.
And the confusion matrices are available in the [Confusion Matrices](Confusion%20Matrices/) directory.

The program (run Twitter_HS_classifier.py) goes through several phases:
  - Tokenization
  - Data preprocessing
    -  Stemming
    -  Lematization
    -  Stop word removal
  - n-gram feature extraction
  - Classification (in Twitter_HS_classifier.py try ussing different classifiers)
    - the code is already prepared and can be modified in the Twitter_HS_classifier.py file from line 453 - 464
  - Representation of results

To succesfully run the program you will need the following Python libraries:
  - Numpy
  - Pandas
  - Scikit Learn
  - vaderSentiment
  - textstat
  - matplotlib

There is a possibility that NLTK will ask you to download some dependencies when running the program for the first time, you can download them like this: 

'''
nltk.download('Wordnet').
'''

For the provided results we used the provided dataset on which we used our algorithm which was implemented in Python 3.8 and tested in PyCharm IDE.

We hope you will have fun with our program.

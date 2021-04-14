This is a TF-IDF based program for offensive language detection.

The program goes through several phases:
  - Removing noise from data
  - Tokenizing data
  - Removing stop words from data
  - Stemming and Lemmatization
  - Classification

For classification we used the following classifiers:
  - Multinomial Naive Bayes
  - Gaussian Naive Bayes
  - Complement Naive Bayes
  - Bernoulli Naive Bayes
  - KNN
  - Decision Tree
  - Random Forest
  - Logistic Regression

And for the data we used the english Offenseval twitter dataset.
The dataset is divided into three subtasks, which are:
  - A: Offensive languge identification
  - B: Automatic categorization of offense types
  - C: Offense target identification

Where our program takes these subtasks into account and does the classification according to them.

To succesfully run the program you will need the following Python libraries:
  - NLTK
  - Scikit Learn
  - Pandas
  - Numpy
  - tqdm

We hope you will have fun with our program.

This is a TF-IDF based program for offensive language detection.

The program (run app.py) goes through several phases:
  - Removing noise from data
  - Tokenizing data
  - Removing stop words from data
  - Stemming and Lemmatization
  - Classification (in app.py try ussing different classifiers with their tags: KNN, MNB, LR, DT, RF, ...)

To succesfully run the program you will need the following Python libraries:
  - NLTK
  - Scikit Learn
  - Pandas
  - Numpy
  - tqdm

There is a possibility that NLTK will ask you to download some dependencies when running the program for the first time, you can download them like this: nltk.download('Wordnet').

We hope you will have fun with our program.

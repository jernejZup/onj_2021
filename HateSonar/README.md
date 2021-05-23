HateSonar allows you to detect hate speech and offensive language in text, without the need for training. There's no need to train the model. You have only to fed text into HateSonar. It detects hate speech with the confidence score.

Our program goes trough several phases:
1. It reads the file and saves text in to an array
2. It analyses the array element by element with hatesonar which produces a hate, offensive and neither scores
3. It just sums up the scores and prints them out

Hate sonar is only designed to work with English!

To install hate sonar just use pip:
pip install hatesonar

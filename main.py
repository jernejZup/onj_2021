from hatesonar import Sonar

import warnings

warnings.filterwarnings('ignore')


def hate_speech_classifier(textArray,Class,hate,offensive,neither,sonar):
    for i in textArray:
        sonar_dict=sonar.ping(text=i)
        Class.append(list(sonar_dict.values())[1])
        hate.append(list(list(sonar_dict.values())[2][0].values())[1])
        offensive.append(list(list(sonar_dict.values())[2][1].values())[1])
        neither.append(list(list(sonar_dict.values())[2][2].values())[1])
    print("finished classifying")


def readFile(filename="data/reddit.csv"):
    file1=open(filename,'r')
    Lines=file1.readlines()
    print("There are {} lines in file {}".format(len(Lines),filename))
    return Lines


def displayResaults(hate,offensive,neither):
    nHateOffensive,nNeither=0,0
    if len(hate) != len(offensive) != len(neither):
        print("something went wrong")
        return
    else:
        for tweet in range(len(hate)):
            if hate[tweet] > neither[tweet]:
                nHateOffensive=nHateOffensive + 1
            elif offensive[tweet] > neither[tweet]:
                nHateOffensive=nHateOffensive + 1
            else: nNeither=nNeither + 1

    print("there were:\nhateful & offensive:{}\nneither:{}".format(nHateOffensive,nNeither))


def main():
    sonar=Sonar()

    textArray=readFile()

    Class=[]
    hate=[]
    offensive=[]
    neither=[]

    hate_speech_classifier(textArray,Class,hate,offensive,neither,sonar)
    displayResaults(hate,offensive,neither)


if __name__ == '__main__':
    main()

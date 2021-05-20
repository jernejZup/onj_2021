import pandas as pd
from transformers import AutoTokenizer, AutoModelForMaskedLM,AutoConfig
import torch

def readFile(filename="slo_twitter_filterd_comma.csv"):
    col_list=["Text","Class"]
    df=pd.read_csv(filename)
    for tweet in df.values:
        print(tweet[0])
    return df.values[:,0]


# def main():
#     print("started")
#     tviti=readFile()
#     print("pripravljam bert-a")
#     tokenizer=AutoTokenizer.from_pretrained("EMBEDDIA/sloberta",use_fast=False)
#     config=AutoConfig.from_pretrained("EMBEDDIA/sloberta")
#     print("končal priprave")
#     model=AutoModelForMaskedLM.from_config(config)
#
#
#     sequence="klinc te gleda"
#
#     tokenized_sequence = tokenizer.tokenize(sequence)
#     print(tokenized_sequence)
#
#     outputs=model(tokenized_sequence)
#
#     print("finished")
#
# if __name__ == '__main__':
#     main()


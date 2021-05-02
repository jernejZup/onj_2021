import json

f=open('data/fox-news-comments.json',)
data=json.load(f)

out = open("data/fox_cleaned_output.csv","a")


for tvit in data:
    out.write(tvit['text']+'\n')

f.close()
out.close()
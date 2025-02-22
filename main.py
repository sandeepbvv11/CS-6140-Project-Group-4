import numpy as np
import pandas as pd
import json, os
import spacy


nlp = spacy.load('en_core_web_md')


def load_emojis():
    rows = []
    with open('./emojis.json/emojis.json') as f:
        for emoji in json.loads(f.read()):
            rows.append([emoji['name'], emoji['unicode'], ' '.join(emoji['keywords']), emoji['definition']])
    return np.array(rows)


emojis = load_emojis()
df = pd.DataFrame(emojis, columns=['name', 'unicode', 'keywords', 'definition'])
print(df['unicode'].head())
sentencevector = []
count = 0
for i in range(len(emojis)):
    desc = df['definition'][i] + df['name'][i]
    token = nlp(desc)
    vecs = [t.vector for t in token]
    print(desc)
    mean_vec = np.average(vecs)
    sentencevector.append(mean_vec)
    count=count+1
print(len(sentencevector), count)
print(sentencevector)
np.save("vector.npy", sentencevector)
# print(df['definition'])
file = open('vocab.txt', 'w')
for i in df['unicode']:
    file.write(i)
    file.write('\n')
file.close()

with open("train.tsv",'r',encoding="utf-8") as f:
    text= f.read()
import jieba
import jieba.posseg as pesg
#jieba分词
words = jieba.lcut(text)
print("/".join(words))
#统计词频
from collections import Counter
counts = Counter(words)
for word,count in counts.items():
    print(f"{word}:{count}")
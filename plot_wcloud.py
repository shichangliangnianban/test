# 使用jieba中的词性标注功能
import jieba.posseg as pseg
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def get_adj_list(text):
    """用于获取形容词列表"""
    # 使用jieba的词性标注方法切分文本，获取word，词性
    # 通过判断词性是否为形容词，来返回对应的词汇
    datas = []
    for w in pseg.lcut(text):
        if w.flag=="a":
            datas.append(w.word)
    return datas


def get_word_cloud(keywords_list):
    # 实例化绘制词云的类
    wordcloud=WordCloud(font_path='SimHei.ttf',max_words=100,background_color='white')
    # 将传入的列表转换为词云生成器所需要的字符格式
    keywords_string=" ".join(keywords_list)
    # 生成词云
    wordcloud.generate(keywords_string)
    # 绘制图像并显示
    plt.figure()
    plt.imshow(wordcloud,interpolation='bilinear')
    plt.axis("off")
    plt.show()

import jieba
from itertools import chain
import pandas as pd
# 获取训练集的数据
train_data = pd.read_csv("train.tsv",sep='\t')
# 获取测试集的数据
test_data = pd.read_csv("dev.tsv",sep='\t')
# chain方法用于扁平化列表
# print(*map(lambda x:jieba.lcut(x),train_data["sentence"]))
# print(set(chain(*map(lambda x:jieba.lcut(x),train_data["sentence"]))))
# 获取训练集的句子进行分词之后不同的词的集合，set可以去重
train_vocab=set(chain(*map(lambda x:jieba.lcut(x),train_data["sentence"])))
# print(len(train_vocab))
# 获取验证集的句子进行分词之后不同的词的集合
valid_vocab=set(chain(*map(lambda x:jieba.lcut(x),test_data["sentence"])))

print(len(train_vocab))
print(len(valid_vocab))

print('********************************************************************')
# 获取训练集上正样本
p_train_data = train_data[train_data['label']==1]['sentence']
# 获取正样本的每个句子的形容词
train_p_a_vocab=chain(*map(lambda x:get_adj_list(x),p_train_data))

#获取训练集的负样本
n_train_data= train_data[train_data['label']==0]['sentence']
#获取负样本的每个句子的形容词
train_n_a_vocab=chain(*map(lambda x:get_adj_list(x),n_train_data))

get_word_cloud(train_p_a_vocab)
get_word_cloud(train_n_a_vocab)

print('********************************************************************')
# 获取测试集上正样本
p_test_data = test_data[test_data['label']==1]['sentence']
# 获取正样本的每个句子的形容词
test_p_a_vocab=chain(*map(lambda x:get_adj_list(x),p_test_data))

#获取测试集的负样本
n_test_data= test_data[test_data['label']==0]['sentence']
#获取负样本的每个句子的形容词
test_n_a_vocab=chain(*map(lambda x:get_adj_list(x),n_test_data))

get_word_cloud(test_p_a_vocab)
get_word_cloud(test_n_a_vocab)




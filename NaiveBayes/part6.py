

import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
ftable = pd.read_csv('ftable.csv')
ftable = ftable[ftable['word'] != 'sad']
ftable = ftable[ftable['word'] != 'sad,']
ftable = ftable[ftable['word'] != ':(']
ftable = ftable[ftable['word'] != 'fun']
ftable = ftable[ftable['word'] != 'happy,']
ftable = ftable[ftable['word'] != 'happy']
ftable = ftable.drop_duplicates(subset = 'word')
positive_instance = 24070.0
negative_instance = 23930.0
pos_count = 0
neg_count = 0


# test = " i'm tryna talk to you'"
# test = " i'm tryna talk to you'"
with open('test.csv','r') as test_csv:
    test_reader=csv.reader(test_csv)

    for line in test_reader:
        if line:
            test=line[1]
            print(test)
        
        
            #split all the words in my text
            test_words = test.split()

            prob_positive = float(positive_instance/(positive_instance+negative_instance))
            prob_negative = 1 - prob_positive
            # print(prob_positive)
            pos_word = 1.0*prob_positive
            neg_word = 1.0*prob_negative
            # print(neg_word)
            for i in range(len(test_words)):
                word = test_words[i]
                #print(word)
                index_val = ftable.index[ftable['word'] == word]
                if (len(index_val) > 0):
                    #print(index_val[0])
                    pos_val = ftable['positive'].iloc[index_val[0]]
                    # print("pos_val")
                    # print(pos_val)
                    neg_val = ftable['negative'].iloc[index_val[0]]
                    # print("neg_value")
                    # print(neg_val)
                    pos_word = pos_word * pos_val/positive_instance
                    # print("pos_word")
                    # print(pos_word)
                    neg_word = neg_word * neg_val/negative_instance
                    # print("neg_word")
                    # print(neg_word)
            pos1=pos_word/(pos_word+neg_word)
            if neg_word!=0:
                pos2=neg_word/(pos_word+neg_word)
            else:
                pos2=neg_word
            if pos_word > neg_word:
                print("The sentence is POSITIVE, with a probability of")
                print(pos1)
                pos_count=pos_count+1

            # elif pos_word == neg_word:
            #     print("The sentence was Neutral")
                
            else:
                print("The sentence is NEGATIVE, with a probability of")
                print(pos2)
                neg_count=neg_count+1
                
            probab=[pos1,pos2]
            exp=[0.2,0]
            label_prob=['Positive','Negative']
            plt.pie(probab,labels=label_prob,explode=exp,autopct='%2.1f%%')
            plt.show()
            # plt.savefig('graph.png')

            #print(pos_word)
            #print(neg_word)
prob=['Positive','Negative']
prob_value=[pos_count,neg_count]
ypos=np.arange(len(prob))
plt.xticks(ypos,prob)
plt.ylabel("Tweet(Number)")
plt.title("Twiter Sentiment Analysis")
plt.bar(ypos,prob_value)
plt.show()
# print(pos_count)
# print(neg_count)


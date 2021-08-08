from django.shortcuts import render, redirect
from .models import Dashboard
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
import pandas as pd
import numpy as np
import csv 

# Create your views here.
def configure(request):
	return render(request, 'dashboard/configure.html')

def analysis(request):
	if request.method == 'POST':
		test = request.POST['title']
		ftable = pd.read_csv ('ftable.csv')
		ftable = ftable[ftable['word'] != 'sad']
		ftable = ftable[ftable['word'] != 'sad,']
		ftable = ftable[ftable['word'] != ':(']
		ftable = ftable[ftable['word'] != 'fun']
		ftable = ftable[ftable['word'] != 'happy']
		ftable = ftable[ftable['word'] != 'happy,']
		ftable = ftable.drop_duplicates(subset='word')

		positive_instance = 24070.0
		negative_instance = 23930.0

		test_words = test.split()

		prob_positive = float(positive_instance / (positive_instance + negative_instance))
		prob_negative = 1 - prob_positive

		pos_word = 1.0 * prob_positive
		neg_word = 1.0 * prob_negative
		for i in range(len(test_words)):
			word = test_words[i]

			index_val = ftable.index[ftable['word'] == word]
			if len(index_val) > 0:

				pos_val = ftable['positive'].iloc[index_val[0]]
				print(pos_val)
				neg_val = ftable['negative'].iloc[index_val[0]]
				print(neg_val)
				pos_word = pos_word * pos_val / positive_instance
				neg_word = neg_word * neg_val / negative_instance

		if pos_word > neg_word:
			messages.info(request, 'The Sentence'+'  '+'['+ test + ']'+'  '+'is POSITIVE, with a probability of '+ (str((pos_word / (pos_word + neg_word)))))
			return render(request, 'dashboard/analysis.html')
		else:
			messages.info(request, 'The Sentence'+'  '+'['+ test + ']'+'  '+'is NEGATIVE, with a probability of '+ (str((neg_word / (neg_word + pos_word)))))
			return render(request, 'dashboard/analysis.html')

					
	else:
		return render(request, 'dashboard/analysis.html')

	

def history(request):
	return render(request, 'dashboard/history.html')


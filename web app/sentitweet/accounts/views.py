#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
import pandas as pd
import numpy as np
import csv 




# Create your views here.

def login(request):


    if request.method == 'POST':
        test = request.POST['username']
        ftable = pd.read_csv ('ftable.csv')
        ftable = ftable[ftable['word'] != 'sad']
        ftable = ftable[ftable['word'] != 'sad,']
        ftable = ftable[ftable['word'] != ':(']
        ftable = ftable[ftable['word'] != 'fun']
        ftable = ftable[ftable['word'] != 'happy,']
        ftable = ftable[ftable['word'] != 'happy']
        ftable = ftable.drop_duplicates(subset='word')

        positive_instance = 24070.0
        negative_instance = 23930.0

        # split all the words in my text

        test_words = test.split()

        prob_positive = float(positive_instance / (positive_instance
                              + negative_instance))
        prob_negative = 1 - prob_positive

        pos_word = 1.0 * prob_positive
        neg_word = 1.0 * prob_negative
        for i in range(len(test_words)):
            word = test_words[i]

            # print(word)

            index_val = ftable.index[ftable['word'] == word]
            if len(index_val) > 0:

                # print(index_val[0])

                pos_val = ftable['positive'].iloc[index_val[0]]
                neg_val = ftable['negative'].iloc[index_val[0]]
                pos_word = pos_word * pos_val / positive_instance
                neg_word = neg_word * neg_val / negative_instance

        if pos_word > neg_word:
            messages.info(request, 'The sentence is POSITIVE, with a probability of '+ (str((pos_word / (pos_word + neg_word)))))
			
            
			
			
        else:
            messages.info(request, 'The sentence is NEGATIVE, with a probability of '+ (str((neg_word / (pos_word + neg_word)))))
            
			
		
		
        return render(request, 'accounts/login.html')	
		
    else:

           # password = request.POST['password']

           # user = User.objects.create_user(username=username,password=password)
           # user.save()
           # user1 =auth.authenticate(username=username, password=password)
           # if user1 is not None:
           #   auth.login(request,user1)
           #   return redirect('dashboard')
           # else:
           # ....return redirect('login')

        return render(request, 'accounts/login.html')
def userlog(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username,password=password)
    if user is not None:
      auth.login(request, user)
      return render(request, 'accounts/dashboard.html')
    else:
      messages.info(request,'invalid credentials')
      return redirect('userlog')
  else:
    return render(request, 'accounts/userlog.html')

def logout(request):
    return redirect('index')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')



			
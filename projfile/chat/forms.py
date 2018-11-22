from django.forms import ModelForm
from home.models import chat_vocab_t
from django import forms
import datetime

class ChatVocabForm(ModelForm):
        class Meta:
                    model = chat_vocab_t
                            fields = ['vocab','date','side']


                            

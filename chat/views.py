from django.views.generic import TemplateView ,CreateView, ListView, DetailView, DeleteView, UpdateView
from chatterbot.ext.django_chatterbot import settings
from django.http import JsonResponse, HttpResponse
from chat.form.forms import ChatMessageForm
from django.urls import reverse_lazy
from django.db.models.signals import post_save
from django.shortcuts import render
from chat.models import Message, ChatSession
from chatterbot import ChatBot
import requests
import json

def get_next_message(request){
    #get previous messeg from api call
    if(request.method == "GET"){
        latest_entry = Message.objects.latest('created_at')
    }
}

def enter_message(request){
    if(request.method == "POST"){
        new_entry = Message.objects.latest("created_at")
    }
}

# Create your views here.
class ChatSessionTemplateView(TemplateView):
    template_name='chatume.html'

#list comments
class ChatSessionListView(ListView):
    model = Message
    template_name= 'chatume_messages.html'

#creates api endpont to interact with chatterbot
class ChatSessionCreateView(CreateView):
    form_class = ChatMessageForm
    template_name = 'chat_form.html'

class ChatSessionDetailView(DetailView):
    model = Message

class ChatSessionDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('chatume_messages')

class ChatSessionUpdateView(UpdateView):
    model = Message
    fields = ["text", "bot"]



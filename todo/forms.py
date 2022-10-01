from typing import ClassVar
from todo.models import Todo, Contact
from django import forms

class TodoForm(forms.ModelForm):
    class Meta:
        model=Todo
        fields={"title","description","name","email"}


class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields={"name","subject","email","message","phone_no"} 



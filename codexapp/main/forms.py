from django.forms import ModelForm
from codexapp.main.models import List, Prompt

class ListForm(ModelForm):
    class Meta:
        model = List
        exclude = ('mc_list_id',)

class PromptForm(ModelForm):
    class Meta:
        model = Prompt
        exclude = ('mc_campaign_id',)
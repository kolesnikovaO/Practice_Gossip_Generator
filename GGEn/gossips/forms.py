from django import forms
from .models import Gossip
from .models import Character

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class GossipForm(forms.ModelForm):
    """ch_name = forms.CharField(max_length=30)
    ttl = forms.EmailField(max_length=254)
    gos_text = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(),
        help_text='Write here your message!'
    )"""
    class Meta:
        model = Gossip
        fields = ('gossip_text','expire_date','character_id')

class CharForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ('name','about')

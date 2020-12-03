from django import forms
from .models import Post, Apply

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'contents',)

class ApplyForm(forms.ModelForm):
    
    class Meta:
        model = Apply
        fields = ('gender','age','height','weight','waist','bp_judge','pulse_count_judge','bp_gluc','bt_chol','bt_trig','bt_hb','bt_hbsa','bt_crea','bt_sgot','bt_sgpt','bt_rgpt','smoke_flag','drinking_flag',)

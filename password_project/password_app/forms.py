from django import forms

class PasswordForm(forms.Form):
    word_1 = forms.CharField(label="Enter favourite word 1")
    word_2 = forms.CharField(label="Enter favourite word 2")
    word_3 = forms.CharField(label="Enter favourite word 3")
    word_4 = forms.CharField(label="Enter favourite word 4")
    word_5 = forms.CharField(label="Enter favourite word 5")
    number_1 = forms.CharField(label="Enter favourite number 1")
    number_2 = forms.CharField(label="Enter favourite number 2")
    key = forms.CharField(label="Enter key", required=False)

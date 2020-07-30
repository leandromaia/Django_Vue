from django import forms


class TestForm(forms.Form):
    name = forms.CharField(label='Name', max_length=200)
    content = forms.CharField(widget=forms.Textarea)
    boolean = forms.BooleanField()
    image = forms.ImageField(widget=forms.FileInput)

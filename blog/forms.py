from django import forms
class ContactForm(forms.Form):
    #name = forms.CharField(label="Name",widget=forms.TextInput(attrs={'class' : 'col2'}))
    name = forms.CharField(label="Name:",max_length=100)
    #name.widget = forms.Label(attrs={'class': 'col2',})
    #name.widget = forms.TextInput(attrs={'class': 'col2',})
    #name.render('class','col1 first')
    #name = forms.TextInput(attrs={'size': 10, 'title': 'Name:',})
    sender = forms.EmailField(label="Email:")
    message = forms.CharField(widget=forms.Textarea(attrs={'rows':'5'}))

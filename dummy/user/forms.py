from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'style': '''position: relative;
                    top:10px;
                    left:390px;
                    border: 2px solid white;
                    border-radius: 4px;
                    box-shadow: 0px 0px 100px violet;''',
        }))
    password = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={
        'style':'''position: relative;
                    top:10px;
                    left:390px;
                    border: 2px solid white;
                    border-radius: 4px;
                    box-shadow: 0px 0px 100px skyblue;''',
    }))


class SignupForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'style': '''position: relative;
                    top:10px;
                    left:390px;
                    border: 2px solid white;
                    border-radius: 4px;
                    box-shadow: 0px 0px 100px violet;''',
        }))
    fname = forms.CharField(widget=forms.TextInput(attrs={
        'style': '''position: relative;
            top:10px;
            left:390px;
            border: 2px solid white;
            border-radius: 4px;
            box-shadow: 0px 0px 100px white;
            color: black;''',
        }))
    lname = forms.CharField(widget=forms.TextInput(attrs={
        'style': '''position: relative;
            top:11px;
            left:390px;
            border: 2px solid white;
            border-radius: 4px;
            box-shadow: 0px 0px 100px skyblue;
            color: black;''',
        }))
    password = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={
        'style': '''position: relative;
            top:15px;
            left:390px;
            border: 2px solid white;
            border-radius: 4px;
            box-shadow: 0px 0px 100px lightgreen;
            color: black;''',
        }))
    confirm_password = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={
        'style': '''position: relative;
            top:8px;
            left:390px;
            border: 2px solid white;
            border-radius: 4px;
            box-shadow: 0px 0px 100px orange;
            color: black;''',
        }))

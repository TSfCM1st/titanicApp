from django import forms

class TitanicForm(forms.Form):
    Id = forms.IntegerField(label='Id')
    Pclass = forms.IntegerField(label='Pclass', required=True)
    Name = forms.CharField(label='Name', required=False)
    Sex = forms.ChoiceField(label='Sex', choices=[(1, 'male'), (0, 'female')], required=True)
    Age = forms.IntegerField(label='Age', required=False)
    SibSp = forms.IntegerField(label='SibSp', required=True)
    Parch = forms.IntegerField(label='Parch', required=True)
    Ticket = forms.CharField(label='Ticket',required=False)
    Fare = forms.FloatField(label='Fare', required=False)
    Cabin = forms.CharField(label='Cabin', required=False)
    Embarked = forms.ChoiceField(label='Embarked', choices=[('S', 'S'), ('C', 'C'), ('Q', 'Q')])
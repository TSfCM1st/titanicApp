from django.shortcuts import render
from django.http import HttpResponse
from .forms import TitanicForm
from .ai import AiMdels

def index(request):
    params = {
        'title': 'タイタニックLinearSVCによる予想',
        'message': 'タイタニック号の乗客の特性を入力してください',
        'form': TitanicForm()
    }

    if (request.method == 'POST'):
        data = [[
            request.POST['Id'],
            request.POST['Pclass'],
            request.POST['Name'],
            request.POST['Sex'],
            request.POST['Age'],
            request.POST['SibSp'],
            request.POST['Parch'],
            request.POST['Ticket'],
            request.POST['Fare'],
            request.POST['Cabin'],
            request.POST['Embarked']
            ]]

        params['message'] = 'PassengerId' + request.POST['Id'] + \
            '<br>Pclass: ' + request.POST['Pclass'] + \
            '<br>Name: ' + request.POST['Name'] + \
            '<br>Sex: ' + request.POST['Sex'] + \
            '<br>Age: ' + request.POST['Age'] + \
            '<br>SibSp: ' + request.POST['SibSp'] + \
            '<br>Parch; ' + request.POST['Parch'] + \
            '<br>Ticket: ' + request.POST['Ticket'] + \
            '<br>Fare: ' + request.POST['Fare'] + \
            '<br>Cabin: ' + request.POST['Cabin'] + \
            '<br>Embarked: ' + request.POST['Embarked'] + \
            '<br>なら乗客の生死は…！！！   ' + \
            '<br>' + str(AiMdels(data))

        params['form'] = TitanicForm(request.POST)
    return render(request, 'titanicai/index.html', params)
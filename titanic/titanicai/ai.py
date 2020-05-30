import pickle
import pandas as pd

def AiMdels(data):

    with open('titanicai/LinearSVC.pickle', 'rb') as f:
        clf_pickle = pickle.load(f)

    with open('titanicai/LinearSVC_SC.pickle', 'rb') as f:
        sc_pickle = pickle.load(f)

    _df = pd.DataFrame(data, columns=['PassengerId', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp','Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'])
    _df = _df.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1)  # 不要カラムの削除
    _df['Age'] = _df['Age'].fillna(28.0)  # Ageカラムの欠損値埋め
    _df['Pclass'] = pd.Categorical(_df['Pclass'], categories=[1, 2, 3])
    _df['Embarked'] = pd.Categorical(_df['Embarked'], categories=['C', 'Q', 'S'])
    _df['Sex'] = pd.Categorical(_df['Sex'], categories=['female', 'male'])
    _df = pd.get_dummies(_df, columns=['Sex'], drop_first=True)
    _df = pd.get_dummies(_df, columns=['Pclass', 'Embarked'])

    X_std = sc_pickle.transform(_df)  #標準化
    answer = clf_pickle.predict(X_std)  #jupyterで作った学習済モデルで予測

    return answer[0]
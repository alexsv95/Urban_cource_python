import requests as req
import matplotlib.pyplot as plt
import pandas as pd

langs = ['python', 'java', 'go', "C#", "PHP"]

def counting_repositories(langs: list):
    count_rep = {}
    for l in langs:
        params = {'q' : l}
        r = req.get('https://api.github.com/search/repositories', params=params)
        r_json = r.json()
        count_rep[l] = r_json['total_count']
    return count_rep

class Dashboard:
    def __init__(self, data):
        self.data = data

    def created_pie(self):
        plt.title('Кол-во репозиторий в GitHub')
        plt.pie(self.data.values(), labels=self.data, autopct='%1.1f%%')
        plt.show()

    def created_bar(self):
        plt.title('Кол-во репозиторий в GitHub')
        res = pd.Series(self.data)
        plt.bar(res.index, height=res)
        plt.show()

langs_rep = counting_repositories(langs)
dash = Dashboard(langs_rep)
dash.created_bar()
dash.created_pie()
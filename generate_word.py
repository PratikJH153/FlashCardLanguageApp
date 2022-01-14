import pandas as pd


class GenerateWord:
    def __init__(self):
        self.words = {}
        self.get_data()

    def get_data(self):
        data = pd.read_csv("data/french_words.csv")
        for i in range(len(data)):
            self.words[data.iloc[i]["French"]] = data.iloc[i]["English"]

        print(self.words)


generate_words = GenerateWord()

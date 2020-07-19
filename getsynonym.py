import json

def getsynonym(word):
    with open("synonyms.json") as f:
        synonyms = json.load(f)

    print(synonyms[word])

if __name__ == "__main__":
    getsynonym("bear")
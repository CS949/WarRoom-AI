from services.database import decisions

documents = decisions.find()

for doc in documents:
    print(doc)

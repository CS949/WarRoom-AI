from services.database import (
decisions_collection
)

print("\nDocuments in database:\n")

for doc in decisions_collection.find():

    print(doc)

    print(
        "\n" + "=" * 100 + "\n"
    )

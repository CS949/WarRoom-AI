def calculate_scores(
agents
):


    positive_words = [

        "opportunity",
        "proceed",
        "growth",
        "benefit",
        "advantage",
        "recommend"

    ]

    negative_words = [

        "risk",
        "uncertain",
        "concern",
        "failure",
        "problem",
        "challenge"

    ]

    positive = 0
    negative = 0

    for response in agents.values():

        text = response.lower()

        for word in positive_words:

            if word in text:
                positive += 1

        for word in negative_words:

            if word in text:
                negative += 1

    total = positive + negative

    if total == 0:

        return (
            50,
            50
        )

    consensus = int(
        (positive / total) * 100
    )

    conflict = 100 - consensus

    return (
        consensus,
        conflict
    )


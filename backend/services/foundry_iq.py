VECTOR_MEMORY = {

    "ev": [

        "Electric Vehicle Infrastructure",

        "Government subsidies",

        "Energy transition"

    ],

    "japan": [

        "Ageing population",

        "Strong sustainability policies",

        "Advanced infrastructure"

    ],

    "india": [

        "Large population",

        "Rapid urbanization",

        "Government incentives"

    ],

    "startup": [

        "Funding risk",

        "Scalability opportunity",

        "Market competition"

    ],

    "healthcare": [

        "Patient safety",

        "Privacy compliance",

        "Accessibility"

    ],

    "education": [

        "Digital inclusion",

        "Accessibility",

        "Scalability"

    ],

    "ai": [

        "Responsible AI",

        "Ethics",

        "Data privacy"

    ]

}


def get_foundry_context(
    decision
):

    decision_lower = (
        decision.lower()
    )

    context = []

    for keyword, knowledge in VECTOR_MEMORY.items():

        if keyword in decision_lower:

            context.extend(
                knowledge
            )

    context.extend([

        "Evaluate market opportunities",

        "Evaluate financial feasibility",

        "Evaluate scalability",

        "Evaluate compliance risks",

        "Evaluate operational risks",

        "Evaluate long-term sustainability"

    ])

    return "\n".join(

        list(

            dict.fromkeys(

                context

            )

        )

    )
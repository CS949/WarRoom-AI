from services.openai_client import (
    client,
    MODEL_NAME
)


def generate_moderator_report(
    decision,
    agents
):

    ceo = agents.get(
        "CEO Agent",
        ""
    )

    cfo = agents.get(
        "CFO Agent",
        ""
    )

    cto = agents.get(
        "CTO Agent",
        ""
    )

    marketing = agents.get(
        "Marketing Agent",
        ""
    )

    legal = agents.get(
        "Legal Agent",
        ""
    )

    risk = agents.get(
        "Risk Agent",
        ""
    )

    prompt = f"""
You are the Moderator Agent for WarRoom AI.

Decision:
{decision}

CEO Agent:
{ceo}

CFO Agent:
{cfo}

CTO Agent:
{cto}

Marketing Agent:
{marketing}

Legal Agent:
{legal}

Risk Agent:
{risk}

Return your response in EXACT markdown format.

# Areas of Agreement

• Point

• Point

# Areas of Disagreement

• Point

• Point

# Biggest Opportunities

• Point

• Point

# Biggest Risks

• Point
• Point

# Final Board Recommendation

One concise executive recommendation.

Maximum 250 words.
"""

    response = client.chat.completions.create(

        model=MODEL_NAME,

        messages=[

            {
                "role": "system",

                "content":
                "You are an expert board meeting moderator."
            },

            {
                "role": "user",

                "content":
                prompt
            }

        ],

        temperature=0.3

    )

    return (
        response
        .choices[0]
        .message
        .content
    )
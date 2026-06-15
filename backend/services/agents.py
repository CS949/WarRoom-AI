from services.openai_client import (
client,
MODEL_NAME
)

def run_agent(
role,
decision,
context=""
):

    prompt = f"""

{role}

Decision:
{decision}

Context:
{context}

You must ONLY think from your assigned role.

You are allowed to disagree with other executives.

Return your response in EXACT markdown format:

## Opinion

One short paragraph.

## Benefits

• Benefit 1

• Benefit 2

• Benefit 3

## Risks

• Risk 1

• Risk 2

• Risk 3

## Recommendation

One short paragraph.

Keep the response under 150 words.
"""

    response = client.chat.completions.create(

        model=MODEL_NAME,

        messages=[
            {
                "role": "system",
                "content":
                f"You are a professional {role}."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.7

    )

    return (
        response
        .choices[0]
        .message
        .content
    )

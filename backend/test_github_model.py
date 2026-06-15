from services.openai_client import (
client,
MODEL_NAME
)

response = client.chat.completions.create(


model=MODEL_NAME,

messages=[
    {
        "role": "user",
        "content":
        "Say hello from GitHub Models."
    }
]


)

print(
response.choices[0].message.content
)

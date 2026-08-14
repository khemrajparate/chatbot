from google import genai
from google.genai import types

# Your Gemini API key
API_KEY = "AQ.Ab8RN6Jn-fZe6C1OTHPj8VBcv4UUS6dZCVqLA49GIkcn-k_B3w"

# Create Gemini client
client = genai.Client(api_key=API_KEY)

# Create chat
chat = client.chats.create(
    model="gemini-2.5-flash",
    config=types.GenerateContentConfig(
        system_instruction=(
            "You are a helpful and friendly personal chatbot. "
            "Answer the user clearly and simply."
        )
    )
)

print("🤖 Gemini Chatbot")
print("Type 'exit' to stop.\n")

while True:

    message = input("You: ").strip()

    if message.lower() == "exit":
        print("Bot: Goodbye! 👋")
        break

    if not message:
        continue

    try:

        # Send message to Gemini
        response = chat.send_message(message)

        # Print response
        print("Bot:", response.text)
        print()

    except Exception as e:

        print("❌ Error:", e)
        print()
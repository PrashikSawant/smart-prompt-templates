from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ask_ai(system_prompt, user_input):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ]
    )
    return response.choices[0].message.content

# ── 5 TEMPLATES ───────────────────────────────────────────────────────────────

TEMPLATES = {
    "1": {
        "name": "📝 Summarizer",
        "system": "You are an expert summarizer. Summarize the given text in 3-5 clear bullet points. Be concise and capture only the most important ideas.",
        "prompt": "Enter the text you want to summarize: "
    },
    "2": {
        "name": "❓ Q&A",
        "system": "You are a knowledgeable assistant. Answer the user's question clearly, accurately and in simple language. If you don't know something, say so honestly.",
        "prompt": "Enter your question: "
    },
    "3": {
        "name": "🔍 Explainer",
        "system": "You are a teacher who explains complex topics in the simplest way possible. Use analogies, examples, and simple language. Explain as if talking to a 15 year old.",
        "prompt": "Enter the topic or concept you want explained: "
    },
    "4": {
        "name": "🌍 Translator",
        "system": "You are a professional translator. First ask the user which language they want to translate to. Then translate the given text accurately while preserving the original meaning and tone.",
        "prompt": "Enter the text and target language (e.g. 'Hello world - translate to Hindi'): "
    },
    "5": {
        "name": "✍️ Critic",
        "system": "You are a constructive writing critic. Review the given text and provide: 1) What works well, 2) What can be improved, 3) Specific suggestions to make it better. Be honest but encouraging.",
        "prompt": "Enter the text you want reviewed: "
    }
}

# ── MAIN LOOP ─────────────────────────────────────────────────────────────────

def main():
    print("\n" + "="*50)
    print("   🤖 Smart Prompt Templates Assistant")
    print("="*50)

    while True:
        print("\nChoose a template:")
        for key, template in TEMPLATES.items():
            print(f"  {key}. {template['name']}")
        print("  6. Exit")

        choice = input("\nEnter your choice (1-6): ").strip()

        if choice == "6":
            print("\nGoodbye! 👋")
            break

        if choice not in TEMPLATES:
            print("Invalid choice. Please enter a number between 1 and 6.")
            continue

        template = TEMPLATES[choice]
        print(f"\n── {template['name']} ──")

        user_input = input(template['prompt']).strip()

        if user_input == "":
            print("No input provided. Please try again.")
            continue

        print("\n⏳ Thinking...\n")
        result = ask_ai(template['system'], user_input)

        print("── AI Response ──")
        print(result)
        print("\n" + "-"*50)

        another = input("\nUse another template? (yes/no): ").strip().lower()
        if another != "yes":
            print("\nGoodbye! 👋")
            break

if __name__ == "__main__":
    main()
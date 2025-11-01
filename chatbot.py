import random

knowledge_base = {
    # --- GREETINGS ---
    "greetings": {
        "patterns": ["hi", "hello", "hey", "good morning", "good evening", "what's up", "yo"],
        "responses": [
            "Hello!  How can I assist you today?",
            "Hey there! What brings you here today?",
            "Hi! Hope you're having a great day ",
            "Good to see you! How can I help?"
        ]
    },

    # --- GOODBYES ---
    "goodbye": {
        "patterns": ["bye", "goodbye", "see you", "take care", "later"],
        "responses": [
            "Goodbye! ",
            "See you later!",
            "Take care and have a great day!",
            "Bye! Keep learning and smiling "
        ]
    },

    # --- THANK YOU ---
    "thanks": {
        "patterns": ["thanks", "thank you", "thx", "appreciate it", "thanks a lot"],
        "responses": [
            "You're welcome! ",
            "Glad I could help!",
            "No problem at all!",
            "Always happy to help! "
        ]
    },

    # --- ABOUT BOT ---
    "about_bot": {
        "patterns": ["who are you", "what can you do", "what is your name", "introduce yourself", "tell me about you"],
        "responses": [
            "I am an AI chatbot created to assist with questions, learning, and fun!",
            "I am your personal AI assistant — I can answer questions, explain topics, or just chat with you.",
            "I am a smart chatbot built using Python and AI logic! "
        ]
    },

    # --- AI BASICS ---
    "ai_basics": {
        "patterns": ["what is ai", "define artificial intelligence", "explain ai", "meaning of ai"],
        "responses": [
            "Artificial Intelligence (AI) is the simulation of human intelligence by machines.",
            "AI enables computers to perform tasks like reasoning, learning, and problem solving.",
            "AI is what allows systems like me to understand and respond intelligently! "
        ]
    },

    # --- MACHINE LEARNING ---
    "machine_learning": {
        "patterns": ["what is machine learning", "define ml", "explain ml", "how ml works"],
        "responses": [
            "Machine Learning (ML) is a part of AI that allows systems to learn from data without explicit programming.",
            "ML algorithms analyze patterns in data and improve their performance over time.",
            "In simple words, ML teaches computers to learn from experience like humans!"
        ]
    },

    # --- DEEP LEARNING ---
    "deep_learning": {
        "patterns": ["what is deep learning", "explain deep learning", "what are neural networks"],
        "responses": [
            "Deep Learning is a subset of ML using neural networks with many layers to analyze complex patterns.",
            "It powers technologies like image recognition, speech processing, and self-driving cars ",
            "Deep Learning mimics how the human brain processes information."
        ]
    },

    # --- NLP ---
    "nlp": {
        "patterns": ["what is nlp", "define natural language processing", "how nlp works"],
        "responses": [
            "Natural Language Processing (NLP) helps computers understand and generate human language.",
            "NLP is how I can read your messages and respond meaningfully!",
            "NLP combines linguistics and machine learning to make sense of human language."
        ]
    },

    # --- DATASETS ---
    "datasets": {
        "patterns": ["what is dataset", "example of dataset", "types of dataset"],
        "responses": [
            "A dataset is a collection of data used to train or test AI models.",
            "Datasets can contain images, text, audio, or any type of information used for learning.",
            "Examples include MNIST (handwritten digits) and ImageNet (object images)."
        ]
    },

    # --- AI APPLICATIONS ---
    "applications": {
        "patterns": ["applications of ai", "uses of ai", "where is ai used", "ai in daily life"],
        "responses": [
            "AI is used in healthcare , finance , education , robotics , and self-driving cars .",
            "You use AI daily — voice assistants, chatbots, recommendation systems, and spam filters are examples.",
            "AI helps automate complex tasks and improve decision-making everywhere."
        ]
    },

    # --- MOTIVATION ---
    "motivation": {
        "patterns": ["i am sad", "i am tired", "i feel low", "not motivated", "i am stressed"],
        "responses": [
            "Take a deep breath  — you’re doing better than you think.",
            "Every step forward, no matter how small, is progress ",
            "Don’t give up! The best view comes after the hardest climb ",
            "You’re capable of amazing things — keep going "
        ]
    },

    # --- JOKES ---
    "jokes": {
        "patterns": ["tell me a joke", "make me laugh", "funny joke", "say something funny"],
        "responses": [
            "Why did the AI go to school? Because it wanted to improve its neural net! ",
            "I told my computer a joke... but it didn’t get it — no sense of humor in binary! ",
            "Why did the developer go broke? Because he used up all his cache! "
        ]
    },

    # --- STUDY HELP ---
    "study_help": {
        "patterns": ["how to study", "tips for studying", "how to focus", "how to prepare for exam"],
        "responses": [
            "Break your study into short sessions with small breaks — it boosts focus ",
            "Make notes in your own words — that helps memory! ",
            "Practice questions daily and explain topics out loud to yourself — it works wonders "
        ]
    },

    # --- LIFE ADVICE ---
    "life_advice": {
        "patterns": ["life advice", "how to be happy", "how to handle stress", "i feel lost"],
        "responses": [
            "Happiness starts with gratitude — count small wins each day ",
            "Don’t be too hard on yourself; progress is never linear ",
            "Talk to someone you trust — sharing helps lighten the load "
        ]
    },

    # --- PYTHON HELP ---
    "python_help": {
        "patterns": ["what is python", "how to learn python", "python basics"],
        "responses": [
            "Python is a popular programming language known for simplicity and versatility ",
            "Start learning Python with basics like loops, lists, and functions.",
            "You can use Python for AI, data science, web apps, and more!"
        ]
    },

    # --- TECH INFO ---
    "tech_news": {
        "patterns": ["latest in ai", "latest technology", "trending tech", "ai updates"],
        "responses": [
            "AI is rapidly growing — new models and automation tools appear every week!",
            "Generative AI is trending — from chatbots to creative art and code generation.",
            "Tech is evolving fast — quantum computing, robotics, and AI ethics are hot topics."
        ]
    },

    # --- DEFAULT ---
    "default": {
        "patterns": [],
        "responses": [
            "Hmm, I’m not sure about that , but I can learn!",
            "Can you rephrase that?",
            "That’s interesting! Tell me more.",
            "I’ll remember that for later "
        ]
    }
}

def get_response(user_input):
    user_input = user_input.lower()

    for intent, data in knowledge_base.items():
        for pattern in data["patterns"]:
            if pattern in user_input:
                return random.choice(data["responses"])

    return random.choice(knowledge_base["default"]["responses"])


print(" Chatbot is ready! (type 'exit' to stop)")

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Bot: Goodbye! ")
        break

    response = get_response(user_input)
    print("Bot:", response)


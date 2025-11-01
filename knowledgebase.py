knowledge_base = {
    "greetings": {
        "patterns": ["hi", "hello", "hey", "good morning", "good evening", "what's up"],
        "responses": ["Hello!  How can I help you today?",
                      "Hey there! What can I do for you?",
                      "Hi! How’s it going?"]
    },

    "goodbye": {
        "patterns": ["bye", "goodbye", "see you", "take care"],
        "responses": ["Goodbye! ", "See you soon!", "Take care!"]
    },

    "thanks": {
        "patterns": ["thanks", "thank you", "thx", "appreciate it"],
        "responses": ["You're welcome!", "Happy to help!", "No problem! "]
    },

    "about_bot": {
        "patterns": ["who are you", "what can you do", "what is your name", "introduce yourself"],
        "responses": ["I am an AI chatbot built to help you with information and tasks.",
                      "I am your virtual assistant — I can answer questions, explain topics, and more!"]
    },

    "ai_basics": {
        "patterns": ["what is ai", "define artificial intelligence", "explain ai"],
        "responses": ["Artificial Intelligence (AI) is the simulation of human intelligence in machines that can think, learn, and make decisions."]
    },

    "machine_learning": {
        "patterns": ["what is machine learning", "explain ml", "ml basics"],
        "responses": ["Machine Learning is a subset of AI that enables computers to learn from data and improve automatically without being explicitly programmed."]
    },

    "deep_learning": {
        "patterns": ["what is deep learning", "explain neural networks"],
        "responses": ["Deep Learning is a part of Machine Learning that uses neural networks with many layers to analyze complex patterns in data."]
    },

    "nlp": {
        "patterns": ["what is nlp", "explain natural language processing"],
        "responses": ["Natural Language Processing (NLP) is a branch of AI that helps machines understand and process human language."]
    },

    "datasets": {
        "patterns": ["what is a dataset", "example of dataset", "what data is used in ai"],
        "responses": ["A dataset is a collection of data used to train or test AI models. Examples include images, text, audio, or sensor data."]
    },

    "applications": {
        "patterns": ["applications of ai", "uses of ai", "where is ai used"],
        "responses": ["AI is used in healthcare, finance, education, self-driving cars, recommendation systems, and many other areas."]
    },

    "motivational": {
        "patterns": ["i am tired", "i feel low", "i am not motivated", "i am sad"],
        "responses": ["Don’t give up!  Every small step counts.",
                      "You’re doing great — progress takes time. ",
                      "Remember why you started! Keep going! "]
    },

    "fun": {
        "patterns": ["tell me a joke", "make me laugh", "joke"],
        "responses": ["Why did the computer go to therapy? Because it had a hard drive! ",
                      "What do you call an AI that tells jokes? Pun-ctuator! "]
    },

    "default": {
        "patterns": [],
        "responses": ["I'm not sure"]
    }
}
print(knowledge_base)
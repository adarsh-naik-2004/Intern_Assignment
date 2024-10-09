import nltk
from nltk.chat.util import Chat, reflections

# Expanded patterns and responses with guideline
approved_questions = [
    r"What is Castle Swimmer about?",
    r"Who are the main characters?",
    r"What happens in Chapter 83?",
    r"What is the Mini-God’s role?",
    r"What are the themes in Chapter 85?",
    r"What new goal does Siren have in Chapter 86?",
    r"What occurs in Chapter 87?",
    r"Who is Queen Nee?",
    r"What significant events happen in Chapter 89?",
    r"Could you summarize Siren's journey?",
    r"What is the significance of Kappa's dream?",
    r"How does Siren plan to break the curse?",
    r"What role does Prophecy play in the story?",
    r"How does Siren's past influence his actions?",
    r"What challenges does Kappa face?",
    r"How does mythology influence the chapters?",
    r"Quit"
]

pairs = [
    [pattern, [response]] for pattern, response in zip(approved_questions, [
        "Castle Swimmer is a fantasy webtoon about Siren, a beacon destined by prophecy to save his race, and his journey to break curses.",
        "The main characters include Siren, Kappa, Queen Nee, Krilli, and the mysterious mini-gods.",
        "Chapter 83 reveals Siren's curse and his determination to change his fate by living beyond the prophecy's confines.",
        "Chapter 84 explores the mini-god's involvement in sustaining Siren's curse, and provides a warning against trusting divine prophecies.",
        "Chapter 85 focuses on apology and introspection, with Siren confronting memories of his mother and past life.",
        "In Chapter 86, Siren resolves to find a demi-god to break the curse and shares profound reflections with his companions.",
        "Chapter 87 introduces Kappa's internal conflict with new prophecy dreams and a quest for understanding his destiny.",
        "Queen Nee, appearing in Chapter 88, is a regal figure connected to Kappa's past, involved in his ongoing adventures.",
        "Chapter 89 involves Kappa volunteering to help fulfill a prophecy, yet he remains a special guest, underscoring tension and uncertainty.",
        "Siren's journey is about resisting destiny and seeking freedom through defiance of a fatalistic prophecy.",
        "Kappa's dream in Chapter 87 highlights the recurring theme of prophecy and the continuous pull of fate in his life.",
        "Siren intends to seek a demi-god who can help him break the curse, reflecting his ongoing struggle for liberation.",
        "Prophecy is a central theme, often guiding and complicating the characters' actions and decisions throughout the story.",
        "Siren's past deeply impacts his current quest, burdening him with memories but also motivating him to break free from imposed fates.",
        "Kappa faces internal and external challenges shaped by prophecy, friends, and his quest for understanding.",
        "Mythology, through mini-gods and prophecies, enriches the narrative, providing mystical elements that shape the characters' journeys.",
        "Thank you for chatting!"
    ])
]

# Add a default response for unapproved questions
pairs.append([
    r".*",
    ["Sorry, please ask relevant questions to this article."]
])

# Build and run the chatbot
chatbot = Chat(pairs, reflections)
chatbot.converse()

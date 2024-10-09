import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Dataset with webtoon descriptions and their corresponding categories
data = {
    'description': [
        "Shim Su-ae is a martyr for romance. Despite all the clear signs that her boyfriend is cheating on her, she still acts like nothing has happened. But a mysterious jelly-pop flip phone turns her dumb fate around. After all, that thing is a bloody sentient love guru! But will the phone’s love advice be enough to knock some sense into our dull female lead?",
        "Hana Han desires nothing but a normal life. Too bad her stupid ancestor had to mess with a mountain god. Her entire bloodline suffers from a curse that turns them into dogs when they kiss someone. To break the curse, they must kiss the same person again. So what's the twist? Hana accidentally kissed her handsome co-teacher, who's downright terrified of dogs.",
        "Dani is a simple girl who loves reading web novels. But one fateful day, she suddenly transmigrates into her favorite novel—no, not as the protagonist, but as the best friend of the female MC. Trapped inside a romance tale, she sets out to avoid ruining the plotline. Too bad the other characters have no such plans. Thus begins her eerie journey between the borders of fiction and reality.",

        "Ijin Yu had a dark childhood. His parents died in a plane crash, leaving him in a foreign land where child mercenaries were normal. Trapped in a war zone, he had to kill and fight to survive. Ten years later, he reunites with his kin through a kind man's help. But can a man baptized by fire and blood live a normal life? Or will his past haunt him?",
        "Jaha Lee desires to reach the zenith of martial arts. Call it stupid, but to achieve his lofty dream, he steals a treasure from the notorious Demon Cult. Unfortunately, the cult doesn't take such madness kindly and releases a kill order against him. To escape, he jumps off a cliff, only to wake up in the past—back when he was just an insignificant innkeeper. Still, his return to the past matters little. His dream is the same—to become the greatest martial artist in Murim—and he won't stop until he achieves it.",
        "Bullies have taken over the lives of Eunjang High's students. Worse, your life becomes miserable once they put a target on your back. But everything changes when the mysterious transferee Gray joins the school. Gray turns out to be the bane of all bullies. Although he has a weak stature, he makes the school's toughest bullies fall onto their knees—bruised and bloodied.",

        "When he transmigrated into Lyod Frontera, civil engineering student Suho Kim knew his life was bound to become one of labor and toil—a wretched fate. So he’s hell-bent on changing his bad ending. To escape his fate, he mixes his engineering skills with magic to achieve the life that he wants. From sewage systems to condo units, he’ll construct anything to save himself from death.",
        "Jiwoo is a cat-loving, compassionate young man. Nobody knows that he possesses superhuman abilities beyond comprehension. One fateful day, Jiwoo rescues a wounded, chubby stray cat. However, he soon realizes that he has saved a very strange feline—a talking cat. But that's not all! This fat kitty also turns out to be the most feared superhuman in the world.",
        "Divine War God Dan Woohyun is a name that strikes fear into the hearts of many. His martial path is so inhuman that he leaves trails of blood wherever he treads. He's the chilling embodiment of death itself. However, fate takes an unexpected turn when he finds himself sealed in ice for a thousand long years. Upon his awakening, a small act of kindness from an orphaned girl melts the icy barrier around his heart, revealing a warmth he thought was long lost.",

        "While not strictly a horror series, The Horizon bears enough of a horrific footprint embodying many of the genre's hallmarks, including a sense of dread due to a war-torn landscape fraught with danger. A young boy and girl find each other, attempt to survive this bleak hellscape, and deal with unbearable loss, conveyed in graphic detail to the reader, enthralling them with one of the best first chapters in any manhwa. The Horizon examines topics like death, childhood innocence, and hope, while the environmental storytelling does the heavy lifting in the relative absence of dialogue in a concise, post-apocalyptic masterpiece.",
        "Bastard revolves around Jin Seon and his terrible twisted life. Not only is he bullied at school due to his quiet nature, but he also has to witness and participate in horrifying events at home. As far as most can tell, his father would be considered a successful and charismatic businessman, but all of that is just a facade behind which lies a deviant serial killer, whom Jin has no choice but to secretly help. However, when the next target ends up being his girlfriend, Jin finally has the chance to defy his father. Successfully combining horror with romance elements, Bastard is truly one of the best manhwa titles ever published.",
        "After losing his family in a tragic car accident, Cha Hyun moves into a new apartment by himself. Adjusting to his new environment and life would be difficult enough under normal circumstances, but he soon finds out that his situation is anything but normal. The people around him begin turning into scary monsters intent on exterminating humanity, and he must fight alongside other tenants to learn the truth and survive in a dark and dangerous world. Sweet Home features not only a compelling story but also a brilliant art style with unique character designs that create genuine suspense and fear among readers.",

    ],
    'category': [
        'romance', 'romance', 'romance', 'action',
        'action','action','comedy','comedy','comedy','horror','horror','horror'
    ]
}

# DataFrame
df = pd.DataFrame(data)

# Vectorize the text data
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['description'])
y = df['category']

# Split the dataset into a training set and a test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Training the decision tree model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Predicting the categories
y_pred = model.predict(X_test)

# Calculating the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print(f'Classification Accuracy: {accuracy * 100:.2f}%')

# Function to take input and make predictions
def classify_description(description):
    description_vector = vectorizer.transform([description])
    prediction = model.predict(description_vector)
    return prediction[0]

# Taking exmple input
input_description = "An epic love story in the bustling city with a twist of fate."
predicted_category = classify_description(input_description)
print(f'The predicted category for the input description is: {predicted_category}')

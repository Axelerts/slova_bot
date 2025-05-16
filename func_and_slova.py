import random

# Существительные с родом и одушевлённостью
nouns = [
    {"word": "Краб", "gender": "m", "animate": True},
    {"word": "Лимон", "gender": "m", "animate": False},
    {"word": "Мышка", "gender": "f", "animate": True},
    {"word": "Машина", "gender": "f", "animate": False},
    {"word": "Робот", "gender": "m", "animate": True},
    {"word": "Книга", "gender": "f", "animate": False}
]

# Глаголы в прошедшем времени, с формами по роду
verbs = {
    "позвал": {"m": "позвал", "f": "позвала"},
    "увидел": {"m": "увидел", "f": "увидела"},
    "нашёл": {"m": "нашёл", "f": "нашла"},
    "обнял": {"m": "обнял", "f": "обняла"},
    "встретил": {"m": "встретил", "f": "встретила"},
    "понюхал": {"m": "понюхал", "f": "понюхала"}
}

# Склонение объекта в винительном падеже
def decline_obj(noun):
    word = noun["word"]
    gender = noun["gender"]
    animate = noun["animate"]

    if gender == "m":
        if animate:
            return word.lower() + "а"  # Краб → краба
        else:
            return word.lower()  # Лимон остаётся лимоном
    elif gender == "f":
        if word.endswith("а"):
            return word[:-1] + "у"  # Машина → машину
        elif word.endswith("я"):
            return word[:-1] + "ю"
    return word.lower()

# Генерация предложений
def genereted():
    subject = random.choice(nouns)
    verb_key = random.choice(list(verbs.keys()))
    verb = verbs[verb_key][subject["gender"]]

    obj = random.choice([n for n in nouns if n["word"] != subject["word"]])
    obj_word = decline_obj(obj)

    return f"{subject['word']} {verb} {obj_word}."


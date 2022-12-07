def translate(sentence: str):
    lst = sentence.split()
    print(lst)
    words = {'esta': 'is', 'la': 'the', 'en': 'in', 'gato': 'cat', 'casa': 'house', 'el': 'the'}
    translate_gen = (words[word] for word in lst)
    final = []
    for w in translate_gen:
        final.append(w)
    return " ".join(final)

print(translate("el gato esta en la casa"))
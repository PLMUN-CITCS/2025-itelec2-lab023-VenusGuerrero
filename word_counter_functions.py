def get_sentence_input():
    sentence = (input("Enter a sentence: "))
    return sentence

def count_words(sentence):
    words = sentence.split()
    return len(words)

sentence_final = get_sentence_input()
word_count = count_words(sentence_final)
print(f"The sentence has {word_count} words.")

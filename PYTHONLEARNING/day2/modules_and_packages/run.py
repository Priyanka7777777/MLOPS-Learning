from text_analyzer import TextAnalyzer, clean_text, remove_punctuation

text = "Hello, world! Hello Python. This is a test. Hello!!!"

print("Original text:", text)
print("Without punctuation:", remove_punctuation(text))
print("Cleaned text:", clean_text(text))

analyzer = TextAnalyzer(text)

print("\nWord count:", analyzer.word_count())
print("Character count:", analyzer.char_count())
print("Top 3 words:", analyzer.top_n_words(3))


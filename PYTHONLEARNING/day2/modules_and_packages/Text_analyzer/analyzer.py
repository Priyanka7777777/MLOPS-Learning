from .utils import clean_text

class TextAnalyzer:

    def __init__(self, text):
        self.original_text = text
        self.cleaned_text = clean_text(text)
        self.words = self.cleaned_text.split()

    def word_count(self):
        """Return number of words."""
        return len(self.words)

    def char_count(self):
        """Return number of characters (no spaces)."""
        return len(self.cleaned_text.replace(" ", ""))

    def top_n_words(self, n):
        """Return top n most frequent words."""
        freq = {}
        for w in self.words:
            freq[w] = freq.get(w, 0) + 1

        sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        return sorted_words[:n]

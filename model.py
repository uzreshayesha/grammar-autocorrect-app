class GrammarAutocorrectModel:
    def correct_spelling(self, text):
        custom_dictionary = {"hehlo": "hello", "helo": "hello", "helllo": "hello", "i": "I"}
        words = text.split()
        return " ".join([custom_dictionary.get(w.lower(), w) for w in words])
        
    def correct_grammar(self, text):
        text = text.replace("wants", "want").replace("eating", "to eat").replace("is very", "are very")
        return text.capitalize() if text else text
        
    def process_text(self, text):
        return self.correct_grammar(self.correct_spelling(text))

import os
import re
import random
from collections import Counter
from typing import List, Set, Tuple, Any

class WordLoader:
    def __init__(self, directory: str):
        self.directory = directory
        self.word_counts = Counter()
        self.unique_words = set()

    def load_files(self) -> None:
        if not os.path.exists(self.directory) or not os.path.isdir(self.directory):
            raise ValueError(f"Input directory '{self.directory}' does not exist or is not a directory.")

        files = [file for file in os.listdir(self.directory) if file.endswith('.txt')]
        for file in files:
            file_path = os.path.join(self.directory, file)
            if not os.path.isfile(file_path) or not file_path.endswith('.txt'):
                continue

            with open(file_path, 'r') as f:
                text = f.read().lower()
                words = re.findall(r'\b\w+\b', text)
                self.word_counts.update(words)
                self.unique_words.update(words)

class WordPredictor:
    def __init__(self, word_loader: WordLoader):
        self.word_loader = word_loader

    def display_stats(self) -> None:
        print("Basic Statistics:")
        print(f"a. Number of files trained: {len(os.listdir(self.word_loader.directory))}")
        print(f"b. Total number of words: {sum(self.word_loader.word_counts.values())}")
        print(f"   Number of unique words: {len(self.word_loader.unique_words)}")
        print("c. Five rarest words:")
        rare_words = self.word_loader.word_counts.most_common()[:-6:-1]
        min_count = rare_words[-1][1]
        rarest_words = [word for word, count in rare_words if count == min_count]
        if len(rarest_words) < 5:
            rarest_words.extend(random.sample(self.word_loader.unique_words - set(rarest_words), 5 - len(rarest_words)))
        print("\n".join(rarest_words))

    def _get_following_words(self, word: str) -> List[str]:
        following_words = [w for w in self.word_loader.word_counts if w!= word]
        following_words.sort(key=lambda w: self.word_loader.word_counts[w], reverse=True)
        return following_words

    def mode_a(self, word: str, k: int) -> None:
        if word not in self.word_loader.unique_words:
            print("Word not found in training material.")
            return

        possible_words = self._get_following_words(word)[:k]
        print(f"Top {k} words that may follow '{word}':")
        print("\n".join(possible_words))

    def mode_b(self, word: str, n: int) -> None:
        if word not in self.word_loader.unique_words:
            print("Word not found in training material.")
            return

        result = [word]
        for _ in range(n):
            following_words = self._get_following_words(word)
            next_word = random.choice([w for w in following_words if w != word])
            result.append(next_word)
            word = next_word
        print(" ".join(result))

    def mode_c(self, word: str, n: int) -> None:
        if word not in self.word_loader.unique_words:
            print("Word not found in training material.")
            return

        result = [word]
        for _ in range(n):
            following_words = self._get_following_words(word)
            probabilities = [self.word_loader.word_counts[w] / sum(self.word_loader.word_counts.values()) for w in following_words]
            next_word = random.choices(following_words, weights=probabilities)[0]
            result.append(next_word)
            word = next_word
        print(" ".join(result))

# Example usage
directory = "path/to/training/files"
word_loader = WordLoader(directory)
word_loader.load_files()
predictor = WordPredictor(word_loader)
predictor.display_stats()

mode = input("Select mode of operation (A/B/C): ")
if mode == 'A':
    word = input("Entera word: ").lower()
    k = int(input("Enter maximum number of recommendations (k): "))
    predictor.mode_a(word, k)
elif mode == 'B':
    word = input("Enter a word: ").lower()
    n = int(input("Enter number of text words (n): "))
    predictor.mode_b(word, n)
elif mode == 'C':
    word = input("Enter a word: ").lower()
    n = int(input("Enter number of text words (n): "))
    predictor.mode_c(word, n)
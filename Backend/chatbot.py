import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from knowledge_base  import load_knowledge_base
from utils import preprocess_text

class Chatbot:
    def __init__(self, knowledge_base_path: str):
        """
        Initialise the chatbot:
        - Load the knowledge base 
        - Preprocess all questions
        - Build TF-IDF matrix for  similarity search
        """

        self.knowledge_base = load_knowledge_base(knowledge_base_path)
        # separate questions and answers 
        self.questions = [item["questions"] for item in self.knowledge_base]
        self.answers =  [item["answer"] for item in self.knowledge_base]

        # Preprocess questions
        self.processed_questions = [preprocess_text(q) for q in self.questions]

        # Build TF_IDF vectorizer
        self.vectorizer = TfidfVectorizer()
        self.question_vectors = self.vectorizer.fit_transform(self.processed_questions)

        def get_response(self, user_input: str) -> str:
            """
            Process user input, compare it with knowledge base
            and returns the most relevant answer.
            """
            processed_input = preprocess_text(user_input)
            input_vector = self.vectorizer.transform([preprocessed_input])

            # Compute similarity
            if best_score < 0.2:
                return "Hmmn, I would have to contact NASA for that 😂"
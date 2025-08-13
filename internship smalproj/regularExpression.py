# question_classifier.py
import re

def classify_question(question: str) -> str:
   
    # Math detection
    if re.search(r'\d+[\+\-\*/]\d+', question):
        return "math"

    # Opinion detection keywords
    opinion_keywords = ["think", "feel", "opinion", "believe", "prefer", "like", "dislike"]
    if any(word in question.lower() for word in opinion_keywords):
        return "opinion"

   
    return "factual"





if __name__ == "__main__":
    user_q = input("Ask me something: ")
    print(classify_question(user_q))

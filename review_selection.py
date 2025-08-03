import json
import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')

positive_keywords = {'good', 'great', 'excellent', 'amazing', 'awesome', 'fantastic', 'love', 'wonderful', 'best'}

def is_good_review(tokens):
    tokens_lower = [t.lower() for t in tokens]
    return any(word in tokens_lower for word in positive_keywords)

with open('tokenized_reviews.json', 'r', encoding='utf-8') as fin:
    for line in fin:
        review = json.loads(line)
        tokens = review.get('tokens', [])
        if is_good_review(tokens):
            review_id = review.get('review_id')
            business_id = review.get('business_id')
            logging.info(f'review_id: {review_id}, business_id: {business_id}, tokens: {tokens}')
            logging.basicConfig(level=logging.INFO, format='%(message)s', filename='selected_reviews.log', filemode='w')
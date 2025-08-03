import json
import nltk

# Download NLTK tokenizer if not already present
nltk.download('punkt')
nltk.download('punkt_tab')

def get_all_reviews(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        # Adjust the key below to match your JSON structure
        reviews = []
        if isinstance(data, dict) and 'reviews' in data:
            reviews = data['review_count']
        elif isinstance(data, list):
            for item in data:
                if 'review_count' in item:
                    if item['review_count'] > 5:
                        reviews.append(item['attributes'])
        # Tokenize each review (optional)
        #tokenized_reviews = [nltk.word_tokenize(review) for review in reviews]
        #return reviews, tokenized_reviews
        return reviews

if __name__ == "__main__":
    # reviews, tokenized_reviews = get_all_reviews('fb.json')
    reviews = get_all_reviews('fb.json')
    for review in reviews:
        print(review)
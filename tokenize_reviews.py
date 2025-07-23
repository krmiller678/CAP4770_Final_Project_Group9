import json
import nltk

nltk.download('punkt')

input_file = 'filtered_reviews.json'
output_file = 'tokenized_reviews.json'

with open(input_file, 'r', encoding='utf-8') as fin, open(output_file, 'w', encoding='utf-8') as fout:
    for line in fin:
        review = json.loads(line)
        review_id = review.get('review_id')
        business_id = review.get('business_id')
        text = review.get('text', '')
        tokens = nltk.word_tokenize(text)
        out_obj = {
            'review_id': review_id,
            'business_id': business_id,
            'tokens': tokens
        }
        fout.write(json.dumps(out_obj) + '\n')
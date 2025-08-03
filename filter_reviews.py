# Code Snippet 2 - Filtering the Reviews
import json

target_city = "Santa Barbara"
target_state = "CA"
business_ids = set()
filtered_businesses = []

filtered_reviews = []

with open('fb.json', 'r', encoding='utf-8') as f:
    business_data = json.load(f)
    business_ids = set()
    if isinstance(business_data, list):
        for item in business_data:
            if 'business_id' in item:
                business_ids.add(item['business_id'])
    elif isinstance(business_data, dict) and 'business_id' in business_data:
        business_ids.add(business_data['business_id'])


with open('yelp_academic_dataset_review.json', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        data = json.loads(line)
        if data['business_id'] in business_ids:
            filtered_reviews.append(data)

with open('filtered_reviews.json', 'w', encoding='utf-8') as f:
    for r in filtered_reviews:
        f.write(json.dumps(r) + '\n')
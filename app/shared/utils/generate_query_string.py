import random, string

def generate_url_string_with_query_string(utm_campaign_prefix):
    random_chars = ''.join(random.choices(string.ascii_uppercase + string.digits, k=3))
    return utm_campaign_prefix + random_chars
import re

# Defining Regular expression (NB we used the re module first to fetch raw API data)
restaurant_pattern = r'([^-]+) - ([^,]+)'
ingredient_pattern = r'([^,]+)'
rgb_color_pattern = r'rgb\((\d+), (\d+), (\d+)\)'
social_media_pattern = r'@(\w+)'
product_code_pattern = r'([A-Z]+[0-9]+)'
news_headline_pattern = r'([^:]+): ([^:]+)'
event_datetime_pattern = r'(\w+ \d{2}, \d{4} - \d{2}:\d{2} [APap][Mm])'
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

# Instructing API to respond to the data
api_response = """
Restaurant1 - Italian, Restaurant2 - Mexican, Restaurant3 - Japanese
Ingredients: ingredient1, ingredient2, ingredient3
Background color: rgb(255, 255, 255)
Check out our profile: @the invincible 
Product code: ABC123
News: Headline1: Subheader1, Headline2: Subheader2
Event: Oct 10, 2023 - 02:30 PM
Contact us at: k.thuch@alustudent.com
"""


# Extract the Restaurant Data
restaurants = re.findall(restaurant_pattern, api_response)
ingredients = re.findall(ingredient_pattern, api_response)
rgb_colors = re.findall(rgb_color_pattern, api_response)
social_usernames = re.findall(social_media_pattern, api_response)
product_codes = re.findall(product_code_pattern, api_response)
news_headlines = re.findall(news_headline_pattern, api_response)
event_datetime = re.findall(event_datetime_pattern, api_response)
email_addresses = re.findall(email_pattern, api_response)

# Print Extracted Data
print("Restaurants:", restaurants)
print("Ingredients:", ingredients)
print("RGB Colors:", rgb_colors)
print("Social Media Usernames:", social_usernames)
print("Product Codes:", product_codes)
print("News Headlines:", news_headlines)
print("Event Date and Time:", event_datetime)
print("Email Addresses:", email_addresses)

#collaboration is awesome

# Done by Group1

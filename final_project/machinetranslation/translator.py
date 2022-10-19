import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

# Translation instance

translation = language_translator.translate(
    # Input text
    text='Hello, how are you today?',
    model_id='en-es').get_result()
# Return only translation text
d = translation['translations']
# Get translation's dict object
t = d[0]
# Get list object
result = t['translation']
print(result)

# Function translate English text to French
def english_to_french(englishText):
    # Prevent input is null
    while True:
        if englishText != '':
            french_text = language_translator.translate(
                text=englishText,
                model_id='en-fr').get_result()
            d = french_text['translations']
            t = d[0]
            result = t['translation']
            # Since the translation is still a list object, we need to convert it to string so API can read it
            return str(result)
        else:
            break
            

def french_to_english(frenchText):
    while True:
        if frenchText != '':
            english_text = language_translator.translate(
                text=frenchText,
                model_id='fr-en').get_result()
            d = english_text['translations']
            t = d[0]
            result = t['translation']
            return str(result)
        else:
            break    
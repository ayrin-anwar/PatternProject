from googletrans import Translator

import requests
import json


# translator = Translator()
# value = translator.translate("Where are you going?")
# print(value.src)
# print(value.dest)
# print(value.text)


def trans_papa(parsed_text, detected_language, translate_language):
    # List of language code available to translate the text data
    language_dict = {'Tamil': 'ta', 'Hindi': 'hi', 'English': 'en', 'Bangla': 'bn'}
    # Condition when both 'translate_language' and 'detected_language' are available
    if (translate_language in language_dict.keys()) and (detected_language in language_dict.keys()):
        translate_language_code = language_dict[translate_language]
        detected_language_code = language_dict[detected_language]

    # condition when our function can't dect the 'detected_language'
    elif (detected_language == "Can't detect the language") and (translate_language in language_dict.keys()):
        translate_language_code = language_dict[translate_language]
        detected_language_code = "en"
    else:
        # Default languages
        detected_language_code = "en"
        translate_language_code = "bn"
    # api_key = "https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20191228T162619Z.ae9fac5e3ce7b128.b8cc7b5dc723af948a8aabe275072026880e09eb"
    # url = api_key+"&text="+parsed_text+"&lang="+detected_language_code+"-"+translate_language_code+"&[format=plain]"
    # API call through python

    # response = requests.get(url)

    # print(parsed_text,"sadhfahsdfkhaskdhfasdfkahsdf")
    trans = Translator()
    # value = translator.translate("Where are you going?", dest="bn")
    try:
        response = trans.translate(parsed_text, src=detected_language_code, dest=translate_language_code)
    except AttributeError:
        response = trans.translate(parsed_text, src=detected_language_code, dest=translate_language_code)
    except AttributeError:
        response = trans.translate(parsed_text, src=detected_language_code, dest=translate_language_code)
    except AttributeError:
        response = trans.translate(parsed_text, src=detected_language_code, dest=translate_language_code)
    except AttributeError:
        response = trans.translate(parsed_text, src=detected_language_code, dest=translate_language_code)
    except AttributeError:
        response = trans.translate(parsed_text, src=detected_language_code, dest=translate_language_code)
    except AttributeError:
        response = trans.translate(parsed_text, src=detected_language_code, dest=translate_language_code)
    except AttributeError:
        response = trans.translate(parsed_text, src=detected_language_code, dest=translate_language_code)
    except AttributeError:
        response = trans.translate(parsed_text, src=detected_language_code, dest=translate_language_code)
    except AttributeError:
        response = trans.translate(parsed_text, src=detected_language_code, dest=translate_language_code)
    except AttributeError:
        response = trans.translate(parsed_text, src=detected_language_code, dest=translate_language_code)
    except AttributeError:
        response = trans.translate(parsed_text, src=detected_language_code, dest=translate_language_code)
    except AttributeError:
        response = trans.translate(parsed_text, src=detected_language_code, dest=translate_language_code)
    except AttributeError:
        response = trans.translate(parsed_text, src=detected_language_code, dest=translate_language_code)
    except AttributeError:
        response = trans.translate(parsed_text, src=detected_language_code, dest=translate_language_code)
    except:
        response = trans.translate(parsed_text, src=detected_language_code, dest=translate_language_code)

        # response = trans.translate(parsed_text,src="en",dest=translate_language_code)

    print(response)
    # Converting to JSON format
    # result = json.loads(response.text)
    # print(result,"tttttttttttttttttttttttttttttt")
    # Condition to check the translated text

    # if 'text' in result.keys():
    #     return result['text'][0]
    if response.text:
        return response.text
    else:
        # When function fails to execute
        return "Can't translate"


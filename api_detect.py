from googletrans import Translator
import requests
import json


# Text received from Flask Interface
def language_detector(text_data):
    # api_key = "https://translate.yandex.net/api/v1.5/tr.json/detect?key=trnsl.1.1.20191228T162619Z.ae9fac5e3ce7b128.b8cc7b5dc723af948a8aabe275072026880e09eb"
    # url = api_key + "&text=" +  text_data

    detect = Translator()
    # Python API call to Flask

    # response = requests.get(url)
    # response = detect.translate("How are you ?")

    try:
        response =detect.translate(text_data)
    except AttributeError:
        response = detect.translate(text_data)
    except AttributeError:
        response = detect.translate(text_data)
    except AttributeError:
        response = detect.translate(text_data)
    except AttributeError:
        response = detect.translate(text_data)
    except AttributeError:
        response = detect.translate(text_data)
    except AttributeError:
        response = detect.translate(text_data)
    except AttributeError:
        response = detect.translate(text_data)
    except AttributeError:
        response = detect.translate(text_data)
    except AttributeError:
        response = detect.translate(text_data)
    except AttributeError:
        response = detect.translate(text_data)
    except AttributeError:
        response = detect.translate(text_data)
    except AttributeError:
        response = detect.translate(text_data)
    except:
        response = detect.translate(text_data)
        # Converting data to JSON format

    result = (response.src)

    # MAtching language code with the user's language  input
    # language_dict = {'ta': 'Tamil', 'hi': 'Hindi','en': 'English','bn':'Bangla'}
    # language_dict = {'en': 'English','bn':'Bangla'}
    language_dict = {'ar': 'arabic', 'hy': 'armenian',
                     'az': 'azerbaijani', 'eu': 'basque', 'be': 'belarusian', 'bn': 'bengali', 'bs': 'bosnian',
                     'bg': 'bulgarian', 'ca': 'catalan', 'ceb': 'cebuano', 'ny': 'chichewa',
                     'zh-cn': 'chinese (simplified)', 'zh-tw': 'chinese (traditional)', 'co': 'corsican',
                     'hr': 'croatian', 'cs': 'czech', 'da': 'danish', 'nl': 'dutch', 'en': 'english', 'eo': 'esperanto',
                     'et': 'estonian', 'tl': 'filipino', 'fi': 'finnish', 'fr': 'french', 'fy': 'frisian',
                     'gl': 'galician',  'el': 'greek', 'gu': 'gujarati',
                     'ht': 'haitian creole', 'hi': 'hindi',
                     'it': 'italian', 'ja': 'japanese', 'jw': 'javanese', 'kn': 'kannada',
                     'kk': 'kazakh',  'ko': 'korean', 'ku': 'kurdish (kurmanji)', 'ky': 'kyrgyz',
                     'lo': 'lao', 'la': 'latin', 'lv': 'latvian', 'lt': 'lithuanian', 'lb': 'luxembourgish',

                     'ml': 'malayalam', 'mt': 'maltese',
                     'mi': 'maori', 'mr': 'marathi',  'ne': 'nepali',
                      'pl': 'polish', 'pt': 'portuguese',
                     'pa': 'punjabi', 'ro': 'romanian', 'ru': 'russian',
                    'sd': 'sindhi',
                    'es': 'spanish', 'su': 'sundanese', 'sw': 'swahili',
                     'sv': 'swedish',  'ta': 'tamil', 'te': 'telugu',  'cy': 'welsh', 'xh': 'xhosa',
                    }

    # Checking whether  language is available
    # if ('lang' in result.keys()) and  (result['lang'] != ""):
    #     lang =  result['lang']
    #     return  language_dict[lang]
    if result:
        return language_dict[result]
    else:
        return "Can't detect the language"


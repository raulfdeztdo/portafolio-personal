from portafolio_personal.i18n import messages_es, messages_en

def get_translation(key, lang):
    if lang == 'es':
        return messages_es.MESSAGES.get(key, key)
    elif lang == 'en':
        return messages_en.MESSAGES.get(key, key)
    else:
        return key  # Devuelve la clave si no se encuentra una traducción
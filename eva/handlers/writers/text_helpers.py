class TextHandler(object):
    @classmethod
    def concatenate_information_to_text(cls, base_text, information_data):
        text_to_concatenate = ", ".join(information_data)
        return base_text.format(text_to_concatenate)

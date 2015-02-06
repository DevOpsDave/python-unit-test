import json
import re

class ChatParser(object):

    def parse_string(self, input_string):
        output = self.__process_string__(input_string)
        return output


    def __process_string__(self, input_string):
        # initial data
        return_data = {}


        # Used for stripping out symbols
        translate_table = str.maketrans('','','@()')


        # Find mentions.
        mentions = re.findall("@\w+",input_string)
        if mentions:
            return_data['mentions'] = [ mention.translate(translate_table) for mention in mentions ]

        # Find emoticons.
        emoticons = re.findall("\(\s*\w+\s*\)",input_string)
        if emoticons:
            return_data['emoticons'] = emoticons

        return json.dumps(return_data)







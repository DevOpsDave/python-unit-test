#!/usr/bin/env python -W ignore::DeprecationWarning
# Script parses a string for symbols and outputs a json string that breaks out the mentions, links, emoticons.
# Usage example:
# chat_parser_obj = ChatParser()
# json_string_output = chat_parser_obj.parse_string('@bob @john (success) such a cool feature')

import json
import re
from urllib import request
from bs4 import BeautifulSoup

from IPython import embed

class ChatParser(object):

    # Main method to use.
    def parse_string(self, input_string):
        output = self.__process_string__(input_string)
        return output

    def __process_string__(self, input_string):
        # initial data
        return_data = {}

        # Used for stripping out symbols
        translate_table = str.maketrans('','','@()')

        # Find mentions.
        mentions = re.findall(r"@\w+",input_string)
        if mentions:
            return_data['mentions'] = [ mention.translate(translate_table) for mention in mentions ]

        # Find emoticons.
        emoticons = re.findall(r"\(\s*\w+\s*\)",input_string)
        if emoticons:
            return_data['emoticons'] = [ emoticon.translate(translate_table) for emoticon in emoticons ]

        # Find links.
        links = re.findall(r"(https{0,1}://[^ ]+)", input_string)
        if links:
            return_data["links"] = list()
            for link in links:
                page_data = request.urlopen(link).read()
                title = BeautifulSoup(page_data).title.string
                return_data["links"].append({"url": link, "title": str(title)})

        return json.dumps(return_data)



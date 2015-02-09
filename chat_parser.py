#!/usr/bin/env python -W ignore::DeprecationWarning

import json
import re
from urllib import request
from bs4 import BeautifulSoup

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
            return_data['emoticons'] = [ emoticon.translate(translate_table) for emoticon in emoticons ]

        # Find links.
        links = re.findall(r"(http://[^ ]+)", input_string)
        if links:
            for link in links:
                page_data = request.urlopen(link).read()
                title = BeautifulSoup(page_data).title
                return_data["links"] = list()
                return_data["links"].append({ "url": link, "title": str(title.string) })

        return json.dumps(return_data)








#!/usr/bin/env python -W ignore::DeprecationWarning

from chat_parser import ChatParser
import json
import unittest

from IPython import embed

class TestChatParser(unittest.TestCase):

    def setUp(self):
        self.cpobj = ChatParser()

    def helper(self, test_name, input_string, should_data, silent=True):
        output_string = self.cpobj.parse_string(input_string)
        if not silent:
            print("Running: ", str(test_name))
            print("Input: ", input_string)
            print("Output: ", output_string)
        self.assertEqual(output_string, json.dumps(should_data))

    # A string with no symbols should simply output an empty json string.
    def test_no_symbols(self):
        input_string = 'hipchat is cool'
        should_data = {}
        self.helper('Test no symbols', input_string, should_data)

    def test_mentions(self):
        input_string = 'Hey @bob, hipchat is cool'
        should_data = { "mentions": ["bob"] }
        self.helper('Test mentions', input_string, should_data)

    def test_multi_mentions(self):
        input_string = 'Hey @bob, hipchat is cool. @Ted should know too.'
        should_data = { "mentions": [ "bob", "Ted" ] }
        self.helper('Test multiple mentions', input_string, should_data)

    def test_emoticons(self):
        input_string = 'Yo, good job! (success)'
        should_data = { "emoticons": [ "success" ] }
        self.helper('Test emoticons', input_string, should_data)

    def test_multi_emoticons(self):
        input_string = 'Yo, good job! (success) (awesome)'
        should_data = { "emoticons": [ "success", "awesome" ] }
        self.helper('Test multi emoticons', input_string, should_data)

    def test_links(self):
        input_string = 'Olympics are starting soon; http://www.nbcolympics.com'
        should_data = { "links": [ {"url": "http://www.nbcolympics.com", "title": "NBC Olympics | Home of the 2016 Olympic Games in Rio"  } ] }
        self.helper('Test links', input_string, should_data)

    def test_multi_links(self):
        input_string = 'First go here: http://www.google.com and then go here: http://www.nbcolympics.com'
        should_data = { "links": [ { "url": "http://www.google.com", "title": "Google" } ] }
        should_data["links"].append({ "url": "http://www.nbcolympics.com", "title": "NBC Olympics | Home of the 2016 Olympic Games in Rio" })
        self.helper('Test multi links', input_string, should_data)

    def test_all_of_them(self):
        input_string = "@bob @john (success) such a cool feature; https://twitter.com/jdorfman/status/430511497475670016"
        url = 'https://twitter.com/jdorfman/status/430511497475670016'
        title = 'Justin Dorfman on Twitter: "nice @littlebigdetail from @HipChat (shows hex colors when pasted in chat). http://t.co/7cI6Gjy5pq"'
        should_data = { "mentions": ["bob","john"], "emoticons": ["success"], "links": [ { "url": url, "title": title } ] }
        self.helper('Test all', input_string, should_data)

if __name__ == '__main__':
    unittest.main()





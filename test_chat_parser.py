#!/usr/bin/env python

from chat_parser import ChatParser
import json
import unittest

class TestChatParser(unittest.TestCase):

    def setUp(self):
        self.cpobj = ChatParser()

    # A string with no symbols should simply output an empty json string.
    def test_no_symbols(self):
        output = self.cpobj.parse_string('my test string with no symobols')
        self.assertEqual(output, '{}', 'A string with no symbols should return {}')

    def test_mentions(self):
        output = self.cpobj.parse_string('Hey @bob, hipchat is cool')
        should_return = json.dumps({ "mentions": ["bob"] })
        self.assertEqual(output, should_return)



if __name__ == '__main__':
    unittest.main()





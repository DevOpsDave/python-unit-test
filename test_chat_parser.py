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
        input_string = 'Hey @bob, hipchat is cool'
        output = self.cpobj.parse_string(input_string)
        should_return = json.dumps({ "mentions": ["bob"] })
        print("Input_string is: ", input_string)
        print("Output is: ", output)
        self.assertEqual(output, should_return)

    def test_emoticons(self):
        input_string = 'Yo, good job! (success)'
        output = self.cpobj.parse_string(input_string)
        should_return = json.dumps({ "emoticons": ["success"] })
        print("Input_string is: ", input_string)
        print("Output is: ", output)
        self.assertEqual(output, should_return)




if __name__ == '__main__':
    unittest.main()





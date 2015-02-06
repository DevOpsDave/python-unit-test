#!/usr/bin/env python

from chat_parser import ChatParser
import unittest

class TestChatParser(unittest.TestCase):

    def setUp(self):
        self.cpobj = ChatParser()

    # A string with no symbols should simply output an empty json string.
    def test_no_symbols(self):
        output = self.cpobj.parse_string('my test string with no symobols')
        assertEqual(output, '{}', 'A string with no symbols should return {}')



if __name__ == '__main__':
    unittest.main()





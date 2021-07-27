import unittest


class UnicodeTests(unittest.TestCase):

    def test_howToGetFunctionName(self):
        def functionName():
            pass

        self.assertEqual(unicode(functionName.__name__), u"functionName")
        pass

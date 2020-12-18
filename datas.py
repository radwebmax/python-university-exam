import datetime
import unittest

a = datetime.date(2020, 12, 23).strftime("%U")
print(a)

class MyTest(unittest.TestCase):

    # testing queue for empty
    def test_weeks(self):
        self.assertNotEqual(a, 51)

def sort_test_suite():
    suite = unittest.TestSuite()
    suite.addTest(MyTest('test_weeks'))
    return suite


if __name__ == '__main__':
    import xmlrunner
    runner = xmlrunner.XMLTestRunner(output='test-reports')
    unittest.main(testRunner=runner)


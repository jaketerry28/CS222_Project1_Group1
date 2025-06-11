import unittest
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from wiki.Search import Search

#test class for the Search file in the Wiki folder

class TestSearch(unittest.TestCase):

    #test if the search params are intitialized correctly
    def testSearchLimit(self):

        s = Search()
        excepcted_keys = ["action", "list", "srsearch", "format"]
        self.assertEqual(list(s.params.keys()), excepcted_keys)

    #test if the search params are initialized correctly
    def testSetSearchTerm(self):
        s = Search()
        s.params["srsearch"] = "Python"
        self.assertEqual(s.params["srsearch"], "Python")


    # test if the default search term is empty
    def testDefaultSearchTermEmpty(self):
        s = Search()
        self.assertEqual(s.params["srsearch"], "")

if __name__ == "__main__":
    unittest.main()
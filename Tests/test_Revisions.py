import unittest
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from wiki.Revisions import Revisions

#test class for the Revisions file in wiki folder

class TestRevisions(unittest.TestCase):

    def test_rvlimit (self):

        r = Revisions()
        self.assertEqual(r.params["rvlimit"], "30")

        #this function tests includes the 30 revisions limit in the params dict
    
    
    #checks if initial title is empty in the params dict
    def testInitialTitleIsEmpty(self):

        r = Revisions()
        self.assertEqual(r.params["titles"], "")


    #tests if if a title is correctly in the params dict
    def testTitle(self):

        r = Revisions()
        r.params["titles"] = "new title"
        self.assertEqual(r.params["titles"], "new title")

if __name__ == "__main__":
    unittest.main()
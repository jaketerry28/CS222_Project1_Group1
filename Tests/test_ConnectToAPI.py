import unittest
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from wiki.ConnectToAPI import ConnectToAPI

#test class for the ConnectToAPI file in the wiki folder

class TestConnectToAPI(unittest.TestCase):
    
    def testUrlProperty(self):
        
        #test if the url property returns the wiki api endpoint
        api = ConnectToAPI("Test")
        self.assertEqual(api.URL, "https://en.wikipedia.org/w/api.php") #wiki api endpoint


if __name__ == "__main__":
        unittest.main()

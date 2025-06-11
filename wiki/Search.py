from .ConnectToAPI import ConnectToAPI
from .Revisions import Revisions

class Search(ConnectToAPI):
    
    # parameters for conducting a search with wiki api
    # note srsearch is intentionally left as a blank string
    def __init__(self):
        super().__init__("Search")
        self.params = {
          "action": "query",
          "list": "search",
          "srsearch": "",
          "format": "json"
        }
    
    def searchWiki(self, search_page):
        # input from main becomes srseach parameter
        self.params["srsearch"] = search_page

        # use ConnectToApi inheritence to perform get request
        DATA = super().connect(self.params, self.name)

        search_info = DATA["query"]["searchinfo"]
        search_results = DATA["query"]["search"]

        if search_info["totalhits"] == 0 or not search_results:
            raise ValueError("Error: No Wikipedia page found for given name.")
        
        first_title = search_results[0]["title"]
        # if first title matches search term
        if first_title.lower() == search_page.lower():
            title_to_use = first_title
        else:
            print(f"Redirected to {first_title}")
            title_to_use = first_title

        revisions = Revisions()
        revisions.getRevisions(title_to_use)

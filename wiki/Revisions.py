from .ConnectToAPI import ConnectToAPI

class Revisions(ConnectToAPI):
 
    # parameters for getting revision information
    # titles is intentionally left blank
    # rvlimit limits to 30 max revisions
    def __init__(self):
        super().__init__("Revisions")
        self.params = {
        "action": "query",
        "format": "json",
        "prop": "revisions",
        "titles": "",
        "formatversion": "2",
        "rvprop": "user|timestamp",
        "rvlimit": "30"
    }   


    def getRevisions(self, search_page):
        # assign titles parameter
        self.params["titles"] = search_page

        # perform get request with updated parameters
        DATA = super().connect(self.params, self.name)

        # initialize a counter and print out revisions (max 30)
        count = 0
        print("\nHere are the most recent changes to this wikipedia page: ")
        print("============================================================")
        for element in DATA["query"]["pages"][0]["revisions"]:
            count +=1
            print(f"{count}) User: {element['user']} || Date: {element['timestamp']}")
    

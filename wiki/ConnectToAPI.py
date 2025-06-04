import requests

class ConnectToAPI:
    # base Wiki API URL
    _URL = "https://en.wikipedia.org/w/api.php"

    # set as a property to not accidentally change URL
    @property
    def URL(self):
        return self._URL
    
    def __init__(self, name):
        self.name = name

    # takes parameters dictated by Search or Revisions classes
    def connect(self, params, name):
        try:
            session = requests.Session()
            response = session.get(url=self.URL, params=params)
            data = response.json()

            print(f"\n{name} URL: {response.url}\n")
            return data
        except requests.exceptions.RequestException as e:
            print("Request failed:", e)

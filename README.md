# CS222 Project1 Group 1
**Collaborators**: Denait Mehari and Jake Terry

## Milestones
- [x] User input is read correctly.
- [x] JSON response is fetched from Wikipedia
- [x] JSON response is parsed correctly to get time and username
- [x] 30 or less changes (based on JSON that is returned) are displayed
- [x] Show if user has been redirected
- [ ] Error code 1
- [ ] Error code 2
- [ ] Error code 3
- [ ] README

* ConnectToApi is a class that will handle the initial connection to the wiki api.
* Search and Revisions inherit form ConnectToApi in order to perform two separate api requests.
* Search will use the search specific parameters and check:
  * if there are no search results return a message saying so
  * if a match is found, get the pages revisions by creating an instance of Revisions()
  * if a similar match is found, a message calling the redirection, then get the page revisions by creating a Revisions().
* Revisions will return at most 30 recent edits, along with the username if not private and the dates of the revision.
* Main will handle the user input for searching and creating an instance of Search() and importing from the packages.
* Packaged all the classes under the wiki directory.

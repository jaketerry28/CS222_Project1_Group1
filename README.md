# CS222 Project1 Group 1
**Collaborators**: Denait Mehari and Jake Terry

## Overview

The purpose of this project is to pull the 30 most recent revisions for any particular wikipedia article. The user enters the name of an article and the program returns a max of 30 revisions, including date/time and username of the revisioner, in reverse-chronological order. If no search is found, the user is redirected, or if there is a connection error, then the program will print the appropiate message.   

Important links:  
[Wiki API Documentation](https://www.mediawiki.org/wiki/API:Main_page)  
[API Parameter Constructor](https://en.wikipedia.org/wiki/Special:ApiSandbox)  




### Tests
* Each class in the wiki folder has its own tests inside the tests folder (test_ConnectToAPI, test_Revisions, & test_Search).
* Implemented Test-Driven Development (TDD) by writing tests that reflect the expected behavior of each class.
* Each test file has focused test cases. For example for the test_ConnectToAPI there is a test that tests if the if the url property returns the wiki api endpoint.

### Classes 
Packaged all the classes under the wiki directory.  
  
**ConnectToApi**
* ConnectToApi is a class that will handle the initial connection to the wiki api.
* Search and Revisions inherit form ConnectToApi in order to perform two separate api requests.

**Search**
* Search will use the search specific parameters and check:
  * if there are no search results return a message saying so
  * if a match is found, get the pages revisions by creating an instance of Revisions()
  * if a similar match is found, a message calling the redirection, then get the page revisions by creating a Revisions().

**Revisions**  
* Revisions will return at most 30 recent edits, along with the username if not private and the dates of the revision.
* Main will handle the user input for searching and creating an instance of Search() and importing from the packages.


## Milestones
- [x] User input is read correctly.
- [x] JSON response is fetched from Wikipedia
- [x] JSON response is parsed correctly to get time and username
- [x] 30 or less changes (based on JSON that is returned) are displayed
- [x] Show if user has been redirected
- [x] Error code 1
- [x] Error code 2
- [x] Error code 3
- [x] README

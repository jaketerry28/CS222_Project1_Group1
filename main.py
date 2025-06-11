from wiki import Search

#main function, runs the program

def main():
    
    try:
        query = input("Search for Article: ").strip()
        if not query:
            print("error: no article name given")
            exit(1)
            #error code 1

        search = Search()
        search.searchWiki(query)

        #error code 0
        exit(0)
    except ValueError as value_error:
        print(str(value_error))
        exit(2)
        # error code 2
    except ConnectionError as connection_error:
        print(str(connection_error))
        exit(3)
        # error code 3

main()
from neo4j_conn import get_neo4j_driver

def fetch_some_data(driver):
    # Get the names of people born in a specific year (e.g. 1964)
    records, summary, keys = driver.execute_query("MATCH (p:Person {birthYear: $birthYear}) RETURN " \
    "p.name AS name", birthYear=1964, database_="movies",) 
    # Loop through results and do something with them 
    for person in records:  
        print(person) 
    # Summary information 
    print("The query '{query}' returned {records_count} records in {time} ms." 
          .format(query=summary.query, records_count=len(records), time=summary.result_available_after, 
        ))

if __name__ == "__main__":
    # 1. get the connection
    my_driver = get_neo4j_driver()
    print("Connected Successfully to Local Server")
    
    try:
        # 2. Here we will perform our queries
        print("--------------------------------------------------")
        fetch_some_data(my_driver)
        print("--------------------------------------------------")
    finally:
        # 3. Closing connection
        my_driver.close()
        print("Connection closed successfully!")
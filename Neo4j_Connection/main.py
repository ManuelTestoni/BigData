from neo4j_conn import get_neo4j_driver

def fetch_some_data(driver):
    with driver.session() as session:
        result = session.run("MATCH (n) RETURN n LIMIT 5")
        for record in result:
            print(record)

if __name__ == "__main__":
    # 1. get the connection
    my_driver = get_neo4j_driver()
    
    try:
        # 2. Here we will perform our queries
        fetch_some_data(my_driver)
    finally:
        # 3. Closing connection
        my_driver.close()
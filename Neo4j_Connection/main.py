from neo4j_conn import get_neo4j_driver

# Esempio di una funzione che fa la query passando il driver connesso
def fetch_some_data(driver):
    with driver.session() as session:
        result = session.run("MATCH (n) RETURN n LIMIT 5")
        for record in result:
            print(record)

if __name__ == "__main__":
    # 1. Recupera la connessione al database
    my_driver = get_neo4j_driver()
    
    try:
        # 2. Fai le tue query
        fetch_some_data(my_driver)
    finally:
        # 3. Assicurati di chiudere il driver alla fine di tutto!
        my_driver.close()
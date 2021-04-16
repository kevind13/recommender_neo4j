from py2neo import Graph

url = 'bolt://localhost:7687'
user = "neo4j"  # Default by neo4j
password = '1234'


def connectToNeo4j(user, password):
    '''
    Establishes a connection with neo4j.
    Default neo4j username is 'neo4j'
    '''
    try:
        connection = Graph(url, user=user, password=password)
    except:
        connection = Graph(url, user=user, password=password)
    return connection


def removeExistingData(connection):
    '''
    Neo4j does not replace a dataset when additional data is added, that is
    why we need to remove all existing data before loading the dataset again
    '''
    connection.run("MATCH (n) DETACH DELETE n")
    for constraint in connection.run("CALL db.constraints"):
        connection.run("DROP CONSTRAINT " + constraint[0])


# Establish a connection with neo4j and load the dataset
connection = connectToNeo4j(user, password)
removeExistingData(connection)

queries = [
    """CREATE CONSTRAINT ON (user:User) ASSERT user.userID IS UNIQUE;""",
    """USING PERIODIC COMMIT LOAD CSV WITH HEADERS
        FROM 'https://git.io/JOmL7'
        AS line
        WITH toInteger(line.CustomerID) AS userID, line WHERE NOT line.CustomerID IS null
        MERGE(user:User {userID: userID})
        ON CREATE SET user.country = line.Country;""",
    """CREATE CONSTRAINT ON (product:Product) ASSERT product.stockCode IS UNIQUE;""",
    """USING PERIODIC COMMIT
        LOAD CSV WITH HEADERS
        FROM 'https://git.io/JOmL7'
        AS line
        MERGE(product:Product {productID: line.StockCode})
        ON CREATE SET product.description = line.Description;""",
    """CREATE CONSTRAINT ON (order:Order) ASSERT order.orderID IS UNIQUE;""",
    """USING PERIODIC COMMIT
        LOAD CSV WITH HEADERS
        FROM 'https://git.io/JOmL7'
        AS line
        MERGE(order:Order {orderID: line.InvoiceNo})
        ON CREATE SET order.orderDate = line.InvoiceDate;""",
    """USING PERIODIC COMMIT
        LOAD CSV WITH HEADERS
        FROM 'https://git.io/JOmL7'
        AS line
        WITH toInteger(line.CustomerID) AS UserID, line.InvoiceNo AS OrderID
        MATCH (user:User {userID: UserID})
        MATCH (order:Order {orderID: OrderID})
        MERGE (user)-[:MADE]->(order);""",
    """USING PERIODIC COMMIT
        LOAD CSV WITH HEADERS
        FROM 'https://git.io/JOmL7'
        AS line
        WITH toInteger(line.Quantity) AS Quantity, toFloat(line.UnitPrice) AS UnitPrice, line.InvoiceNo AS OrderID, line.StockCode AS ProductID
        MATCH (order:Order {orderID: OrderID})
        MATCH (product:Product {productID: ProductID})
        MERGE (order)-[r:CONTAINS]->(product)
            ON CREATE SET r.quantity = Quantity, r.price = UnitPrice * Quantity
            ON MATCH SET r.quantity = r.quantity + Quantity, r.price = r.price + UnitPrice * Quantity;"""
]


for q in queries:
    connection.run(q)

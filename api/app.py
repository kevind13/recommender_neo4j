from flask import Flask
from flask_cors import CORS
from neomodel import config
from neomodel import (config, StructuredNode, StringProperty, IntegerProperty,
                      UniqueIdProperty, RelationshipTo)

config.DATABASE_URL = 'bolt://neo4j:1234@localhost:7687'  # default


class Product(StructuredNode):
    description = StringProperty()
    stockCode = StringProperty(unique_index=True)


class Transaction(StructuredNode):
    transactionDate = StringProperty()
    transactionID = StringProperty(unique_index=True)

    product = RelationshipTo(Product, 'CONTAINS')


class Customer(StructuredNode):
    uid = UniqueIdProperty()
    customerID = IntegerProperty(unique_index=True)
    country = StringProperty()

    # traverse outgoing IS_FROM relations, inflate to Country objects
    transaction = RelationshipTo(Transaction, 'MADE')


# Iterable
for c in Customer.nodes.has(transaction=True):
    print(c.customerID)


app = Flask(__name__)

if __name__ == '__main__':
    # app.run(debug=True)
    pass

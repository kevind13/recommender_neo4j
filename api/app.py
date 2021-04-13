from flask import Flask, request, jsonify
from flask_cors import CORS
from neomodel import config
from neomodel import (config, StructuredNode, StringProperty, IntegerProperty,
                      UniqueIdProperty, RelationshipTo, db)
config.DATABASE_URL = 'bolt://neo4j:1234@localhost:7687'  # default

app = Flask(__name__)


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


@app.route('/users', methods=['GET'])
def get_users():
    users = [{'id': user.customerID, 'country': user.country}
             for user in Customer.nodes]
    return jsonify(users)


@app.route('/user/<id>', methods=['GET'])
def get_user_products(id):
    products = []
    for tran in Customer.nodes.get(customerID=id).transaction:
        for prod in tran.product:
            if {'description': prod.description} not in products:
                products.append({'description': prod.description})
    return jsonify(products)


'''
- First, get all products that Costumer has ordered
- Next, find all customers that has at least one food contained in customer1's products
- List out customer2 and collect all products for this customer2
- Create a list of recommended products based on those found in customer1 products list BUT NOT found in customer2 produc list
- Return recommended products but ensure that there is at least one product in Customer1 list that is not found in customer2 list (product2)
'''

"""
@app.route('/recomendation/<id>', methods=['GET'])
def get_user_recomendation(id):
    
    return jsonify()

query = "MATCH (c1:Customer {customerID: 17850})-[:MADE]-(:Transaction)-[:CONTAINS]->(p:Product) return c1"
results, meta = db.cypher_query(query)
print(len(results))
"""

if __name__ == '__main__':
    # app.run(debug=True)
    pass

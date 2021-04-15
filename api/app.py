from flask import Flask, request, jsonify
from flask_cors import CORS
from neomodel import config
from neomodel import (config, StructuredNode, StringProperty, IntegerProperty,
                      UniqueIdProperty, RelationshipTo, db)
config.DATABASE_URL = 'bolt://neo4j:1234@localhost:7687'  # default

app = Flask(__name__)

CORS(app)


class Product(StructuredNode):
    description = StringProperty()
    productID = StringProperty(unique_index=True)


class Order(StructuredNode):
    orderDate = StringProperty()
    orderID = StringProperty(unique_index=True)

    product = RelationshipTo(Product, 'CONTAINS')


class User(StructuredNode):
    uid = UniqueIdProperty()
    userID = IntegerProperty(unique_index=True)
    country = StringProperty()

    # traverse outgoing IS_FROM relations, inflate to Country objects
    order = RelationshipTo(Order, 'MADE')


@app.route('/users', methods=['GET'])
def get_users():
    users = [{'id': user.userID, 'country': user.country}
             for user in User.nodes]

    return jsonify(users)


@app.route('/user/<id>', methods=['GET'])
def get_user_products(id):
    products = []
    for tran in User.nodes.get(userID=id).order:
        for prod in tran.product:
            if {'product': prod.description} not in products:
                products.append({'product': prod.description})
    return jsonify(products)


'''
- First, get all products that Costumer has ordered
- Next, find all customers that has at least one food contained in customer1's products
- List out customer2 and collect all products for this customer2
- Create a list of recommended products based on those found in customer1 products list BUT NOT found in customer2 produc list
- Return recommended products but ensure that there is at least one product in Customer1 list that is not found in customer2 list (product2)
'''


@app.route('/recomendation/<id>', methods=['GET'])
def get_user_recomendation(id):
    query = '''MATCH (c1:User {userID: $_id})-[:MADE]->(:Order)-[:CONTAINS]->(p1:Product)<-[:CONTAINS]-(:Order)-[:MADE]-(c2:User)
            WHERE c1<>c2
            MATCH (c2)-[:MADE]->(:Order)-[:CONTAINS]->(p2:Product)
            where p2<>p1
            return p2.description, count(p2) as frequency
            ORDER BY frequency DESC
            LIMIT 5'''

    results, meta = db.cypher_query(query, params={'_id': int(id)})
    recomendations = [{'product': product[0]} for product in results]

    # It may happen that no one has bought your product, so in that case I take the most purchased products.
    if len(recomendations) == 0:
        query = '''MATCH (c1:User {userID: $_id})-[:MADE]->(:Order)-[:CONTAINS]->(p1:Product)
                MATCH (c2:User)-[:MADE]->(:Order)-[:CONTAINS]->(p2:Product)
                where p2<>p1
                return p2.description, count(p2) as frequency
                ORDER BY frequency DESC
                LIMIT 5'''

        results, meta = db.cypher_query(query, params={'_id': int(id)})
        recomendations = [{'product': product[0]} for product in results]

    return jsonify(recomendations)


if __name__ == '__main__':
    app.run(debug=True)

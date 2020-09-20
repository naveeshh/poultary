from flask import request

# from src.models.poultry import Customers
from flask.views import MethodView
from src.handlers.handler_customer import addcustomer


class Customers(MethodView):
    def get(self):
        """
                Create a new user
                ---
                tags:
                  - users
                definitions:
                  - schema:
                      id: Group
                      properties:
                        name:
                         type: string
                         description: the group's name
                parameters:
                  - in: body
                    name: body
                    schema:
                      id: User
                      required:
                        - email
                        - name
                      properties:
                        email:
                          type: string
                          description: email for user
                        name:
                          type: string
                          description: name for user
                        address:
                          description: address for user
                          schema:
                            id: Address
                            properties:
                              street:
                                type: string
                              state:
                                type: string
                              country:
                                type: string
                              postalcode:
                                type: string
                        groups:
                          type: array
                          description: list of groups
                          items:
                            $ref: "#/definitions/Group"
                responses:
                  201:
                    description: User created
                """
        return "rupesh"

    def post (self):
        """
                Create a new user
                ---
                tags:
                  - users
                definitions:
                  - schema:
                      id: Group
                      properties:
                        name:
                         type: string
                         description: the group's name
                parameters:
                  - in: body
                    name: body
                    schema:
                      id: User
                      required:
                        - email
                        - name
                      properties:
                        email:
                          type: string
                          description: email for user
                        name:
                          type: string
                          description: name for user
                        address:
                          description: address for user
                          schema:
                            id: Address
                            properties:
                              street:
                                type: string
                              state:
                                type: string
                              country:
                                type: string
                              postalcode:
                                type: string
                        groups:
                          type: array
                          description: list of groups
                          items:
                            $ref: "#/definitions/Group"
                responses:
                  201:
                    description: User created
                """
        a = request.get_json()
        return addcustomer(a)


cust = Customers.as_view("navesh")





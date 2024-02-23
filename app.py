from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint



SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI (without trailing '/')
API_URL = '/static/swagger.json'  # Our API url (can of course be a local resource)

# Call factory function to create our blueprint
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "E-commerce API"
    },
)



app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Secret key to sign the JWT token
jwt = JWTManager(app)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

from flask import json

@app.route('/static/swagger.json')
def generate_swagger_spec():
    swagger_spec = {
        "swagger": "2.0",
        "info": {
            "title": "E-commerce API",
            "version": "1.0",
            "description": "API for managing products in an e-commerce application"
        },
        "basePath": "/",
        "schemes": [
            "http"
        ],
        "paths": {
            "/login": {
                "post": {
                    "summary": "Authenticate user and get JWT token",
                    "responses": {
                        "200": {
                            "description": "Successful operation"
                        },
                        "401": {
                            "description": "Unauthorized"
                        }
                    }
                }
            },
            "/protected": {
                "get": {
                    "summary": "Protected route that requires authentication",
                    "responses": {
                        "200": {
                            "description": "Successful operation"
                        },
                        "401": {
                            "description": "Unauthorized"
                        }
                    }
                }
            },
            "/products": {
                "get": {
                    "summary": "Get all products",
                    "responses": {
                        "200": {
                            "description": "Successful operation"
                        },
                        "401": {
                            "description": "Unauthorized"
                        }
                    }
                }
            },
            "/products/{product_id}": {
                "get": {
                    "summary": "Get a specific product by ID",
                    "responses": {
                        "200": {
                            "description": "Successful operation"
                        },
                        "401": {
                            "description": "Unauthorized"
                        }
                    }
                }
            }
        }
    }
    return json.dumps(swagger_spec)




# Simulation of a user database
users = {
    'admin': {'password': 'admin', 'role': 'admin'},
    'joaoteste': {'password': 'joaoteste', 'role': 'registered'},
}

# Route for authentication and JWT token issuance
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    if not username or not password:
        return jsonify({"msg": "Usuário ou senha inválidos"}), 401

    user = users.get(username, None)
    if not user or password != user['password']:
        return jsonify({"msg": "Usuário ou senha inválidos"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200

# Protected route that requires authentication
@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

@app.route('/')
def index():
    return "Welcome to the E-commerce server!"

if __name__ == '__main__':
    #app.run(debug=False, host='127.0.0.1', port=8000) 
    app.run(debug=True) 



# curl -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcwODU3NDIyMCwianRpIjoiYTQ2MWYxNTYtMGY5My00NGI1LWE0ODYtZjkzOWExMjNhYWE1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImFkbWluIiwibmJmIjoxNzA4NTc0MjIwLCJjc3JmIjoiM2IwZTEyYjMtM2NmMy00OWNiLTljNWQtNjFmZGZmNWQ2ZDJkIiwiZXhwIjoxNzA4NTc1MTIwfQ.OgPYBY3UqiPmGYvEbCSG-I28xQwiFSPREODiCTZco3E" http://localhost:5000/protected
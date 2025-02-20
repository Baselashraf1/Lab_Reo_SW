from flask import Flask, request, jsonify
from routes.todos import todos_bp # type: ignore

app = Flask(__name__)

app.register_blueprint(todos_bp, url_prefix = "/todos")

#404 handler for unknown routes
@app.errorhandler(404) 
def not_found(e): 
    return jsonify({"error": "Resource not found"}), 404

if __name__ == "__main__":
    app.run(port=3000)
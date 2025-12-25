from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# ---------------- DATABASE CONNECTION ----------------
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="login"
)

cursor = db.cursor(dictionary=True)

# ---------------- REGISTER API ----------------
@app.route("/register", methods=["POST"])
def register():
    data = request.json

    firstname = data.get("firstname")
    lastname = data.get("lastname")
    email = data.get("email")
    contact = data.get("contact")
    password = data.get("password")

    # Basic validation
    if not all([firstname, lastname, email, contact, password]):
        return jsonify({"message": "All fields are required"}), 400

    # Check if user already exists
    cursor.execute("SELECT * FROM users WHERE email=%s", (email,))
    user = cursor.fetchone()

    if user:
        return jsonify({"message": "User already exists"}), 409

    # Insert new user
    cursor.execute(
        """
        INSERT INTO users (firstname, lastname, email, contact, password)
        VALUES (%s, %s, %s, %s, %s)
        """,
        (firstname, lastname, email, contact, password)
    )
    db.commit()

    return jsonify({"message": "Registration successful"}), 201


# ---------------- LOGIN API ----------------
@app.route("/login", methods=["POST"])
def login():
    data = request.json

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"message": "Email and password required"}), 400

    cursor.execute(
        "SELECT * FROM users WHERE email=%s AND password=%s",
        (email, password)
    )
    user = cursor.fetchone()

    if user:
        return jsonify({
            "message": "Login successful",
            "user": {
                "id": user["id"],
                "firstname": user["firstname"],
                "lastname": user["lastname"],
                "email": user["email"],
                "contact": user["contact"]
            }
        }), 200
    else:
        return jsonify({"message": "Invalid email or password"}), 401


# ---------------- RUN SERVER ----------------
if __name__ == "__main__":
    app.run(debug=True)

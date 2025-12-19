# !pip install flask-ngrok

from flask import Flask, request, render_template_string
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)

comments = []

html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Simple Blog - Stored XSS Demo</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f2f2f2;
            margin: 0;
            padding: 0;
        }
        .container {
            max-width: 800px;
            margin: 40px auto;
            padding: 20px;
            background: white;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        h1, h2 {
            text-align: center;
        }
        textarea {
            width: 100%;
            padding: 10px;
            border-radius: 5px;
            margin-bottom: 10px;
            border: 1px solid #ccc;
        }
        input[type="submit"] {
            width: 100%;
            padding: 10px;
            background: #007bff;
            color: white;
            border: none;
            border-radius: 5px;
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        li {
            background: #eee;
            padding: 10px;
            margin-top: 5px;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>📝 Leave a Comment</h1>
        <form method="POST">
            <textarea name="comment" rows="4" placeholder="Your comment..."></textarea><br>
            <input type="submit" value="Submit">
        </form>
        <h2>💬 All Comments</h2>
        <ul>
            {% for comment in comments %}
                <li>{{ comment|safe }}</li>
            {% endfor %}
        </ul>
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        comment = request.form.get("comment")
        comments.append(comment)
    return render_template_string(html_template, comments=comments)

app.run()

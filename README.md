Task 3: Templates and Dynamic Content (Flask & Jinja2)
📌 Objective

The objective of this task is to learn how to create dynamic web pages using Flask templates and the Jinja2 templating engine. This task demonstrates how data can be passed from Python to HTML and how reusable layouts improve code organization.

🛠️ Tools & Technologies Used

Python 3

Flask

Jinja2 Templating Engine

HTML5

Visual Studio Code

Web Browser

GitHub

📚 What I Learned

What templates are and why they are used

How Jinja2 works with Flask

Template inheritance (base.html)

Passing dynamic data from Flask to HTML

Using loops and variables inside templates

Creating reusable layout components

📝 Steps Performed
1️⃣ Create Templates Folder

Created a folder named templates/

Stored all HTML files inside this folder as required by Flask

2️⃣ Create a Base Template

Created base.html

Added common elements such as:

Page structure

Navigation bar

Used {% block %} tags for content replacement

3️⃣ Create Child Templates

Created index.html

Extended base.html using {% extends %}

Overrode title and content blocks

4️⃣ Pass Dynamic Data from Flask

Passed variables like:

Username

Current date

List of items

Rendered dynamic content using:

{{ }} for variables

{% for %} loops

💻 Source Code
base.html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}My Website{% endblock %}</title>
</head>
<body>
    <nav>
        <a href="/">Home</a> |
        <a href="/about">About</a>
    </nav>

    {% block content %}{% endblock %}
</body>
</html>

index.html
{% extends "base.html" %}

{% block title %}Home Page{% endblock %}

{% block content %}
<h1>Welcome, {{ username }}!</h1>
<p>Today is {{ date }}</p>

<ul>
    {% for item in items %}
        <li>{{ item }}</li>
    {% endfor %}
</ul>
{% endblock %}

app.py
from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template(
        'index.html',
        username="John",
        date=datetime.now().strftime("%Y-%m-%d"),
        items=['Apple', 'Banana', 'Orange']
    )

if __name__ == '__main__':
    app.run(debug=True)

📁 Project Structure
Task-3/
│
├── app.py
├── templates/
│   ├── base.html
│   └── index.html
└── README.md

✅ Expected Output

A web page with a consistent layout

Dynamic username and date

A list generated from Python data

Clean separation between logic and presentation

🎯 Conclusion

This task demonstrates how Flask + Jinja2 enable dynamic and scalable web applications. Using templates improves code reusability, maintainability, and consistency across multiple pages.

from flask import Flask, request
from caesar import superEncrypt

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            h1 {{
                font-size: 3em;
                text-align: center;
                margin: 20px 0 20px 0;
                color: #d82222;
            }}
            body {{
                background-color: #a9c7e4;
            }}           
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <h1><em>Caesar's Cypher</em></h1>
            <form action="/" method="POST">
                <label for="rot">Rotate by:</label>
                <input type="text" name="rot" id="rot" value="0">
                <textarea name="text" id="text" cols="30" rows="10" placeholder="Enter Text Here">{0}</textarea>
                <button>Submit</button>
            </form>
    </body>
</html>

"""

@app.route("/")
def index():
    form1 = form.format("")
    return form1

@app.route("/", methods=['POST'])
def encrypt():
    rotate_by = int(request.form["rot"])
    text = request.form["text"]
    encrypted_text = superEncrypt(text,rotate_by)
    form1 = form.format(encrypted_text) 
    return form1

app.run()
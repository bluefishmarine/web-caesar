from flask import Flask, request
from caesar import Encryption


app = Flask(__name__)
app.config['DEBUG'] = True
encrypt1 = Encryption()


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
                <label for="key">Key</label>
                <input type="text" name="key" id="key" value="">
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
    rotate = request.form["rot"]
    key = request.form["key"]
    text = request.form["text"]
    encryptR = ""
    encryptK = ""
    encryptB = ""
    if rotate and key:
        rotate = int(rotate)
        encryptR = encrypt1.encrypt(text,rotate)
        encryptK = encrypt1.text_encrypt(text,key)
        encryptB = encrypt1.text_encrypt(encryptR,key)
        results = encryptR + "&#8194" + encryptK + "&#8194" + encryptB  
        form1 = form.format(results)
        return form1
    if rotate:
        rotate = int(rotate)
        encrypted_text = encrypt1.encrypt(text,rotate)
        form1 = form.format(encrypted_text) 
        return form1
    elif key:
        encrypted_text = encrypt1.text_encrypt(text,key)
        form1 = form.format(encrypted_text) 
        return form1


app.run()
from flask import Flask, render_template, request
import random
import string
import os
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def Generate_password(length, characters):
    return ''.join(random.choice(characters) for _ in range(length))

CHARACTER_MAP = {
    "digits" : string.digits,
    "ascii_letters" : string.ascii_letters,
    "punctuation" : string.punctuation
}

char_key = ['digits', 'ascii_letters','punctuation']
char_value = [string.digits, string.ascii_letters, string.punctuation]

@app.route("/health")
def health():
    return {"status": "healthy", "service": "password-generator"}, 200

@app.route("/", methods=["GET", "POST"])
def index():    
    logger.info("Index route accessed")
    try:
        if request.method == "POST":
            logger.info("POST request received")
            length_str = request.form.get("length")
            
            characters = ""

            for i in range(len(char_key)):
                if request.form.get(char_key[i]):
                    characters += char_value[i]
                    
            if not characters:
                # remember to remove whitespaces
                characters = string.printable
                
            # handle if the length exists and is valid
            if length_str:
                try:
                    length = int(length_str)
                    if length < 8:
                        return render_template("index.html", error="Length should be greater than 8")
                    elif length > 50:
                        return render_template("index.html", error="Length should be shorter than 50.")
                    else:
                        password = Generate_password(length, characters)
                        return render_template("index.html", password=password, length=length)
                except ValueError:
                    return render_template("index.html",error="Please enter a number.")
            else:
                # handle if the length doesn't exist
                return render_template("index.html", error="Please enter the length.")
        # return the default website if no length received
        logger.info("Rendering index template")
        return render_template("index.html")
    except Exception as e:
        logger.error(f"Error in index route: {str(e)}")
        return f"Error: {str(e)}", 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
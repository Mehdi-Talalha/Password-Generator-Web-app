from flask import Flask, render_template, request
import random
import string

<<<<<<< HEAD
def Generate_password(length, use_alpha=True, use_digits=True, use_punctuation=True):
    CHARACTERS = ""
    if use_alpha:
        CHARACTERS += string.ascii_letters
    if use_digits:
        CHARACTERS += string.digits
    if use_punctuation:
        CHARACTERS += string.punctuation

    # fallback if nothing is selected
    if not CHARACTERS:
        CHARACTERS = "".join(char for char in string.printable if char not in set(string.whitespace))

    return ''.join(random.choice(CHARACTERS) for _ in range(length))

# to run the server: flask --app app.py run --debug --port 5001
=======
def Generate_password(length):
    # take the charcters form the string module
    CHARACTERS = "".join(char for char in string.printable if char not in set(string.whitespace))
    # return the random password
    return ''.join(random.choice(CHARACTERS) for _ in range(length))

# to run the server: Type this command in the terminal ==> flask --app app.py run --debug --port 5001
>>>>>>> fa2ad8361d90042a51caac0e2bb97de9c8fa785a

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        length = request.form.get("length")
<<<<<<< HEAD
        characters = request.form.getlist("characters")

        use_alpha       = "alpha"       in characters
        use_digits      = "digits"      in characters
        use_punctuation = "punctuation" in characters

        if length:
            try:
                length = int(length)
                if length < 4:
                    return render_template("index.html", error="Length must be at least 4", length=length, characters=characters)
                if length > 128:
                    return render_template("index.html", error="Length must be 128 or less", length=length, characters=characters)
                password = Generate_password(length, use_alpha, use_digits, use_punctuation)
                strength = get_strength(length, use_alpha, use_digits, use_punctuation)
                return render_template("index.html", password=password, length=length, characters=characters, strength=strength)
            except ValueError:
                return render_template("index.html", error="Please enter a valid number", characters=characters)
        else:
            return render_template("index.html", error="Please enter the length of the password", characters=characters)

    return render_template("index.html")

def get_strength(length, alpha, digits, punct):
    score = 0
    if length >= 8:  score += 1
    if length >= 16: score += 1
    if length >= 24: score += 1
    if alpha:  score += 1
    if digits: score += 1
    if punct:  score += 1
    if score <= 2: return "Weak"
    if score <= 4: return "Medium"
    return "Strong"

if __name__ == "__main__":
    app.run(debug=True)
=======
        # handle if the length exist and not agreed
        if length:
            try:
                length = int(length)
                password = Generate_password(length)
                return render_template("index.html", password=password, length=length)
            except ValueError:
                return render_template("index.html",error="Please enter a valid number")
        else:
            # handle if the length doesn't exist
            return render_template("index.html", error="Please enter the length of the number")
    # return the default website of they are no length recived
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
>>>>>>> fa2ad8361d90042a51caac0e2bb97de9c8fa785a

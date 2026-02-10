from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        data = {
            "name": request.form.get("name"),
            "email": request.form.get("email"),
            "age": request.form.get("age"),
            "gender": request.form.get("gender"),
            "skills": request.form.getlist("skills"),
            "course": request.form.get("course"),
            "feedback": request.form.get("feedback"),
            "dob": request.form.get("dob")
        }
        return render_template("success.html", data=data)

    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)

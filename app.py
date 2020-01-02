from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    """Landing page."""
    return render_template('/index.html', title="Logbook")


if __name__ == "__main__":
    app.run(debug=True)

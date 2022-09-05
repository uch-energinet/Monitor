from flask import Flask, render_template
from src.models import Section, Page
from src import dashboard


DEBUG = True
SECTIONS = [
    Section(
        name="dashboards",
        menu_name="Dashboards",
        pages=[
            Page(
                name="all",
                menu_name="All"
            )
        ]
    )
]
CONFIG = {
    "sections": SECTIONS
}


app = Flask(__name__)
app.register_blueprint(dashboard.bp)


@app.route("/")
def index():
    return render_template("index.jinja", **CONFIG)

if __name__ == "__main__":
    app.run(debug=DEBUG)


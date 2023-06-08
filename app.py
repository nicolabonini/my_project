#this is the app.py file that contain the backend logic for my first project

from flask import Flask, render_template
from flask.json import jsonify

app = Flask (__name__)

jobs_list = [
    {
        'id' : 1,
        'title' : 'Data Analyst',
        'location' : 'Milan',
        'salary' : '70.000 €'
    }
]

@app.route ("/")
def render_page ():
    return render_template (
        'home.html',
        jobs = jobs_list,
        company_name = 'unfair_project'
    )

@app.route ("/api/jobs")
def list_jobs ():
    return jsonify (jobs_list)

if __name__ == "__main__":
    app.run (host = '0.0.0.0', debug = True)
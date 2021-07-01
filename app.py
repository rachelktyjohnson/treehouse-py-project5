from flask import (render_template, request, redirect, url_for)
from models import db, Project, app


@app.route('/')
def index():
    return "Home Page"


@app.route('/about')
def about():
    return "About Page"


@app.route('/projects/new')
def project_new():
    return "New Project Page"


@app.route('/projects/<project_id>')
def project_view(project_id):
    return "Specific Project Page"


@app.route('/projects/<project_id>/edit')
def project_edit(project_id):
    return "Edit Specific Project Page"


@app.route("/projects/<project_id>/delete")
def project_delete(project_id):
    return "Delete Specific Project Page"


@app.errorhandler(404)
def not_found():
    return "404 page"


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=8000, host='127.0.0.1')

from flask import (render_template, request, redirect, url_for)
from models import db, Project, app


@app.context_processor
def inject_projects():
    projects = Project.query.all()
    return dict(projects=projects)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/projects/new')
def project_new():
    return render_template('projectform.html')


@app.route('/projects/<project_id>')
def project_view(project_id):
    return render_template('detail.html')


@app.route('/projects/<project_id>/edit')
def project_edit(project_id):
    return render_template('projectform.html')


@app.route("/projects/<project_id>/delete")
def project_delete(project_id):
    return "Delete Specific Project Page"


@app.errorhandler(404)
def not_found(error):
    return "404 page"


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=8000, host='127.0.0.1')

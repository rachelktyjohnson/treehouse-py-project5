from flask import (render_template, request, redirect, url_for)
from models import db, Project, app
import datetime


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


@app.route('/projects/new', methods=['GET', 'POST'])
def project_new():
    if request.form:
        year = request.form['date'][0:4]
        month = request.form['date'][5:7]
        new_project = Project(
            title=request.form['title'],
            date=datetime.datetime.strptime(f'{year}/{month}/01', '%Y/%m/%d'),
            description=request.form['desc'],
            skills=request.form['skills'],
            repo=request.form['github']
        )
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('project_view', project_id=new_project.id))
    return render_template('project_add.html')


@app.route('/projects/<project_id>')
def project_view(project_id):
    project = Project.query.get_or_404(project_id)
    project.skills_list = project.skills.split(',')
    return render_template('detail.html', project=project)


@app.route('/projects/<project_id>/edit', methods=['GET', 'POST'])
def project_edit(project_id):
    project = Project.query.get_or_404(project_id)
    if request.form:
        project.title = request.form['title']
        year = request.form['date'][0:4]
        month = request.form['date'][5:7]
        project.date = datetime.datetime.strptime(f'{year}/{month}/01', '%Y/%m/%d')
        project.description = request.form['desc']
        project.skills = request.form['skills']
        project.repo = request.form['github']
        db.session.commit()
        return redirect(url_for('project_view', project_id=project.id))
    return render_template('project_edit.html', project=project)


@app.route("/projects/<project_id>/delete")
def project_delete(project_id):
    project = Project.query.get_or_404(project_id)
    db.session.delete(project)
    db.session.commit()
    return redirect(url_for('index'))


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html')


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=8000, host='127.0.0.1')

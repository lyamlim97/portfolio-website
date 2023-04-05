from flask import Flask, abort, render_template

app = Flask(__name__)

projects = [
    {
        'name': 'Habit tracking app with Python and MongoDB',
        'thumb': 'img/habit-tracking.png',
        'hero': 'img/habit-tracking-hero.png',
        'categories': ['python', 'mongodb'],
        'slug': 'habit-tracking',
        'prod': 'https://habit-tracker-lyamlim.vercel.app/',
    },
    {
        'name': 'Microblog app with Python and MongoDB',
        'thumb': 'img/personal-finance.png',
        'hero': 'img/personal-finance.png',
        'categories': ['python', 'mongodb', 'writing'],
        'slug': 'microblog',
        'prod': 'https://microblog-lyamlim.vercel.app/',
    },
    {
        'name': 'Dream app with OpenAI DALL-E 2',
        'thumb': 'img/dall-e2.png',
        'hero': 'img/dall-e2.png',
        'categories': ['python', 'DALL-E 2', 'OpenAI'],
        'slug': 'dream',
        'prod': 'https://dream-lyamlim97.vercel.app/',
    }
]

slug_to_project = {project["slug"]: project for project in projects}


@app.route('/')
def home():
    return render_template('home.html', projects=projects)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/project/<string:slug>')
def project(slug):
    if slug not in slug_to_project:
        abort(404)
    return render_template(f'project_{slug}.html', project=slug_to_project[slug])


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

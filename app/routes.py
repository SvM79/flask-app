from flask import Blueprint

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return "Hello, Flask + Render!"
@main.route('/status')
def status():
    return "CI/CD to Render is working!"

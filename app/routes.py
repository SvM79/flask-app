from flask import Blueprint, request

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return "Hello, Flask + Render! :-)"

@main.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        message = request.form.get('message')
        return f"Thanks! You wrote: {message}"
    return '''
        <form method="post">
            <textarea name="message" rows="4" cols="50" placeholder="Write something..."></textarea><br>
            <input type="submit" value="Send">
        </form>
    '''


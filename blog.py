from src import app,db
from src.models import User,Post

@app.shell_context_processor
def make_shell_context():
    return {'app': app, 'db': db,'User':User,'Post':Post}

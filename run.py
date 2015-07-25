from eve import Eve
from flask import render_template

app = Eve(__name__)

@app.route('/')
def index():
    # return app.send_static_file('index.html') -- use this if in static dir
    return render_template('index.html')

if __name__ == '__main__':
    app.run()

from eve import Eve
app = Eve(__name__)

@app.route('/')
def index():
    return app.send_static_file('test.html')

if __name__ == '__main__':
    app.run()

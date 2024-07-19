from flask import Flask
app=Flask(__name__)
@app.route('/')
def hello_World():
    return "<div><h1>hello world</h1></div>";
if __name__=="__main__":
    app.run(debug=True)
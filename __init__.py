
from flask import Flask

app = Flask(__name__)
@app.route('/')
def hello() -> str:
    return "hello world from Flask"

def main():
    app.run()

if __name__ == "__main__":
    main()

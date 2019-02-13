from flask import Flask
from vserch import search4letters


app = Flask(__name__)#create flask instance)
#flask route decolator
@app.route('/')#url  
def hello() -> str:
    return "hello world from Flask"

@app.route('/str_search')#url
def str_serch() -> str:
    return str()



def main():
    app.run()

if __name__ == "__main__":
    main()

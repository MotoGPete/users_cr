from flask import Flask, render_template, request, redirect
# import the class from friend.py
#from friend import Friend
from user import User

app = Flask(__name__)
@app.route("/")
def index():
    # call the get all classmethod to get all friends
    # friends = Friend.get_all()  
    # print(friends)
    return render_template("index.html" ) 

@app.route("/read")
def read():

    users = User.get_all()
    return render_template("read.html", users=users)

@app.route('/form')
def form():
    return render_template("form.html")

@app.route('/create', methods=["POST"])
def create_user():
    #first we make a data dictionary from our request.form coming fro our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"]
    }
    #We pass the data dictionary into the save method from the Friend class
    User.save(data)
    # Don't forget to redirect after saving into the database.
    return redirect('/read')



if __name__ == "__main__":      
    app.run(debug=True)



import os
from flask_pymongo import PyMongo
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)

from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env
    
    
app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_recipes")
def get_recipes():
    recipes = list(mongo.db.recipes.find())
    return render_template("recipes.html", recipes=recipes)


#This is the code for adding a recipe to the database, it will split the ingredients and preparation steps into a list and
#add them to the database. Once the recipe is added it will display a success message and redirect the user to the recipes page.
@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        ingredients = request.form.get("Ingredients").split("\n")
        Preparation_steps = request.form.get("Preparation_steps").split("\n")
        tools = request.form.get("Tools").split("\n")
        recipe = {
            "Name": request.form.get("Name"),
            "Category_name": request.form.get("Category_name"),
            "Description": request.form.get("Description"),
            "Ingredients": ingredients,
            "Preparation_steps": Preparation_steps,
            "Tools": tools,
            "Notes": request.form.get("Notes"),
            "created_by": session["user"]
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Successfully Added")
        return redirect(url_for("get_recipes"))
    categories = mongo.db.categories.find().sort("Category_name", 1)
    return render_template("add_recipe.html", categories=categories)


#This is the code for the edit recipe page, users can edit the recipe and it will update the database.
@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        ingredients = request.form.get("Ingredients").split("\n")
        Preparation_steps = request.form.get("Preparation_steps").split("\n")
        tools = request.form.get("Tools").split("\n")
        submit = {
            "Name": request.form.get("Name"),
            "Category_name": request.form.get("Category_name"),
            "Description": request.form.get("Description"),
            "Ingredients": ingredients,
            "Preparation_steps": Preparation_steps,
            "Tools": tools,
            "Notes": request.form.get("Notes"),
            "created_by": session["user"]
        }
        mongo.db.recipes.update_one({"_id": ObjectId(recipe_id)}, {"$set": submit})
        flash("Recipe Successfully Updated")
        
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    categories = mongo.db.categories.find().sort("Category_name", 1)
    return render_template("edit_recipe.html", recipe=recipe, categories=categories)


#This is the code for the delete recipe ,it will delete the recipe from the database and display a success message.
#then it will redirect the user to the recipes page.
@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.delete_one({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Deleted")
    return redirect(url_for("get_recipes"))


#This is the code for the register page that checks if the username already exists and if it does it will display an error message and
#if it doesn't it will add the username and password to the database and log the user in.
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))
        
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


#This is the login function that checks the username and password against the database and 
#if it matches it will log the user in and if it doesn't it will display an error message.
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        
        if existing_user:
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))
        else:
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))
        
    return render_template("login.html")    


#This is the logout function that will log the user out and display a success message.
@app.route("/logout")
def logout():
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


#This is the user profile page that displays the username of the user that is logged in, 
#if the user is not logged in it will redirect them to the login page. it also displays the recipes that the user has added to the database.
#and allows the user to edit or delete the recipes.
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    if session["user"]:
        recipes = mongo.db.recipes.find({"created_by": session["user"]})
        return render_template("profile.html", username=username, recipes=recipes)
    
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
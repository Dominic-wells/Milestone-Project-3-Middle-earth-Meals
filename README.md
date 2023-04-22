# Milestone-Project-3-Middle-earth-Meals

![All the screens](/static/images/Allscreens.png)

Middle Earth Meals is a comprehensive, full-stack web application developed using the Flask framework and MongoDB as the underlying database. This project aims to provide a platform for users to manage recipes inspired by the rich cultures within J.R.R. Tolkien's Middle Earth universe. The application implements CRUD (Create, Read, Update, and Delete) functionalities, allowing users to interact with the recipe database effectively.

The platform is designed to cater to both registered and non-registered users, providing access to the extensive collection of recipes. Users who create an account can fully utilize the features offered by Middle Earth Meals, including adding new recipes, editing and deleting their own entries, and managing their account details.

The primary objective of this project is to create a seamless experience for users to discover, share, and collaborate on Middle Earth-inspired culinary creations, fostering a vibrant community of food enthusiasts and Tolkien fans. Middle Earth Meals serves as a robust and reliable platform for users to explore, create, and appreciate the diverse flavors of Middle Earth.

# Live Site

The live site is published here using Heroku - https://mem-site.herokuapp.com/

1. [Milestone-Project-3-Middle-earth-Meals](#milestone-project-3-middle-earth-meals)
   - [Live Site](#live-site)
2. [UX](#ux)
   - [User Stories](#user-stories)
   - [Design](#design)
     - [Color Scheme](#color-scheme)
     - [Typography](#typography)
     - [Responsiveness](#responsiveness)
   - [Wireframes](#wireframes)
3. [Features](#features)
   - [Features Left to Implement](#features-left-to-implement)
4. [Testing](#testing)
   - [Manual Testing](#manual-testing)
     - [Manual Testing Plan](#manual-testing-plan)
     - [Test Scenarios](#test-scenarios)
     - [Test Steps, Expected Results, and Success Criteria](#test-steps-expected-results-and-success-criteria)
5. [Testing Tools](#testing-tools)
6. [Errors and Bugs](#errors-and-bugs)
7. [Technologies Used](#technologies-used)
8. [Applications and Libraries](#applications-and-libraries)
9. [Database](#database)
   - [Categories](#categories)
   - [Users](#users)
   - [Recipes](#recipes)
10. [Deployment](#deployment)
    - [Heroku](#heroku)
    - [GitHub](#github)
11. [Acknowledgements](#acknowledgements)

## Ux

### User Stories

- As a visitor, I want to be able to browse through a variety of Middle Earth-inspired recipes so that I can find new and interesting dishes to try.

- As a visitor, I want to be able to search for specific recipes using keywords or filters, such as names or descriptions, to quickly find the recipes that interest me.

- As a user, I want to be able to access the platform on various devices, such as desktops, laptops, tablets, and smartphones, ensuring a consistent and user-friendly experience.

- As a registered user, I want to be able to create an account and log in, so I can access personalized features and have a more customized experience.

- As a registered user, I want to be able to add new recipes to the platform, sharing my own culinary creations with the community.

- As a registered user, I want to be able to edit and update my own recipes, ensuring that the information is accurate and up-to-date.

- As a registered user, I want to be able to delete my own recipes, giving me control over my contributions to the platform.

### Design

The Middle Earth Meals website is designed to evoke the fantasy atmosphere of J.R.R. Tolkien's universe, providing an immersive and visually appealing experience. The website's design elements are carefully chosen to reflect the enchanting world of Middle Earth and its diverse cultures. The design includes:

### Color Scheme

For our website, we have selected a captivating fantasy-inspired color scheme that harmoniously complements the Lord of the Rings-themed logo. Our primary colors are:

- Golden Yellow (#fec354) - evoking the aura of magical artifacts (color of a ring)

- Deep Teal (#007061) - embodying the mystique of enchanted forests

- Dark Forest Green (#005248) - representing the depths of the ancient realms

![Color Theme](/static/images/color%20theme.png)

### Typography

A fantasy themed typography was chosen

![Test Theme](/static/images/testtype.png)

### Responsiveness

The website aims to provide a fast and user-friendly experience for all users, regardless of whether they are accessing it from a desktop, tablet, or mobile device. Extensive testing has been conducted on all three platforms to ensure optimal performance. The site's design is adaptable to different screen sizes and device types, with layout adjustments made accordingly to ensure usability across all formats. The primary means of achieving this responsiveness is through the use of the Bootstrap CSS Framework.

### Wireframes

Balsamiq original Design:

<details><summary>A wireframe design in Balsamiq for the Home page</summary><img src="/static/images/memwireframes/Addrecipes.png"></details>
<details><summary>A wireframe design in Balsamiq for the Recipe page</summary><img src="/static/images/memwireframes/Recipes.png"></details>
<details><summary>A wireframe design in Balsamiq for the Add recipes page</summary><img src="/static/images/memwireframes/Addrecipes.png"></details>
<details><summary>A wireframe design in Balsamiq for the Edit recipes page</summary><img src="/static/images/memwireframes/Editrecipes.png"></details>
<details><summary>A wireframe design in Balsamiq for the Profile page</summary><img src="/static/images/memwireframes/Profile.png"></details>
<details><summary>A wireframe design in Balsamiq for the Login page</summary><img src="/static/images/memwireframes/Login.png"></details>
<details><summary>A wireframe design in Balsamiq for the Change password page</summary><img src="/static/images/memwireframes/Changepassword.png"></details>
<details><summary>A wireframe design in Balsamiq for the Register page</summary><img src="/static/images/memwireframes/Register.png"></details>

## Features

- **Homepage:** A landing page that welcomes users to the website.
- **Recipe Browsing:** Users can view and browse through all the available recipes on the website.
- **Recipe Search:** Users can search for specific recipes by entering a query, and the website will display relevant results based on the recipe name and description.
- **Add Recipe:** Users can submit their own recipes to the website by providing required information such as the recipe's name, category, description, ingredients, preparation steps, tools, notes, and an image URL.
- **Edit Recipe:** Users can edit existing recipes on the website by modifying the recipe's information.
- **Delete Recipe:** Users can delete their own recipes from the website.
- **User Registration:** New users can register on the website by providing a username and password.
- **Change Password:** Users can update their account password.
- **User Login:** Users can log in to the website using their registered username and password.
- **User Logout:** Users can log out of their account.
- **User Profile:** Displays the user's profile page with their username and the recipes they have added to the website. Users can also edit or delete their recipes from their profile page.

### Features Left to Implement

- Rating system: Allow users to rate and review recipes.
- Ingredient substitution suggestions: Provide alternative ingredients for users with dietary restrictions or preferences.

## Testing

### Manual Testing

I used manual testing to ensure that the website functions as expected and provides a smooth user experience.

### Manual Testing Plan

#### Test Scenarios

1. Homepage Accessibility
2. Recipe Browsing
3. Recipe Search
4. User Registration
5. Add Recipe
6. Edit Recipe
7. Delete Recipe
8. Change Password
9. User Login
10. User Logout

#### Test Steps, Expected Results, and Success Criteria

**1\. Homepage Accessibility**

- Steps:
  - Access the website's homepage.
- Expected Results:
  - The homepage is displayed with a welcome message.
- Success Criteria:
  - The homepage is accessible and displays the welcome message correctly.

* **PASS**

<details><summary>The website is accessiable and the homepage is displayed</summary><img src="/static/images/Memtesting/Test1homescreen.png"></details>

**2\. Recipe Browsing**

- Steps:
  - Navigate to the recipes page.
  - Browse the displayed recipes.
- Expected Results:
  - All recipes in the database are displayed and properly formatted.
- Success Criteria:
  - The recipe browsing feature works as expected

* **PASS**

<details><summary>The recipes are viewable</summary><img src="/static/images/Memtesting/Test2recipeviewing.png"></details><br/>

**3\. Recipe Search**

- Steps:
  - Enter various search queries (valid and invalid inputs) in the search bar.
  - Review the search results.
- Expected Results:
  - Relevant recipes are displayed based on the search query.
  - Appropriate error messages are shown when necessary.
- Success Criteria:
  - The search functionality works correctly and provides relevant results.

* **PASS**

<details><summary>Recipes in the database are found based on name and description </summary><img src="/static/images/Memtesting/Test3norecipesfound.png"></details><br/>

**4\. User Registration**

- Steps:
  - Access the "Register" page.
  - Create a new user account with a unique username and password.
  - Verify successful registration by accessing the user's profile page.
- Expected Results:
  - The new user account is created, and the user can access their profile page.
- Success Criteria:
  - The user registration process works as expected.

* **PASS**

<details><summary>User Registration</summary><img src="/static/images/Memtesting/Test4aregistration.png"></details>
<details><summary>User Profile</summary><img src="/static/images/Memtesting/Test4bregistration.png"></details><br/>

**5\. Add Recipe**

- Steps:
  - Log in with a valid user account.
  - Navigate to the "Add Recipe" page.
  - Submit a complete recipe form with valid information.
  - Check the recipes page for the added recipe.
- Expected Results:
  - The new recipe is successfully added to the website and displayed on the recipes page.
- Success Criteria:
  - The add recipe feature works as expected.

* **PASS**

<details><summary>Add Recipe Page</summary><img src="/static/images/Memtesting/Test5aaddrecipe.png"></details>
<details><summary>Inputting Recipe</summary><img src="/static/images/Memtesting/Test5baddrecipe.png"></details>
<details><summary>Successfully Added Message</summary><img src="/static/images/Memtesting/Test5caddrecipe.png"></details>
<details><summary>Recipe on Screen</summary><img src="/static/images/Memtesting/Test5daddrecipe.png"></details><br/>

**6\. Edit Recipe**

- Steps:
  - Log in with a valid user account.
  - Select an existing recipe.
  - Modify the recipe information and submit the form.
  - Verify the changes on the website.
- Expected Results:
  - The edited recipe is saved, and the changes are reflected on the website.
- Success Criteria:
  - The edit recipe feature works as expected.

* **PASS**

<details><summary>Edit Recipe Page </summary><img src="/static/images/Memtesting/Test6aedit.png"></details>
<details><summary>Editing Recipe </summary><img src="/static/images/Memtesting/Test6bedit.png"></details>
<details><summary>Successfully updated Message</summary><img src="/static/images/Memtesting/Test6cedit.png"></details>
<details><summary>Edit on Screen</summary><img src="/static/images/Memtesting/Test6dedit.png"></details><br/>

**7\. Delete Recipe**

- Steps:
  - Log in with a valid user account.
  - Select a recipe to delete.
  - Confirm the deletion.
  - Verify that the recipe is removed from the website.
- Expected Results:
  - The selected recipe is successfully deleted and no longer appears on the website.
- Success Criteria: - The delete recipe feature works as expected.

* **PASS**

  <details><summary>Recipe to delete </summary><img src="/static/images/Memtesting/Test7adeleted.png"></details>
  <details><summary>Recipe delete button </summary><img src="/static/images/Memtesting/Test7bdeleted.png"></details>
  <details><summary>Successfully Deleted Message</summary><img src="/static/images/Memtesting/Test7cdeleted.png"></details>
  <br/>

**8\. Change Password**

- Steps:
  - Log in with an existing user account.
  - Access the "Change Password" page.
  - Enter the old password and a new password.
  - Submit the form and verify the new password by logging in again.
- Expected Results:
  - The new password works, and the old password is no longer valid.
- Success Criteria: - The change password feature works as expected.

* **PASS**

  <details><summary>Change password button</summary><img src="/static/images/Memtesting/Test8achangepassword.png"></details>
  <details><summary>Change password form</summary><img src="/static/images/Memtesting/Test8bchangepassword.png"></details>
  <details><summary>Successfully changed password Message</summary><img src="/static/images/Memtesting/Test8cchangepassword.png"></details>
  <details><summary>Incorrect Username and/or Password Message</summary><img src="/static/images/Memtesting/Test8dchangepassword.png"></details>
  <br/>

**9\. User Login**

- Steps:
  - Access the "Login"
  - Enter a valid username and password.
  - Verify that the user is successfully logged in and redirected to their profile page.
- Expected Results:
  - The user is able to log in and access their profile page.
- Success Criteria: - The user login process works as expected.

* **PASS**

  <details><summary>User login</summary><img src="/static/images/Memtesting/Test9auserloggin.png"></details>

**10\. User Logout**

- Steps:
  - Log in with a valid user account.
  - Click on the "Logout" button or link.
  - Verify that the user is logged out and redirected to the login page.
- Expected Results:
  - The user is successfully logged out and can no longer access their profile page.
- Success Criteria: - The user logout process works as expected.

* **PASS**

  <details><summary>User logout</summary><img src="/static/images/Memtesting/Test10aaoggedout.png></details>

# Testing Tools

- <details><summary>W3C CSS Validator</summary><img src="/static/images/css Validator.png></details>
- <details><summary>Lighthouse report</summary><img src="/static/images/LightHouse.png></details>
- <details><summary>CIPepe8 Python validator</summary><img src="/static/images/Pythonpass.png></details>

Tested all HTML files using the W3C Markup Validation Service, which pointed out several errors due to the use of Jinja2 templating language. However, no other errors were detected in the HTML pages.

# Errors and Bugs

- Toggle bar will sometimes display over the logo
- Issue with adding square brackets to the Preparation_steps and Ingredients. The issue was that when it was splitting the ingredients and preparation steps by the newline character (\n), it was including the newline character in the resulting list. This means that each item in the list had a trailing newline character, which was causing the square brackets to appear in the template. Using the strip() method to remove any leading or trailing whitespace from each item in the list, I was able to remove the newline character and fix the issue.

# Technologies Used

- HTML
- CSS
- Python
- Flask
- JINJA Templating
- MongoDB (non relational DB)
- Git & GitHub
- Heroku

# Applications and Libraries

- Bootstrap Utilized to enhance website responsiveness and styling
- Visual Studio Code IDE used to code the site and its features
- Google Fonts Used to import fonts
- Utilized GitHub as online repository for code storage, commit messages, and versioning
- Heroku Used to make the site live
- Created wireframes during design phase using Balsamiq
- Font Awesome icons
- amiresponsive for Screenshot

## Database

MongoDB, a non-relational database, was utilized to store the collections outlined below. These collections were held in MemDb

###### categories

```
_id: <ObjectId>
Category_name: <String>
```

###### Users

```
_id: <ObjectId>
Username: <String>
Password: <String>(stored using SHA256)
```

###### Recipes

```
_id: <ObjectId>
Name: <String>
Category_name:<String>
Description: <String>
Ingredients: <Array>
Preparation_step: <Array>
Tools: <Array>
Notes: <string>
created_by: <string>
image_url <String>
```

### Categories:

This collection stores information about the different categories of recipes available on the website. Each document in the collection has the following fields:

- \_id: A unique ObjectId automatically generated by MongoDB to identify each document.
- Category_name: A string representing the name of the recipe category.

### Users:

This collection stores user account information. Each document in the collection has the following fields:

- \_id: A unique ObjectId automatically generated by MongoDB to identify each document.
- Username: A string representing the user's username.
- Password: A string containing the user's password, which is stored using the secure SHA256 hashing algorithm to ensure data privacy and security.

Recipes:
This collection stores the recipe information. Each document in the collection has the following fields:

- \_id: A unique ObjectId automatically generated by MongoDB to identify each document.
- Name: A string representing the name of the recipe.
- Category_name: A string representing the category the recipe belongs to.
- Description: A string containing a brief description of the recipe.
- Ingredients: An array of strings listing the ingredients required for the recipe.
- Preparation_step: An array of strings outlining the steps to prepare the recipe.
- Tools: An array of strings listing the tools needed to prepare the recipe.
- Notes: A string containing any additional notes or comments about the recipe.
- created_by: A string representing the username of the user who submitted the recipe.
- image_url: A string containing the URL of the recipe's image.

The database used in this project, MemDb, is an in-memory database that stores the data in the server's memory. It provides high performance and low latency access to the data, making it a suitable choice for this application.

## Deployment

### Heroku

```
1. Generate a "requirements.txt" file with the command "pip3 freeze --local > requirements.txt"
2. Produce a "Procfile" using the command "echo web: python app.py > Procfile"
3. Apply the changes to your repository by executing "git add -A", "git commit -m 'your commit message here'", and "git push"
4. Verify that a .gitignore file exists in your repository
5. Include "env.py" and "pycache/" in your .gitignore file to prevent exposure of sensitive data in your repository
6. Sign in or register for a Heroku account
7. Press "New" on the top-right corner of the dashboard and choose "Create new app"
8. Provide an "App name", select a region, and hit "Create app"
9. Navigate to the "Deploy" tab and choose "GitHub" under "Deployment method"
10. Locate your GitHub repository and press "Connect" (Note: avoid enabling automatic  deployment at this point to prevent errors)
11. Access the "Settings" tab and unveil Config Vars by clicking "Reveal Config Vars"
12. Input the key-value pairs corresponding to those in your env.py file:
13. Return to the "Deploy" tab and activate "Enable Automatic Deployment"
14. Under "Manual deploy" in the "Deploy" tab, choose "main"
15. Press "Deploy Branch"
16. Once the app finishes building, click "Open App" to launch your site.
```

### GitHub

```
1. Sign in to GitHub and find the desired GitHub Repository.
2. Beneath the repository name, select "Clone or download."
3. To clone the repository via HTTPS, copy the link provided under "Clone with HTTPS."
```

## Acknowledgements

- [Awesome README](https://github.com/matiassingers/awesome-readme)
- [How to write a Good readme](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)
- The people at Reddit for all your coding advice
- James for being the best coder I know and a real life saver
- Toby for being the best son money can buy

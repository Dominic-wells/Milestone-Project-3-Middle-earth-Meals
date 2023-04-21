# Milestone-Project-3-Middle-earth-Meals

Middle Earth Meals is a comprehensive, full-stack web application developed using the Flask framework and MongoDB as the underlying database. This project aims to provide a platform for users to manage recipes inspired by the rich cultures within J.R.R. Tolkien's Middle Earth universe. The application implements CRUD (Create, Read, Update, and Delete) functionalities, allowing users to interact with the recipe database effectively.

The platform is designed to cater to both registered and non-registered users, providing access to the extensive collection of recipes. Users who create an account can fully utilize the features offered by Middle Earth Meals, including adding new recipes, editing and deleting their own entries, and managing their account details.

The primary objective of this project is to create a seamless experience for users to discover, share, and collaborate on Middle Earth-inspired culinary creations, fostering a vibrant community of food enthusiasts and Tolkien fans. Middle Earth Meals serves as a robust and reliable platform for users to explore, create, and appreciate the diverse flavors of Middle Earth.

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

### Wireframes

Balsamiq original Design:

<details><summary>A wireframe design in Balsamiq for the Home page</summary><img src="/static/images/mem wireframes/Home.png"></details>
<details><summary>A wireframe design in Balsamiq for the Recipe page</summary><img src="/static/images/mem%20wireframes/Recipes.png"></details>
<details><summary>A wireframe design in Balsamiq for the Add recipes page</summary><img src="/static/images/mem wireframes/Add%20recipes.png"></details>
<details><summary>A wireframe design in Balsamiq for the Edit recipes page</summary><img src="/static/images/mem wireframes/Edit Recipes.png"></details>
<details><summary>A wireframe design in Balsamiq for the Profile page</summary><img src="/static/images/mem wireframes/Profile.png"></details>
<details><summary>A wireframe design in Balsamiq for the Login page</summary><img src="/static/images/mem wireframes/Login.png"></details>
<details><summary>A wireframe design in Balsamiq for the Change password page</summary><img src="/static/images/mem wireframes/Change password.png"></details>
<details><summary>A wireframe design in Balsamiq for the Register page</summary><img src="/static/images/mem wireframes/Register.png"></details>

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

<details><summary>The website is accessiable and the homepage is displayed</summary><img src="/static/images/memtesting/Test1 Homescreen"></details>

**2\. Recipe Browsing**

- Steps:
  - Navigate to the recipes page.
  - Browse the displayed recipes.
- Expected Results:
  - All recipes in the database are displayed and properly formatted.
- Success Criteria:
  - The recipe browsing feature works as expected

* **PASS**

<details><summary>The recipes are viewable</summary><img src="/static/images/memtesting/Test2 Recipe Viewing"></details><br/>

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

<details><summary>Recipes in the database are found based on name and description </summary><img src="/static/images/memtesting/Test3 No Recipes Found"></details><br/>

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

<details><summary>User Registration</summary><img src="/static/images/memtesting/Test4a Registration"></details>
<details><summary>User Profile</summary><img src="/static/images/memtesting/Test4b Registration"></details><br/>

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

<details><summary>Add Recipe Page</summary><img src="/static/images/memtesting/Test5a Add Recipe.png"></details>
<details><summary>Inputting Recipe</summary><img src="/static/images/memtesting/Test5b Add Recipe.png"></details>
<details><summary>Successfully Added Message</summary><img src="/static/images/memtesting/Test5c Add Recipe.png"></details>
<details><summary>Recipe on Screen</summary><img src="/static/images/memtesting/Test5d Add Recipe.png"></details><br/>

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

<details><summary>Edit Recipe Page </summary><img src="/static/images/memtesting/Test6a Edit.png"></details>
<details><summary>Editing Recipe </summary><img src="/static/images/memtesting/Test6b Edit.png"></details>
<details><summary>Successfully updated Message</summary><img src="/static/images/memtesting/Test6c Edit.png"></details>
<details><summary>Edit on Screen</summary><img src="/static/images/memtesting/Test6d Edit.png"></details><br/>

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

  <details><summary>Recipe to delete </summary><img src="/static/images/memtesting/Test7a Deleted.png"></details>
  <details><summary>Recipe delete button </summary><img src="/static/images/memtesting/Test7b Deleted.png"></details>
  <details><summary>Successfully Deleted Message</summary><img src="/static/images/memtesting/Test7c Deleted.png"></details>
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

  <details><summary>Change password button</summary><img src="/static/images/memtesting/Test8a Change Password.png"></details>
  <details><summary>Change password form</summary><img src="/static/images/memtesting/Test8b Change Password.png"></details>
  <details><summary>Successfully changed password Message</summary><img src="/static/images/memtesting/Test8c Change Password.png"></details>
  <details><summary>Incorrect Username and/or Password Message</summary><img src="/static/images/memtesting/Test8d Change Password.png"></details>
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

  <details><summary>User login</summary><img src="/static/images/memtesting/Test9a User Loggin.png"></details>

**10\. User Logout**

- Steps:
  - Log in with a valid user account.
  - Click on the "Logout" button or link.
  - Verify that the user is logged out and redirected to the login page.
- Expected Results:
  - The user is successfully logged out and can no longer access their profile page.
- Success Criteria: - The user logout process works as expected.

* **PASS**

  <details><summary>User logout</summary><img src="/static/images/memtesting/Test10a Logged Out.png></details>

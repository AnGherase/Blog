# What does it do and what does it fulfill?
This project uses skills to build a full-stack website around business logic and centrally-owned dataset. The purpose of creating this platform was for the users to view be able to shop for products. Users can also search for products that contain the searched word in its tags, title or description. So in essence Andreea’s Shop is a website created to give users access and full control over their orders. The platform features amazing colors and pictures from catalogues. The project can be viewed at: 
https://github.com/AnGherase/Blog
## UX
### Project purpose
The goal of Andreea’s website is to give users full access and control over their orders connected to the ability to choose from the desired products catalogue. This means they can create orders, view all orders, update, and delete any order.
### User experience
The project needs to meet its original purpose. The goal is to have the online customer return after a good experience and not have the user give up because of a hard registration. The perfect result of a successful user experience is a combination of desirability, viability and feasibility. Engagement drives customer value. Other UX objectives are to save time, effort and money, reduce misinterpretations, risk and waste, increase adaptability and focus. 
Users are presented with a catalogue icon at the top of the screen for mobile and tablet display and a navigation bar on desktop and display for Home, List of Products and Add products. A logo has been included to help easily navigate back to the homepage at any given time. An introductory heading has been included to guide the user to the website. A search bar has been included so the users can search for a product they would want to find right away. In case a user has mistakenly inputted a wrong path in the URL, a 404 page will show with a link back to the home page. Edit products fields are filled out automatically so that the user does not need to input all the previous values back in before they submit an update. When the delete button is clicked on the Orders page, the user is presented with a way to ensure they want to delete the order permanently.
The user's goal by using this website includes being able to see a well-functioning website to attract him to use it, navigation/buttons that are simple, full control over all orders in the cart, clear separation between each instruction.
The developer's goals include: having every feature reacting to its intended purpose, showing clear examples of the usage of HTML, CSS, JavaScript, jQuery and Python.
The value provided is that users can advance their own goals by authenticating on the site and paying for some of its products. Before that, the site makes clear how the goals would be furthered by the site. The site/shop owner is able to make money by providing this range of products to the users. There is no regular way to bypass the site’s mechanisms and derive all of the value without paying.
### Design/Styling of the website
The design of the website was chosen to ensure that the user has the best experience. Styles have been chosen to give it a professional and good-looking design. This was also reflected at the level of the Edit and Delete Buttons, as well as Forms, and Images.
The information architecture has been designed keeping in mind the user goals. “The purpose of your Information Architecture (IA) is to help users understand where they are, what they’ve found, what’s around, and what to expect.” (Peter Morville). The main IA components (organization structures, labeling systems, navigation systems, search systems)
The sample flow consists of the following steps:
•	Directing to the website (shop);
•	Home page;
•	Blog section of interest;
•	Interaction;
•	Completes input.
The goals when designing a user interface were to have it fast, simple and goal-oriented, useful/usable and delightful, authentic/appealing.
The following design principles were followed:
1.	Consistency helps the user to find what they are looking for. Users learn faster how the system works. This is achieved through patterns-using the same pattern whenever possible (e.g. the same position of buttons or side bar). It is also achieved by using known order principles (conventional, frequency of use, order of use, categorical, alphabetical). The same icons are used for the same actions.
2.	Hierarchy helps the user to understand the relationship and importance of elements and reduces complexity. It is achieved by using proximity-positioning elements close to each other to achieve the group look.
3.	Visual clarity-helps the User to achieve his goal fast and efficient and is accomplished through:
•	using white space, 
•	simplification and using less information,
•	shorter sentences and using fewer words, 
•	positioning elements in fewer directions (also important inside of the elements);
•	strategic usage of color
•	good readability and contrast
4.	User guidance-through which tasks can be completed efficiently and intuitively and leading the user’s attention, by reveal/guide functionalities, through clear call to actions, through recommendation of an option, through notifications and user messages.
In order to improve the user experience for the blog section, I gave focus to the text input as soon as the page loads so that the user can type directly in it. I also captured keyboard key pressed events to identify the Enter/Return Key and fire the click event on the submit button. The user will either be able to click the button or press the Enter/return key to send a message.
-sharing posts via email;
-adding comments to a post;
-tagging posts;
-recommending similar posts;
-creating custom tags and filters;
-adding a sitemap and a post-feed;
-implementing full-text search;
-creating feeds for the blog posts;
-adding full-text search to the blog (including multiple search fields)
### Functionality of project
The website is fully responsive and uses MongoDB for the users and products collection. Logged in users are able to create, update (edit) and delete their own products. Any user can search for products using the search box. A user can also log out. The Products page shows all products in order of the amount of views each product has. The pagination of the products is done by the database. Each product on the products page can be clicked onto and that will load the single products page which shows the entire entry. If the user created/added the product on this page, they will not be able to edit and delete this product. The add product allows the logged in user to create a product and enter it onto the database. Django was used to set up an user authentication system and user account system which has been tested.
### Pagination features
Are reflected on the Home Page, Products Listing Page, actual Products Page, Add Products Page, Delete Products Page, Update Products Page. When the user arrives at the Products page, they are presented with the entire product, showing the products name, products image, product description, brand. A delete button has been included so that the user has the option to delete the film and a detailed instruction on how to do so has been included.
When the user arrives at the Add Product to cart page, they are presented with a form which will show the following fields: Product Name, Product Description, Product Image URL, Add to cart 'button'.
When the user arrives at the Delete Product from cart page, they are presented with a form which will show the fields: product Name, Product Description, Product Image URL, Update Cart button.
Features left to implement
Some of the features left to implement include:
1.	Community tab-which can be accessed by all users for the purpose of exchanging opinions on the content.
2.	Pagination-on products page and on the start page which would facilitate the navigation.
3.	Logging in-for the user to have control over his own products and is owned by the user.
4.	Search page-where the user would be presented with a title showing how many search items have been found of whatever query was inputted into the search field. Then the user would be given the option to search for another item. If no results had been found then the user would be informed of that.
5.	Error 404 page-if at any time the user had inputted a value in the URL that has not been found, a 404 page will be presented and it will show the user a message that they got lost and will have a button which will lead them to the home page.

### Database
The database used for this project was SQLite database called MongoDB as required. The data used are: ObjectID, String, Int32. A database was created called 'myProducts' which contains a collection called products which is where each piece of data for each product is stored. The data structure is as follows:
### Technologies used
I used the following languages, frameworks, libraries to construct this project:
•	HTML5-used for structuring and presenting the content (main navigation menu which will handle the clothing dropdowns)
•	CSS/Bootstrap 4-used for the presentation of the web/home page, including the colors, layouts and fonts as well as styling of the payment form
•	JavaScript-used for creating the web page and enhancing user experience
•	Python
•	Django-used for building the project backend by a relational database to create a website that allows users to store and manipulate data records about the domain. In this case it was used for building the shopping cart to allow users to keep selected products while they browse the site
•	MySQL-relational database
•	jQuery-used to make it easier to use JavaScript on the website, to simplify DOM manipulation
•	Github-used as a remote backup of code used in the project and for version control
•	Braintree-integrating the payment gateway into the project
### Deployment
This section describes the process I went through to deploy the project to a hosting platform (Heroku). The website was created in Gitpod, a local Git directory was used for version control and then uploaded to Github.  The details of the database connection are found inside the requirements.txt -it uses the os class environ method to point to its own config available in order to keep the production database connection string secret. There were no differences between the deployed version and the development version.

The following had to be installed on the computer before deployment: PIP, Python 3, Git, as well as having an account in MongoDB Atlas.

The deployment to Heroku consisted mainly of the following steps: adding a requirements.txt file by using the command "sudo pip3 freeze-local> requirements.txt " which will add all the components needed to be used for the project; using "git add" to commit the changes ready to push to Github; creating the repository in Github and following the instruction in order to push the work up to Github; using "git push" and entering the email and password when instructed which will push all the files which have been committed up to Github; signing in to Heroku; creating a new app inside Heroku and then going to "Deploy" and scrolling down the list of instructions given to deploy the project in Heroku; viewing the project in Heroku by clicking "Open App".
### Testing
By testing I checked that all the user stories from the UX section worked as intended, with the project providing an easy and straightforward way for the users to achieve their goals. My tests checked the page loading, as well as the business logic of the views. The testing process can be described via scenarios.
The Create Order cart page was tested by checking that a product was entered, the page redirects and the new product is featured on the index page. The Products page is tested by searching for any products on the products page, getting its ID number and going to that Products details page and changing some data and committing it. This then redirects the user to the Index page and that is tested that the information has changed on that product. The Delete Orders page is tested by going to its products details page and deleting it, then checking that the redirect has happened and that the product does not appear on the index page. It is impossible to cover everything in testing, but the majority of elements were tested. My focus was on keeping the design usable and simple to navigate. As the site is built with responsive design, it works for mobile devices and I have checked it on iphones 6 to x, Smsung galaxy, ipads (mini to pro), Google's pixel 2 and 3. I also tested it on several browsers (Chrome, Explorer, Edge).
The payments in Stripe were also tested. 
### Credits
The content has been written by me, the developer. The mentor (Spencer Barriball) has been very helpful in guiding me through the process and provided useful tips.


# Roll4

![mockup](roll4app/static/readme/mockup.jpg "A mockup picture for the Roll4 project.")

["Roll4"](https://shirral.github.io/Roll4/) is a simple tool meant to make everyday decisionmaking easier and more fun. Need a hand deciding what to watch at a movie night? Deciding what kind of pizza to order? Or which chores to tackle first? Roll4 has you covered.

Inspired by the decision wheels and by the RPG dice, both of which can be used to determine an option among a set of options at random, Roll4 allows the user to create lists where every option corresponds to a number on one of the dice's side. The user can then either roll a physical die and compare the number with the position on their list, or use the built-in virtual die roll functionality, which will also highlight the rolled option for them.

Roll4 also supports Task Mode for the lists where the list items should be possible to tick off the list, and not be rolled again.

## User Experience & User Interface (UX/UI)

### Site goals

The goal of the site is to provide the user with a handy tool to aid their decisionmaking in the situations where they're faced with many different options to choose from. Some of us are indecisive creatures - that's okay, this is why Roll4 was built! - and some of us just like the fun of letting fate guide their decisions. The lists created by the user are meant to be reused - they won't go away the next time the user opens the app; and the state of completion of the lists in Task Mode will be saved, too.

### User stories

**First time visitor goals:**

* As a first time visitor, I want to learn what the app is about.
* As a first time visitor, I want to create an account.
* As a first time visitor, I want to create my first list.
* As a first time visitor, I want to create some categories for my lists.

**Returning visitor goals:**

* As a returning visitor, I want to log in to my account.
* As a returning visitor, I want to use my lists.
* As a returning visitor, I want to edit and/or delete my lists.
* As a returning visitor, I want to edit and/or delete my categories.
* As a returning visitor, I want to try the Task Mode to use my list for one-off tasks that should be completed once and for all.

### Design

**Colour scheme**

The colour scheme of the app focuses three main colours from the Materialize framework's palette: grey, deep orange, and white. In addition to that, the lightest variant of brown (#efebe9) has been used for the background of the main screens of the app. The full colour palette:

![colour palette - default mode](roll4app/static/readme/colours1.png "A colour palette for the interface elements.")

The app also features a dark theme which can be toggledd off/on in the user profile settings. It inverts most colours, using a dark grey background and a white font; the deep orange text has been made lighter. The colour palette for the dark mode:

![colour palette - dark mode](roll4app/static/readme/colours2.png "A colour palette for the interface elements in the dark mode.")

The home page, login and register screens, as well as the error screens also use the dark palette, with a dark grey background, white text, and deep orange accents:

![colour palette - home page, login, register and not logged in screens, error screens](roll4app/static/readme/colours3.png "A colour palette for the home page, login, register and not logged in screens and the error screens.")

The users are able to choose a colour for each of the categories they create to tell the lists belonging to them more easily. Twelve colours (11 from the Materialize's colour palette, one custom) have been picked for this purpose:

![category colours](roll4app/static/readme/colours4.png "Colours available for the categories.")

**Typography**

The website features two fonts:

* **Lilita One** - a fun, energetic, bold font sans-serif used for the h1 headings, the logo, the name inputs, and the buttons, 
* **Comfortaa** - an easy to read, friendly sans-serif font used for any other text.

Both fonts are served by Google Fonts. Impact has been provided as a fallback font for Lilita One, as it's also a big, loud, bold typeface. The browser has been instructed to use its default sans-serif font as a fallback for Comfortaa as it's not as important for the reception of the project as Lilita One and, frankly, all the web safe sans-serif fonts look equally dull anyway.

**Imagery**

The visual goal for the project is to keep it simple and clean. The imagery is minimalistic, with simple icons, where needed, and black and white line pictures of the dice.

![dice pictures](roll4app/static/readme/dice.png "Pictures of the dice.")

**Wireframes**

The wireframes made in the planning stage of the project work have guided me later on. Although the final version of the project does not look exactly the same as what I initially had in mind - I ended up liking the final outcome better - many elements stayed the same: the colours of the login screen, the layout of the elements, the style of the buttons, and the navbar. The wireframes have been prepared with Figma.

![wireframes](roll4app/static/readme/wireframes.png "Initial wireframes.")
![wireframes](roll4app/static/readme/wireframes2.png "Initial wireframes.")
![wireframes](roll4app/static/readme/wireframes3.png "Initial wireframes.")

## Features

### Responsive design

The website responds to a wide variety of screen sizes. The Materialize framework handles the most breakpoints automatically, but a few elements have been given their own media queries to determine which version of the layout is shown to the user.

![responsive design](roll4app/static/readme/responsive.png "Comparison of the New List page on different screen sizes.")
![responsive design](roll4app/static/readme/responsive.png "Comparison of the homepage on different screen sizes.")
![responsive design](roll4app/static/readme/responsive.png "Comparison of the Add Category page on different screen sizes.")

### Flash messaged

All of the pages except for the **Homepage** and the **Not logged in page** have a dedicated section at the top of the page for displaying flash messages. The messages are used to greet the user after they register or log in, bid them goodbye when they log out or delete their profile, and confirm the successful execution of operations such as adding, editing, or deleting a list or a category.

![flash message](roll4app/static/readme/flash.jpg "A flash message displayed after the user logs in.")

### Navbar

The Materialize navbar is present on all the main pages extended from base.html - the standard pages the user sees after they log in. It provides the user with a quick access to all the main functionalities of the app. The logo, shown on the left on larger screens and in the middle on the smaller screens, is a link leading the user to the **Lists** page. On the very right of the navbar there is a user icon, taking the user to their profile settings. The standard links are displayed on the right side on the bigger screens and in the side menu shown after tapping on the burger icon, displayed on the left of the navbar on smaller screens.

![navbar](roll4app/static/readme/navbar.png "The navbar: mobile on the left, desktop on the right.")
![expanded mobile navbar](roll4app/static/readme/navbar2.jpg "Mobile navbar expanded.")

### Homepage

The simple homepage provides basic information about the application and how to use it. It invites the user to give it a try and presents them with links to **Login** and **Register** pages.

![homepage](assets/readme/homepage.jpg "Homepage.")

### Login/Register/Not logged in pages

The Login page, Register page, and Not logged in page follow the same simple design. The **Not logged in** page shows up whenever the user is trying to access a page they need to be logged in to see (any pages other than the Homepage, Login/Register pages, and the error pages). It informs the user that they need to be logged in to view the page and prompts them to log in with a big button. 

Log in and Register pages feature a form with two input elements - one for the username, the other for password - and a submit button. The forms are connected to a PostgreSQL database where the user data is being stored. The passwords are hashed with Werkzeug.
There is also a link to the Register page on the Login page and a link to the Login page on the Register page in case a registered user accidentally ends up at the Register page, or an unregister user is brought to a Login page.

![not logged in page, login page, register page](assets/readme/loginpages.png "The 'Not logged in', Login, and Register pages.")

### Error pages

The Error 404 and Error 500 pages follow the same simple design. They name the error, provide a brief description to the user, and suggest them an action to take - either going back to an existing page (Lists) in case of error 404, or trying to access the page again at a later time in case of error 500. They both offer the button with a link to help the user take that action. The button on the error 500 page brings the user to the page they were trying to access earlier.

![error pages](assets/readme/errorpages.png "The error pages.")

### Lists page

The lists page is the main viewpoint of the app. This is where all of the lists created by the logged in user can be seen. The list information is pulled from a MondoDB database.

![lists page](assets/readme/lists.jpg "The lists page.")

* **New list button:** Positioned above all of the existing list, the button provides the user with a quick access to creating a new list. It leads to the **New list** page.

![new list button](assets/readme/newlistbutton.jpg "New list button.")

* **List display section:** Below the new list button, all of the lists created by the user are displayed in the form of cards. They are grouped by the die associated with them. Each die section is only going to be displayed if there is at least one list of its kind in them - empty sections will be hidden.

If the lists are given categories, they will be dosplayed on the cards on the very right of them. Lists without a category assigned to them will display [None] as their category. If the category assigned to a list has been assigned a colour, the card will be of that colour.
After clicking on a card, the user will be taken to its **List view** page.

![list display section](assets/readme/listsection.jpg "List display section.")

### New list page

The New list page utilizes Materialize's grid system to align dice on the page. Here, the user picks the die that will determine the number of items in their list. Each option is represented with a picture of the die in question, its name, and a short description of what it represents. Clicking on each die (or their name, or description) leads the user to the **Add list** page of that specific type.

![new list page](assets/readme/newlist.jpg "New list page.")

### List view page

This is where the user can access the details of their list. The list information is pulled from a MondoDB database.

* **List name:** Displays the name given to the list by the user on the top of the page.

* **List item cards:** Each list item is displayed in a card accompanied by its associated number and a notes icon. The icon is only shown on the list items that have any notes added to them. If they do, the list item card can be clicked on for the notes to be shown. Clicking on a card that does not have any notes attached to it does not do anything.

![list item card](assets/readme/itemcard.gif "List item card.")

* **Roll die functionality:** Allows the user to pick a random item from the list. The number rolled will be shown underneath the "DIE ROLL!" section and the corresponding card will be highlighted.

![die rolling](assets/readme/rolldie.gif "Roll die functionality.")

* **Task mode functionality:** Turns the list into a one-off-tasks kind of an affair. After turning the toggle on, every list item can only be rolled once; the items which have been rolled previously will become greyed out. The list refreshes once all of the list items have been rolled, or if the user turns task mode off and on again.

![task mode](assets/readme/taskmode.gif "Task mode functionality.")

* **Back, edit list, delete list buttons:** Let the user navigate to: Lists page, List edit page for the current list, and a modal confirming list deletion, respectively.

![list view buttons](assets/readme/listviewbuttons.gif "Back, edit list, and delete list buttons.")

* **List delete modal:** Asks the user if they are sure they want to delete the list. Shown when the user clicks on the "delete list" button; hidden when the user clicks away from it or chooses one of the options. When list deletion is chosen, the list gets deleted from the database.

### Add/edit list pages

The add/edit list pages look nearly identical. When creating a new list, all of the fields are empty; the placeholder is shown in the input field for the list name. In the edit list page, the information already submitted by the user will be shown; the fields will be pre-populated with the information about the list saved in the database.

![add and edit list pages](assets/readme/addeditlist.png "Comparison of the add list and edit list pages.")

### Categories page

### Add/edit category pages

### User profile page

* **Dark mode toggle:** Allows the user to turn the dark mode on/off. The dark mode inverses the colour scheme of the main section of the app pages, providing ligh-coloured text, icons, and images on a dark background.

![list display section](assets/readme/listsection.jpg "List display section.")
![list display section](assets/readme/listsection.jpg "List display section.")


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

### Flash messages

All of the pages except for the **Homepage** and the **Not logged in page** have a dedicated section at the top of the page for displaying flash messages. The messages are used to greet the user after they register or log in, bid them goodbye when they log out or delete their profile, and confirm the successful execution of operations such as adding, editing, or deleting a list or a category.

![flash message](roll4app/static/readme/flash.jpg "A flash message displayed after the user logs in.")

### Navbar

The Materialize navbar is present on all the main pages extended from base.html - the standard pages the user sees after they log in. It provides the user with a quick access to all the main functionalities of the app. The logo, shown on the left on larger screens and in the middle on the smaller screens, is a link leading the user to the **Lists** page. On the very right of the navbar there is a user icon, taking the user to their profile settings. The standard links are displayed on the right side on the bigger screens and in the side menu shown after tapping on the burger icon, displayed on the left of the navbar on smaller screens.

![navbar](roll4app/static/readme/navbar.png "The navbar: mobile on the left, desktop on the right.")
![expanded mobile navbar](roll4app/static/readme/navbar2.jpg "Mobile navbar expanded.")

### Homepage

The simple homepage provides basic information about the application and how to use it. It invites the user to give it a try and presents them with links to **Login** and **Register** pages.

![homepage](roll4app/static/readme/homepage.jpg "Homepage.")

### Login/Register/Not logged in pages

The Login page, Register page, and Not logged in page follow the same simple design. The **Not logged in** page shows up whenever the user is trying to access a page they need to be logged in to see (any pages other than the Homepage, Login/Register pages, and the error pages). It informs the user that they need to be logged in to view the page and prompts them to log in with a big button. 

Log in and Register pages feature a form with two input elements - one for the username, the other for password - and a submit button. The forms are connected to a PostgreSQL database where the user data is being stored. The passwords are hashed with Werkzeug.
There is also a link to the Register page on the Login page and a link to the Login page on the Register page in case a registered user accidentally ends up at the Register page, or an unregister user is brought to a Login page.

![not logged in page, login page, register page](roll4app/static/readme/loginpages.png "The 'Not logged in', Login, and Register pages.")

### Error pages

The Error 404 and Error 500 pages follow the same simple design. They name the error, provide a brief description to the user, and suggest them an action to take - either going back to an existing page (Lists) in case of error 404, or trying to access the page again at a later time in case of error 500. They both offer the button with a link to help the user take that action. The button on the error 500 page brings the user to the page they were trying to access earlier.

![error pages](roll4app/static/readme/errorpages.png "The error pages.")

### Lists page

The lists page is the main viewpoint of the app. This is where all of the lists created by the logged in user can be seen. The list information is pulled from a MondoDB database.

![lists page](roll4app/static/readme/lists.jpg "The lists page.")

* **New list button:** Positioned above all of the existing list, the button provides the user with a quick access to creating a new list. It leads to the **New list** page.

![new list button](roll4app/static/readme/newlistbutton.jpg "New list button.")

* **List display section:** Below the new list button, all of the lists created by the user are displayed in the form of cards. They are grouped by the die associated with them. Each die section is only going to be displayed if there is at least one list of its kind in them - empty sections will be hidden.

If the lists are given categories, they will be dosplayed on the cards on the very right of them. Lists without a category assigned to them will display [None] as their category. If the category assigned to a list has been assigned a colour, the card will be of that colour.
After clicking on a card, the user will be taken to its **List view** page.

![list display section](roll4app/static/readme/listsection.jpg "List display section.")

### New list page

The New list page utilizes Materialize's grid system to align dice on the page. Here, the user picks the die that will determine the number of items in their list. Each option is represented with a picture of the die in question, its name, and a short description of what it represents. Clicking on each die (or their name, or description) leads the user to the **Add list** page of that specific type.

![new list page](roll4app/static/readme/newlist.jpg "New list page.")

### List view page

This is where the user can access the details of their list. The list information is pulled from a MondoDB database.

* **List name:** Displays the name given to the list by the user on the top of the page.

* **List item cards:** Each list item is displayed in a card accompanied by its associated number and a notes icon. The icon is only shown on the list items that have any notes added to them. If they do, the list item card can be clicked on for the notes to be shown. Clicking on a card that does not have any notes attached to it does not do anything. The cards are animated on hover, inviting the user to click them.

![list item card](roll4app/static/readme/itemcard.gif "List item card.")

* **Roll die functionality:** Allows the user to pick a random item from the list. The number rolled will be shown underneath the "DIE ROLL!" section and the corresponding card will be highlighted.

![die rolling](roll4app/static/readme/rolldie.gif "Roll die functionality.")

* **Task mode functionality:** Turns the list into a one-off-tasks kind of an affair. After turning the toggle on, every list item can only be rolled once; the items which have been rolled previously will become greyed out. The list refreshes once all of the list items have been rolled, or if the user turns task mode off and on again.

![task mode](roll4app/static/readme/taskmode.gif "Task mode functionality.")

* **Back, edit list, delete list buttons:** Let the user navigate to: Lists page, List edit page for the current list, and a modal confirming list deletion, respectively.

![list view buttons](roll4app/static/readme/listviewbuttons.gif "Back, edit list, and delete list buttons.")

* **List delete modal:** Asks the user if they are sure they want to delete the list. Shown when the user clicks on the "delete list" button; hidden when the user clicks away from it or chooses one of the options. When list deletion is chosen, the list gets deleted from the database.

### Add/edit list pages

The add/edit list pages look nearly identical. When creating a new list, all of the fields are empty; the placeholder is shown in the input field for the list name. In the edit list page, the information already submitted by the user will be shown; the fields will be pre-populated with the information about the list saved in the database.

![add and edit list pages](roll4app/static/readme/addeditlist.png "Comparison of the add list and edit list pages.")

* **List name:** Allows the user to name their list. The field is mandatory.

![list name](roll4app/static/readme/listname.jpg "List name field.")

* **Add/change category:** Clicking on the paragraph shows a dropdown menu where a category can be added to the list. Adding a category is optional.

![add/edit category](roll4app/static/readme/addcategory.jpg "Add/edit category functionality.")

* **List item input fields:** This is where all of the options to choose from go. Each of them will have a specific number assigned to it - these are shown on the left.

![list item input](roll4app/static/readme/listiteminput.jpg "List item input field.")

On the right of the text field, there is a button allowing the user to add/edit notes. When the button is hovered over, a Materialize tooltip appears, explaining the function of the button. When it is clicked, a text ares appears below the chosen list item input where notes about the list item can be added or edited.

![add/edit notes button](roll4app/static/readme/notesbtn.gif "Add/edit notes button.")

* **Cancel and save list/save changes buttons:** The cancel button on the Add list page brings the user back to the Lists page. The cancel button on the Edit list page brings them back to the List view page. The save list/save changes buttons send the information submitted by the user to the database.

![cancel and save list/save changes buttons](roll4app/static/readme/cancelsavebtns.jpg "Cancel and save list/save changes buttons.")

### Categories page

This is where all of the categories created by the user are displayed on the cards. The cards will have a colour associated with the category or remain white if no colour has been chosen. The cards are animated on hover, inviting the user to click them. Clicking on a category card will bring the user to the **Edit category** page for that category. Like the List viee page, the Categories page also has a button allowing the user to create a new category positioned above the existing categories.

![categories page](roll4app/static/readme/categories.jpg "The Categories page.")

### Add/edit category pages

The add/edit category pages look nearly identical. When creating a new category, all of the fields are empty; the placeholder is shown in the input field for the category name. In the edit category page, the information already submitted by the user will be shown; the name field and colour choice will be pre-populated with the information about the category saved in the database.

![add/edit category pages](roll4app/static/readme/editcreatecategory.png "Add/edit category pages.")

* **Category name iput:** A text field allowing the user to name the category.

![category name imput](roll4app/static/readme/categoryname.jpg "Category name input.")

* **Colour picker:** Allows the user to pick the colour associated with their category. The colourful circles are styled custom radio buttons.

![colour picker](roll4app/static/readme/colorpicker.jpg "Colour picker.")

* **Cancel, add category/save changes, and delete category buttons:** The cancel button returns the user to the categories page without saving anything to the database. The add category/save changed button saves the information about the category to the database, and then returns the user back to the Categories page. The delete category button brings up a selete category modal.

![cancel, add category/save changes, and delete category buttons](roll4app/static/readme/categorybtns.jpg "Cancel, add category/save changes, and delete category buttons.")

* **Category delete modal:** Asks the user if they are sure they want to delete the category. Shown when the user clicks on the "delete category" button; hidden when the user clicks away from it or chooses one of the options. When category deletion is chosen, the category gets deleted from the database.

![category delete modal](roll4app/static/readme/categorydeletemodal.jpg "Category delete modal.")

### User profile page

The profile page is very simple. It greets the user, allows them to turn dark mode on and off, and to delete their account.

* **User greeting:** The app pulls the user's userame from the database to deliver a personalised greeting.

![user greeting](roll4app/static/readme/greeting.jpg "User greeting.")

* **Dark mode toggle:** Allows the user to turn the dark mode on/off. The dark mode inverses the colour scheme of the main section of the app pages, providing ligh-coloured text, icons, and images on a dark background.

![dark mode toggle](roll4app/static/readme/darkmodetoggle.png "Dark mode toggle.")

Comparison of light mode vs. dark mode:

![dark mode](roll4app/static/readme/darkmode.png "Light mode and dark mode.")

* **Account deletion:** The user can also delete their profile. Clicking on the "Delete profile" link brings up a modal asking the user for confirmation. It works just like the other modals. 

![dark mode](roll4app/static/readme/delaccountmodal.gif "Light mode and dark mode.")

### Future features

Although the project is a simple one and it's meant to stay that way not to overwhelm the user with all the options and choices - in the end, it's an app meant to make the decisionmaking process easier - there are some fetures that might be nice to add in the future:

* **List sharing:** It would be nice to be able to share your lists with other users. It could be achieved by the target user providing the user sharing the list with a unique code generated for them by the application; the other user could then input the code as well as the other user's username as a safety feature preventing users to randomly sending unsolicited lists to others.

* **Custom die and a quick coin flip:** Although these are technically not dice anymore, it would be good to give users the option to create lists with a custom amount of items as well as an option of a quick "coin flip" - a random pick of one of the two items. It would extend the functionality and real-life applications of the app.

* **Improving the list card display on the List page on mobile devices:** For the lists with long names, or items with long category names - or both! - it would be good to change the way both of these are displayed on the cards to improve the cleanliness of the design and the readability.

* **Adding a die roll animation:** Seeing the tumbling die before getting the result would be more fun and engaging for the user.

* **Allowing the user to change them their username and password, and to provide a recovery email address which could be used to recover forgotten password.**

## Testing

### Validator Testing

* **HTML:**

  The initial testing has revealed a `<span>` tag that was not closed properly and the lack of a space character between the "id" and "class" attributes in two divs of the end screen. This has been fixed.

  The validator has also thrown a warning about the empty heading in the end screen that gets filled with the information on the player's victory or defeat through Javascript at the end of the game.

  It has also shown errors relating to the missing `alt` attribute for the image tags. I initially didn't see the purpose of adding it - the project is a game that is relies on visual imagery and the speed of reaction; the images don't fill any of the functions that normally call for using the attribute in web projects. I have added the attribute in the end, as there is no harm in that and it might be useful to be able to tell the images apart in case they fail to load.

  The second round of testing only showed the warning about the empty heading.

  [W3C validator](https://validator.w3.org/) was used.

* **CSS:**

  The validator did not find any errors.
  
  Warnings were shown about the vendor extensions I used to ensure that the styling I'm using will work on all the major browsers: `-webkit-user-select`, `-ms-user-select`, `-ms-overflow-style` and `::-webkit-scrollbar`.

  [W3C Jigsaw validator](https://jigsaw.w3.org/css-validator/) was used.

* **JS:**

  The validator has found one unnecessary semicolon at the end of a function definition. The semicolon was removed.

  [JQuery Validator](https://www.utilities-online.info/jquery-validator) was used.

* **Performance & best practices:**

  While [Lighthouse](https://chrome.google.com/webstore/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk) was satisfied with the page load of the project (all of the statistics in the green zone, ranging between 90-100% on both desktop and mobile device evaluation), it was less impressed when I evaluated the project using its Timespan mode so that the whole project and its interactivity would be assessed. Best Practices were rated 8/8, but the Performance was rated 14/22 (yellow zone).

  After I implemented some of the suggested changes (compressing the background images into the WebP format, adding the missing meta tag attribute), the latter went up to 17/22.

### Manual testing: Features


| Feature       | Expected behaviour | Action  | Result |
| ------------- |--------------------| --------|--------|
| *Responsive design* | When the project is viewed on different kinds of devices with different screen sizes, the design should remain clear and functional. The elements of the starting screen and end screen should resize to match the window size; the apples should generate on a smaller area on smaller screens, and be smaller, and take up more space on screens where more space is available. No elements should go beyond the edge of the screen. | The project is opened and the game is played on several different devices: a laptop (Acer Nitro 5), an Android phone (Ulephone Power Armor 14), and an iOS tablet (iPad Air 4th Generation). | The elements of the project respond to the different screen sizes correctly, changing their proportions to preserve the design and functionality of the game. |
| *Start screen* | The starting screen should load all its elements: the main heading, the div element with the main text, the background image, and the "TO THE ORCHARD!" button-like link. The main text should be scrollable within the bounds of the div on the smaller screens.  | The page is loaded. Scrolling the main text is attempted on a mobile phone (Ulephone Power Armor 14). | All of the elements are loaded correctly. The main text scrolls within its div on a mobile device. |
| *Start screen: "TO THE ORCHARD!" button* | The button should change its colour scheme (black should change to red) once it is hovered upon with a pointer. The starting screen should be replaced with the main game screen with the controls instructions overlay once the button is clicked. | The button is hovered over with a cursor, then it is clicked. | The button changes its colour scheme correctly. The starting screen is replaced with the main game screen with the controls instructions overlay. |
| *Controls instructions overlay* | The controls instructions overlay should be shown on top of the tree background once the main game screen is loaded. The animated gif images presenting the actions required from the player to pick and drop apples should display correcly and show the animation. Each image should be accompanied by a textual description of the action either directly below it (in case of bigger screens) or to its side (in case of small screens). Below them, a "START THE DAY!" button should be displayed. | The main game screen is loaded. | All of the elements load and display correctly. |
| *Controls instructions overlay: "START THE DAY!" button* | The button should change its colour scheme (black should change to pastel yellow, and vice versa; a thin black outline should appear) once it is hovered upon with a pointer. The overlay should disappear, the main game elements (timer, bin, apples) should be shown, and the game should begin. | The button is hovered over with a cursor, then it is clicked. | The button changes its colour scheme correctly. The overlay is hidden, the main game elements are shown, and the game starts correctly. |
| *Timer* | The timer should update the hour shown on the screen by 15 minutes every 5 seconds. When it reaches 16:00, the game should end and the main game screen should be replaced with the end screen. | The game is started and the timer is allowed to run until the hour shown in the screen reaches 16:00. | The timer updates the hour shown on the screen correctly. The game ends and the end screen is shown once it reaches 16:00 with all of its elements loading correctly. |
| *Randomly generated apples* | When the game starts, a random amount of apples between 5-40 appears on the screen, in randomly determined positions between the timer and the apple bin. While it's okay for the apples to cover the top of the bin, they should never cover the timer or go over the edge of the screen. The number of apples generated should never be below 5 or above 40 at a time. All 6 different kinds of apples (3 good, 3 bad) should be generating with a similar frequency. | The game is started multiple times so that several batches of apples are generated. | The apples are generated correctly. |
| *Apple bin* | The picture of the apple bin changes, showing the level of the fullness of the bin, once the following numbers of apples in the current bin are reached: 1, 13, 26, 40. When the bin is full, an animation is triggered that moved the picture of the full bin off the side of the screen, to the left, and brings in a picture of an empty bin back to the centre of the screen, from the right. | 40 apple images are clicked on. | The bin image swaps are happening at the right thresholds of apples picked. At 40 apples, the bin animation is triggered. It runs as expected. |
| *Apple tree background* | When the game is started and the main game screen is emptied of apples (they have been picked or dropped), the background image of an apple tree is animated off the side of the screen, to the left, and then slides back into its central position on the screen from the right. | The game is started and all the apples that generated are clicked on. | When the screen is empty of apples, the background image animation is triggered. It runs as expected. |
| *Game outcome section* | The heading at the very top of the page should say either "APPLE VICTORIA!" if the player has met the victory conditions or "APPLE DEFEAT!" if they have not. | The game is played twice. The first time, to win (good apples are picked, bad apples are dropped); the second time - to fail (no apples are picked or dropped). | The heading shows the correct message in both scenarios. |
| *Outcome text section* | The outcome text should inform the player how many bins of apples they picked and what percentage of them were rotten. It should provide feedback on how good the player's performance was. There are several different outcomes dependent on the player's speed and accuracy. | The game was played several times to achieve the following results: 3.5+ bins of apples picked, none of them rotten; 3.5+ bins of apples picked, one of them rotten; 3.5+ bins of apples picked, less than 5% of them rotten; 3.5+ bins of apples picked, 5%+ of them rotten; less than 3.5+ bins of apples picked, less than 5% of them rotten; less than 3.5+ bins of apples picked, 5%+ of them rotten; less than 0.5 bins of apples picked, rotten or not, and none apples picked at all. | Picking 0, 1, less than 5% and 5%+ of the bad apples, as well as picking no apples, have all shown different feedback on the amount of rotten apples in the second paragraph. The combinations 3.5+ bins, <5% rotten apples; 3.5+ bins, 5%+ rotten apples; <3.5 bins, <5% rotten apples; <3.5 bins, 5%+ rotten apples and <0.5 bins have all brought different supervisor feedback messages in paragraphs 3, 4, and 5. |
| *Score section* | The score should display 0 if the player has not met the victory conditions. If they have, the score should display the amount of apples picked by the player. | The game is played twice. The first time, to win (good apples are picked, bad apples are dropped); the second time - to fail (only a few apples are picked). | The score displays 0 when the game is lost and a number of apples picked (in this case, 153) when it is won. |
| *Try again button* | The button should change its colour scheme (dark green should change to light green, and vice versa; the outline should disappear) once it is hovered upon with a pointer. When the button is clicked, the game should be reset and the player should be brought back to the main game screen with the controls instructions overlay, ready to start another round. | The button is hovered over with a cursor, then it is clicked. | The button changes its colour scheme correctly. The end screen is replaced with the main game screen with the controls instructions overlay. |

### Manual Testing: Testing User Stories from the UX/UI section

**1. First Time Visitor Goals**

* *As a first time visitor, I am bored and I'm looking for some entertainment; I want to have fun.*

  * The user is brought to the starting screen. The imagery and the story introduction suggest the website might have something to do with picking apples; hopefully that makes the user curious. If they read the emphasised line on the bottom or click on the button, they will realise it's a game they can play to fend off their boredom for a bit. They click on the "GO TO THE ORCHARD!" button, learn the controls, click on the "START THE DAY!" button and play the game.

* *As a first time visitor, I have a few minutes to pass and I'm looking for something to do that won't take a long time.*

  * The user is brought to the starting screen. If they read the emphasised line on the bottom, they will realise the website contains a game that only takes about 3 minutes to play - just what they need. They can now click on the "GO TO THE ORCHARD!" button and play the game.

* *As a first time visitor, I am curious about apple picking and want to see how an apple picking simulator might work.*

  * The user is brought to the starting screen where they are presented with the flavour text that details the basic rules of apple picking. Then, after they click on the "GO TO THE ORCHARD!" button and familiarise themselves with the controls, they start the game by clicking on the "START THE DAY!" button. During the gameplay, they get to put what they've just learned into practice. At the end, they receive an evaluation of their efforts which is what they would likely be told by their supervisor if they picked a similar amount of apples of a similar quality at a real-life commercial farm.

**2. Returning Visitor Goals**

* *As a returning visitor, I want to try to beat my previous score in the game.*

  * After having played the game once and receiving their evaluation, the user can click on the "GIVE IT ANOTHER GO!" button to play again and try to achieve a better result. They can also refresh the website to start the game again from the starting screen. The user can always navigate to the website after having closed the page to play the game again, too.

* *As a returning visitor, I want to try to share the game with somebody who might find it funny - perhaps someone who has worked as an apple picker at a farm before.*

  * The user can copy the website's address and paste it in a message to their friend or, if they're on a mobile device, tap on the "share" button in their browser to share the game with others.

### Further Testing

The website has been tested on a variety of screen sizes (resizing the browser window on desktop, tablet, smartphones), browsers (Chrome, Safari, Opera, Edge, Firefox), and devices. Family and friends have been asked to perform additional testing on devices I had no access to (Macbook, iPhone).

The game performed well on all of the devices and browsers tested, although there were some unexpected differences between them:

* The performance on Chrome on iPad Air (4th Edition) was not as smooth as on other devices using the same browser, nor as the same device running Safari. The browser struggled to register apples being tapped quickly one after another to be picked; it did not have the same problem with swiping on the apples to drop them, though.

* Microsoft Edge would sometimes display an image search icon on the clicked apples, which was easy to click on accidentally when picking another apple nearby. This would disrupt the gameplay as it would prompt the browser to run the image search in a window that would pop up to the right side of the screen. Sadly, a programmatical way of disabling it doesn't seem to exist at the moment; the feature can only be turned off locally on the user's device. 

## Bugs fixed & problems overcome

| Problem description   |  Fix  |
| --------------------- | ----- |
| It was possible to click on the same apple numerous times before it was revomed from the DOM, getting it counted as if the player has picked similar apples. | A flag was added to the apple element the first time the user clicks on a given apple. A flag check was also added to run any time an apple is clicked - if the flag was already there, the rest of the picking or dropping function is going to be ignored. |
| The nextTree function would sometimes run several times, leading to several sets of apples generating all at once, if the player has been picking/dropping apples very quickly, making a lot of clicks. | Adding the flags and the flag checks described above has solved this issue, too. |
| The apple bin wouldn't always return to the central position after the animation of it being moved to the side and returning from the other side would finish. The way the bin images were being swapped while the animation was running was to blame. | Pre-loading all the images and using `.show()` and `.hide()` methods has solved the issue. |
| Accidentally dragging or selecting the apple images would stop the click event, interfering with the gameplay and making it impossible to play the game quickly as it's meant to be played. | `ondragstart="return false"` has been added to the `<body>` element in the html file and the `user-select: none;`, `-webkit-user-select: none;` and `-ms-user-select: none;` rules have been added to the css class applied to the apples and other chosen elements. |
| Adding a swipe event for the dropping action on mobile devices proved to be quite a challenge, even though I have found several external libraries that offer the functionality I needed. After a lot of trial and error, it turned out that my apple elements were too small for the script I used to work reliably. | Tweaking the settings in the downloaded library a little has solved the issue. |
| The iPads allow for the display of the context menu if the user taps and holds on an apple or a bin. | `-webkit-touch-callout: none;` has been added to the css class used for preventing selection of images. |
| The second and following bins would not be positioned in the center of the screen after the window was resized. This happened both on computers and mobile devices (if the orientation was changed during the game) and was due to the fact that the nextBin function calculates the bin's current position to pass it to the animation, which  desn't accept standard values for centering, overriding the css margin settings from the stylesheet; the new position wouldn't be central anymore if the screen was suddenly resized. | jQuery's `.resize` method was used to listen for any screen size changes, and to apply the original margin that centers the bin element to it. |

## Technologies and Resources used

### Programming languages used:

* **HTML5**
* **CSS3**
* **JavaScript**

### Frameworks & Libraries Used:

* **[jQuery](https://jquery.com/)**
* **[swipe events by jquery](https://codepen.io/w3codemasters/pen/qvVwGQ)**
* **[Google Fonts](https://fonts.google.com/)**

### Software & other technologies used:

* **[Visual Studio Code(https://code.visualstudio.com/)]** - IDE the project was written in. Used with the **[Live Server (Five Server)](https://marketplace.visualstudio.com/items?itemName=yandeu.five-server)**, **[HTML Boilerplate](https://marketplace.visualstudio.com/items?itemName=sidthesloth.html5-boilerplate)** and **[IntelliSense for CSS class names in HTML](https://marketplace.visualstudio.com/items?itemName=Zignd.html-css-class-completion)** extensions.
* **[GitHub Desktop](https://github.com/apps/desktop)** - used for version control and pushing commits to GitHub.
* **[Canva](https://www.canva.com/)** - used to get the screens mockup base.
* **[Photopea](https://www.photopea.com/)** - used to prepare the images for the readme file.
* **[Procreate](https://procreate.com/)** - used to draw the images of the apple tree, the apples, the apple bins, and the static images for the animated gifs showing the controls.
* **[Ezgif](https://ezgif.com/maker)** - used to put the static images for the controls instructions gifs together into animated gif files and to convert video into gif files for the readme.
* **[Microsoft Copilot](https://copilot.microsoft.com/)** - used to create the background images for the starting screen and for the end screen.
* **[Img.Upscaler](https://imgupscaler.com/)** - used for upscaling the images generated with Copilot.
* **[IMAGECOLORPICKER](https://imagecolorpicker.com/)** - used to grab the colours to use in the design of the website from the generated images.
* **[Snipping Tool](https://apps.microsoft.com/detail/9mz95kl8mr0l?hl=en-US&gl=US)** - used to for the screen recording to create the animated gifs for the readme file.

### How-to references used:

* [right click event](https://api.jquery.com/contextmenu/)
* [swipe event](https://codepen.io/w3codemasters/pen/qvVwGQ )
* [checking if a div is empty](https://www.geeksforgeeks.org/how-to-check-an-html-element-is-empty-using-jquery/)
* [figuring out how to create the timer](https://www.w3schools.com/jsref/met_win_setinterval.asp), [another resource for this](https://developer.mozilla.org/en-US/docs/Web/API/setInterval)
* [rounding numbers to 1 decimal point](https://www.altcademy.com/blog/how-to-round-numbers-in-javascript/)
* [preventing user selection](https://www.w3schools.com/howto/howto_css_disable_text_selection.asp)
* [preventing dragging](https://stackoverflow.com/questions/62097523/disable-dragging-of-image-in-entire-project-html-pages)
* [hiding the scroll bar](https://www.w3schools.com/howto/howto_css_hide_scrollbars.asp)
* [fixing issues with media queries not being applied properly](https://blog.openreplay.com/understanding-css-media-queries/)
* [media queries - detecting touch devices](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Media_queries), [another resource for this](https://stackoverflow.com/questions/26546254/how-to-write-css-media-queries-to-detect-a-touchscreen-device)
* [cursor - pointer](https://developer.mozilla.org/en-US/docs/Web/CSS/cursor)
* [converting seconds to a hh:mm time format](https://www.geeksforgeeks.org/how-to-convert-seconds-to-time-string-format-hhmmss-using-javascript/ )
* [preventing the context menu on a long tap on mobile Apple devices](https://stackoverflow.com/questions/12304012/preventing-default-context-menu-on-longpress-longclick-in-mobile-safari-ipad), [another resource for this](https://developer.mozilla.org/en-US/docs/Web/CSS/-webkit-touch-callout)
* [event listener for screen resize action](https://stackoverflow.com/questions/2996431/detect-when-a-window-is-resized-using-javascript)

### Project guidance & assistance:

* **My Mentor, Mitko Bachvarov** - thank you for your feedback and guidance!
* **My friend Luís** - thank you for all the troubleshooting help, and for showing me how to do debugging!

## Deployment

### GitHub Pages

The project was deployed to GitHub Pages as follows:

1. I opened GitHub and located the project's repository.

  ![locating the repository](assets/readme/deployment-1.png "Locating the project's repository.")

2. I entered the repository and opened its settings.

  ![settings](assets/readme/deployment-2.png "The repository's settings.")

3. There, in the menu on the left of the screen, I located Pages.

  ![accessing Pages](assets/readme/deployment-3.png "Accessing Pages.")

4. Under "Build and development", there is a "Branch" section. I chose the `main` branch from the dropdown menu and clicked on the `Save` button.

  ![choosing the branch](assets/readme/deployment-4.png "Choosing the main branch.")

5. That's it! The site is now deployed and can be accessed from the link created by GitHub. The link can be found on the top of the "Pages" page once it refreshes.

  ![live website link](assets/readme/deployment-5.png "Live website link.")

### Forking the project on GitHub

If, for whatever reason, anyone would like to get themselves a copy of this project to tinker with on their own - feel free to do so! Here is how to do it so you can have your own copy of the entire repository that you can do whatever you please with, without causing any changes to the original:

1. Open the repository of this project on GitHub. It can be found [here](https://github.com/Shirral/Apple-Victoria).

2. Find the "Fork" button located between the "Watch" and "Star" buttons, near the top of the repository page.

  ![forking](assets/readme/fork.png "Forking the project.")

3. Done! Go back to your profile - you will find the copy of the project in your repositories.

### Cloning the project on GitHub *(instructions copied from GitHub Docs)*

1. On GitHub.com, navigate to the main page of the repository.

2. Above the list of files, click `Code`.

  ![cloning](assets/readme/clone-1.png "Cloning the project.")

3. Copy the URL for the repository.

* To clone the repository using HTTPS, under "HTTPS", click on the 'copy' icon.
* To clone the repository using an SSH key, including a certificate issued by your organization's SSH certificate authority, click SSH, then click on the 'copy' icon.
* To clone a repository using GitHub CLI, click GitHub CLI, then click on the 'copy' icon.

  ![cloning](assets/readme/clone-2.png "Cloning the project.")

4. Open Git Bash.

5. Change the current working directory to the location where you want the cloned directory.

6. Type `git clone`, and then paste the URL you copied earlier.

7. Press Enter to create your local clone.

## Live website link:

[https://shirral.github.io/Apple-Victoria/](https://shirral.github.io/Apple-Victoria/)
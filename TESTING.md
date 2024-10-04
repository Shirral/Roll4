## Testing

### Validator Testing

* **HTML:**

All of my html templates have been put through the validator. Nearly all of the warnings/errors shown to me by the validator had to do with the use of Jinja templating engine, which was not recognised by the validator. However, the validator caught three valid issues:

* I forgot to include the 'alt' attributes for my img elements. This is now fixed.
* One of my forms containing a switch element - a styled checkbox, the value of which is sent to the database through an 'onchange' attribute rather than a classic submit button - had an empty 'action' attribute. The attribute has been removed.
* One of my 'id' attributes was duplicated within the same page. The id, used for styling, has been chenged to a class.

[W3C validator](https://validator.w3.org/) was used.

* **CSS:**

The validator was not impressed with my &:hover rule sets inside of the standard rule sets. It called Parse Error on them, so I changed them to the standard element:hover rule sets.

Warnings were shown about the vendor extensions I used to ensure that the styling I'm using will work on all the major browsers: `::-ms-input-placeholder` and `-ms-transform`.

[W3C Jigsaw validator](https://jigsaw.w3.org/css-validator/) was used.

* **JS:**

The validator has found four missing semicolons and two unnecessary semicolons at the end of function definitions. The semicolons have been fixed.

[JQuery Validator](https://www.utilities-online.info/jquery-validator) was used.

* **Python:**

All of my Python files (`app.py`, `__init__.py`, `models.py`, and `routes.py`) have been put through the validator. The validator did not find any issues.

[ExtendsClass Python syntax checker](https://extendsclass.com/python-tester.html) was used.
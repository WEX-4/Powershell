# TASKS P1.2, P4.5

from flask import render_template, request
from database import create_fact

def create_route():
    if request.method == "GET":
        # DONE: (Task P1.2) Render the create.html template
        return render_template("create.html")

    if request.method == "POST":
        # DONE: (Task P1.2) Get the fact_text from the form
        fact_text = request.form.get("fact_text")

        # TODO: (Task P4.5) Get the category from the form

        # DONE: (Task P1.2) Check that fact text is provided, if not return an error
        if not fact_text:
            return "fact_text is required", 400
        
        # DONE: (Task P1.2) Call the create_fact function from the database folder
        create_fact_entity = create_fact(fact_text)

        # TODO: (Task P4.5) Pass the category to the create_fact function

        return render_template('create.html', random_fact = create_fact_entity.fact()) # DONE: (Task P1.2) Pass the HTML template, fact and 
        # TODO: category (Task P4.5) parameters

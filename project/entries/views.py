from flask import render_template, url_for, flash, request, redirect, Blueprint
from flask_login import current_user, login_required
from werkzeug.utils import secure_filename
from project import db
import json
from project.models import Entry
from project.entries.forms import EntryForm
import re


entries = Blueprint('entries', __name__)

@entries.route('/upload', methods = ['GET', 'POST'])
@login_required
def upload_entries():
    form = EntryForm()
    message = ""
    if form.validate_on_submit():
        f = request.files['file']
        if f.filename[-5:].lower() == ".json":
            try:
                filename = secure_filename(form.file.data.filename)
                form.file.data.save('uploads/' + filename)
                r = open('uploads/' + filename, "r")
                data = json.loads(r.read())
                r.close()
                for i in data:
                    temp = Entry(i["id"], i["userId"], i["title"], i["body"])
                    db.session.add(temp)
                    db.session.commit()
                message = "Data is Registered Successfully!"
            except:
                message = "Something Went Wrong"
            return render_template("home.html", message = message)
        else:
            message = "Please Input a JSON file"
            return render_template("home.html", message = message)

    return render_template("upload.html", form=form)


@entries.route('/view', methods = ['GET', 'POST'])
@login_required
def view():
    page = request.args.get('page', 1, type=int)
    d = Entry.query.order_by(Entry.id.asc()).paginate(page=page, per_page=10)
    return render_template("view.html", d = d, nil = False)

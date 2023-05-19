from . import app, db

import random
import string

from flask import render_template, redirect, url_for

from app.forms import URLForm
from app.models import URLS

def index():
    form = URLForm()

    if form.validate_on_submit():
        urls_model = URLS()

        urls_model.url = form.url.data
        urls_model.short = get_shortener()

        db.session.add(urls_model)
        db.session.commit()

        return redirect(url_for("urls"))

    return render_template("index.html", form=form)

def get_shortener():
    while True:
        short = "".join(random.choices(string.ascii_letters + string.ascii_letters + string.digits, k=6))

        if URLS.query.filter(URLS.short == short).first():
            continue
        else:
            return short


def urls():
    urls_list = URLS.query.order_by(URLS.date.desc()).all()

    return render_template("urls.html", urls=urls_list)


def url_redirect(short):
    url_object = URLS.query.filter(URLS.short == short).first()

    if url_object:
        url_object.visits += 1

        db.session.add(url_object)
        db.session.commit()

        return redirect(url_object.url)


app.add_url_rule("/", "index", index, methods=["GET", "POST"])
app.add_url_rule("/urls", "urls", urls)
app.add_url_rule("/<string:short>", "url_redirect", url_redirect)
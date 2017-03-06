from flask import Flask, render_template
from forms import ArticleForm
from models import db, Article


app = Flask(__name__)
app.config.from_object('config')
with app.app_context():
    db.init_app(app)


@app.route('/', methods=['GET', 'POST'])
def form():
    form = ArticleForm()
    if form.validate_on_submit():
        header = form.data['header']
        signature = form.data['signature']
        body = form.data['body']
        article = Article(header=header, signature=signature, body=body)
        db.session.add(article)
        db.session.commit()
    return render_template('form.html', form=form)


if __name__ == "__main__":
    app.run()

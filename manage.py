from flaskblog import create_app, db
from flaskblog.models import User, Post
from flask_bcrypt import Bcrypt

app = create_app()
bcrypt = Bcrypt(app)

with app.app_context():
    db.create_all()

    # Add dummy users only if no users exist
    if not User.query.first():
        user1 = User(
            username='john',
            email='john@example.com',
            password=bcrypt.generate_password_hash('password').decode('utf-8'),
            image_file='default.jpg'
        )
        user2 = User(
            username='jane',
            email='jane@example.com',
            password=bcrypt.generate_password_hash('password').decode('utf-8'),
            image_file='default.jpg'
        )
        db.session.add_all([user1, user2])
        db.session.commit()

        # Add dummy posts
        post1 = Post(
            title='Welcome to the Blog',
            content='This is the first post written by John.',
            author=user1
        )
        post2 = Post(
            title='Another Day, Another Post',
            content='Jane shares some thoughts here.',
            author=user2
        )
        db.session.add_all([post1, post2])
        db.session.commit()

        print("Dummy users and posts added.")
    else:
        print("Database already contains data. No dummy data added.")

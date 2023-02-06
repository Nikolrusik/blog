from blog.models.database import db
import click

# DB Commands


@click.command('create-admin')
def create_admin():
    """
    Run in your terminal:
    flask create-admin
    > done! created admin: <User #1 'admin'>
    """
    from blog.models.user import User
    admin = User(username='admin', is_staff=True)

    db.session.add(admin)
    db.session.commit()

    print('done! create admin:', admin)

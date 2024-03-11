from unittest import TestCase

from app import app
from models import db, User, Post, example_data


# Use test database and don't clutter tests with SQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly_test'
app.config['SQLALCHEMY_ECHO'] = False


# Make Flask errors be real errors, rather than HTML pages with error info
app.config['TESTING'] = True

# This is a bit of hack, but don't use Flask DebugToolbar
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

with app.app_context():
    db.drop_all()
    db.create_all()

class BloggyTestCase(TestCase):

    def setUp(self):
        """Stuff to do before every test."""
        
        with app.app_context():
            # User.query.delete()    
            # Post.query.delete()  
            example_data()  

        self.client = app.test_client()
            
    def tearDown(self):
        """Clean up any fouled transaction."""
        with app.app_context():
            db.session.rollback()
        
    def test_user_list(self):
        """Test if John Doe is displayed in user list page
        """
        with self.client:
            response = self.client.get('/users')
            html = response.get_data(as_text=True)
            
            self.assertEqual(response.status_code, 200)
            self.assertIn('John Doe', html)
    
    def test_user_detail(self):
        """Test if John Doe is displayed in user datial page
        """
        with self.client:
            response = self.client.get(f"/users/1")
            html = response.get_data(as_text=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn('<h1>John Doe</h1>', html)   
            
            
    def test_add_user(self):
        """Test if new user is added is to user list page
        """
        with self.client:
            data = {'first_name': 'Juan',
                    'last_name': 'Sanchez',
                    'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/85/Smiley.svg/1200px-Smiley.svg.png'}
            response = self.client.post("/users/new", data=data, follow_redirects=True)
            html = response.get_data(as_text=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn('<li><a href="/users/3">Juan Sanchez</a></li>', html)
                
                
    def test_delete_user(self):
        """Test if John Doe is deleted from user list page
        """
        with self.client:
            response = self.client.post("/users/1/delete", follow_redirects=True)
            html = response.get_data(as_text=True)

            self.assertEqual(response.status_code, 200)
            self.assertNotIn('<li><a href="/users/2">John Doe</a></li>', html)
            
 ################################################################################### Post test                 
    
    def test_post_detail(self):
        """Test if post 1 is displayed in user detail page
        """
        with self.client:
            response = self.client.get(f"/users/1")
            html = response.get_data(as_text=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn('<li><a href="/posts/1">First Post</a></li>', html)   
            
            
    def test_add_post(self):
        """Test if new post is added is to user detail page
        """
        with self.client:
            data = {'title': 'Test Post',
                    'content': 'testing 123',
                    'user_id': 1}
            response = self.client.post("/users/1/posts/new", data=data, follow_redirects=True)
            html = response.get_data(as_text=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn('<li><a href="/posts/5">Test Post</a></li>', html)

    def test_delete_post(self):
        """Test if post 1 is deleted from user list page
        """
        with self.client:
            response = self.client.post("/posts/1/delete", follow_redirects=True)
            html = response.get_data(as_text=True)

            self.assertEqual(response.status_code, 200)
            self.assertNotIn('<li><a href="/posts/1">First Post</a></li>', html)
        
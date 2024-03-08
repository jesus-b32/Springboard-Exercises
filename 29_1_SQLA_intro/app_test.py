from unittest import TestCase
from app import app
from flask import session
from models import db, connect_db, User
import json


class FlaskTests(TestCase):

    def setUp(self):
        """Stuff to do before every test."""
        
        app.config['TESTING'] = True
        self.client = app.test_client()
            
    def test_user_list(self):
        """Esnure that variables are stored in sessions and HTML template is displayed
        """
        
        with self.client:
            response = self.client.get('/users')
            html = response.get_data(as_text=True)
            
            self.assertEqual(response.status_code, 200)
            # self.assertIsNone(session.get('highest_score'))
            # self.assertIsNone(session.get('number_of_games'))
            self.assertIn('<h1>Users</h1>', html)
            
    # def test_check_word(self):
    #     """check if word is valid by manually modifying the board
    #     """
        
    #     with self.client.session_transaction() as s:
    #         s['game_board'] = [["G", "O", "O", "D", "D"], 
    #                             ["G", "O", "O", "D", "D"], 
    #                             ["G", "O", "O", "D", "D"], 
    #                             ["G", "O", "O", "D", "D"], 
    #                             ["G", "O", "O", "D", "D"]]
            
        
    #     response = self.client.get('/check_word?word=good')
    #     self.assertEqual(response.json['result'], 'ok')
        
    
    # def test_invalid_word(self):
    #     """Test if word is invalid, not found on board"""

    #     self.client.get('/')
    #     response = self.client.get('/check_word?word=python')
    #     self.assertEqual(response.json['result'], 'not-on-board')

    # def test_not_a_word(self):
    #     """Test if word is an actual word"""

    #     self.client.get('/')
    #     response = self.client.get(
    #         '/check_word?word=oksdkfsdfksdofkosdfosdfkosdfkosdkfosdf')
    #     self.assertEqual(response.json['result'], 'not-word')
        
from project import app
import unittest


class FlaskTestCase(unittest.TestCase):

    # Ensure that flask was set up correctly 
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type = 'html/text')
        self.assertEqual(response.status_code, 200)

    # Ensure that the login page loads correctly
    def test_login_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type = 'html/text')
        self.assertTrue(b'Please login' in response.data)

    # Test that the login page loads
    def test_login_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type = 'html/text')
        self.assertTrue(b'Please login' in response.data)

   # Ensure login behaves correctly given the correct creditionals
    def test_correct_login(self):
        tester = app.test_client(self)
        response = tester.post('/login', data = dict(username='admin', password='admin'), follow_redirects = True)
        self.assertIn(b'You were just logged in!', response.data)

    # Ensure login behaves correctly given the incorrect creditionals
    def test_incorrect_login(self):
        tester = app.test_client(self)
        response = tester.post('/login', data = dict(username='admin1', password='admin'), follow_redirects = True)
        self.assertIn(b'Invalid credentials. Please try again.', response.data)

    # Ensure logout behaves correctly
    def test_correct_logout(self):
        tester = app.test_client(self)
        response = tester.post('/login', data = dict(username='admin', password='admin'), follow_redirects = True)
        response = tester.get('/logout', follow_redirects = True)
        self.assertIn(b'You were just logged out', response.data)

    # Ensure that the main page requires login 
    def test_root_login(self):
        tester = app.test_client(self)
        response = tester.get('/', follow_redirects = True)
        self.assertIn(b'You need to login first.', response.data)

    # Ensure that the main page requires login 
    def test_logout_login(self):
        tester = app.test_client(self)
        response = tester.get('/logout', follow_redirects = True)
        self.assertIn(b'You need to login first.', response.data)

    # Ensure posts show up on the main page 
    def test_post_show_up(self):
        tester = app.test_client(self)
        response = tester.post('/login', data = dict(username='admin', password='admin'), follow_redirects = True)
        self.assertIn(b"Well", response.data)






if __name__ == '__main__':
    unittest.main()

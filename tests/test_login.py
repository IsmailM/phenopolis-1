
import unittest
import runserver


class LoginTestCase(unittest.TestCase):

    def setUp(self):
        runserver.app.config['TESTING'] = True
        self.app = runserver.app.test_client()

    def tearDown(self):
        pass

    # Smoke test to check that unittest is running ok.
    def test_smoke_test(self):
       pass 

    def login(self, username, password):
        return self.app.post('/login', data=dict(
            username=username,
            password=password
        ), follow_redirects=True)

    def logout(self):
        return self.app.get('/logout', follow_redirects=True)

    def test_login_logout(self):
        rv = self.login('demox', 'demo123')
        assert 'Invalid Credentials. Please try again.' in rv.data
        rv = self.login('demo', 'demo123x')
        assert 'Invalid Credentials. Please try again.' in rv.data
        rv = self.login('demo', 'demo123')
        assert 'Search Page' and 'HPO Browser' in rv.data
        rv = self.logout()
        assert 'Please login' and 'username' and 'password' in rv.data

if __name__ == '__main__':
    unittest.main()
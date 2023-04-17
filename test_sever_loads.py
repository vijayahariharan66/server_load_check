import unittest
from urllib import request, error

class TestWebsiteConnection(unittest.TestCase):

    def test_website_loads(self):
        url = "https://www.atg.world"
       # url="jenkins.domainname.com"
        print(f"Connecting to {url}...")
        try:
            response = request.urlopen(url)
        except error.URLError as e:
            print(f"Error connecting to {url}: {e}")
            self.fail(f"Error connecting to {url}: {e}")
        else:
            print(f"Connected to {url} successfully!")
            self.assertEqual(response.status, 200, f"Error: HTTP status code is {response.status}")

if __name__ == '__main__':
    unittest.main()

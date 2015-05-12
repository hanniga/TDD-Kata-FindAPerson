import unittest
from Crowdmap import Crowdmap

class FindAPersonTests(unittest.TestCase):
    def setUp(self):
        self.crowdmap = Crowdmap()

    def test_getAllPostsForName(self):
        posts = self.crowdmap.get_all_posts_for("Or")
        self.assertIn("Or", posts)

    def test_getAllPostsForMissingName(self):
        posts = self.crowdmap.get_all_posts_for("Or2")
        self.assertNotIn("Or2", posts)


if __name__ == '__main__':
    unittest.main()

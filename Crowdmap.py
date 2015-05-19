class Crowdmap(object):
    def __init__(self, init_list):
      self.list = init_list
      self.location_service = LocationService()
      
    def get_all_posts_for(self, name):
        return [post for post in self.list if post.find(name) != -1]

    def is_location_for_name(self, name):
        name_posts = self.get_all_posts_for(name)
        for post in name_posts:
            if self.location_service.find(post):
                return True;
        return False

class LocationService:
    def find(self, text):
        return (text.find("Bangkok") != -1)

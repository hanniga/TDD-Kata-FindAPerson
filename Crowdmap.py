class Crowdmap(object):
    def __init__(self, init_list):
      self.list = init_list
      
    def get_all_posts_for(self, param):
        return [post for post in self.list if post.find(param) != -1]

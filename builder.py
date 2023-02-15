import json
import urllib.parse


class Builder(object):

    def __init__(self):
        self.params = dict()
        self.posts = dict()

    def put_url(self, name, value):
        if value is not None:
            if isinstance(value, list):
                self.params[name] = json.dumps(value)
            elif isinstance(value, float):
                self.params[name] = ('%.20f' % (value))[slice(0, 16)].rstrip('0').rstrip('.')
            else:
                self.params[name] = str(value)
    def put_post(self, name, value):
        if value is not None:
            if isinstance(value, list):
                self.posts[name] = value
            else:
                self.posts[name] = str(value)

    def build_url(self):
        if len(self.params) == 0:
            return ""
        encoded_param = urllib.parse.urlencode(self.params)
        return encoded_param

    def build_url_to_json(self):
        return json.dumps(self.params)
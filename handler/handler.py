import tornado.web

class Handler(tornado.web.RequestHandler):

    def get(self):
        name = self.get_argument("name")
        self.write(name)

    def post(self):
        data = tornado.escape.json_decode(self.request.body)
        self.write(data["name"])
        
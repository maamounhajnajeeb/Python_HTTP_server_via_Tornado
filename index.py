import tornado.web
import tornado.ioloop


class BasicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world!")


class BasicStaticHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


class QueryStringRequestHandler(tornado.web.RequestHandler):
    def get(self):
        num = int(self.get_argument("num"))
        result = "odd" if num % 2 else "even"

        self.write(f"the number {num} is {result}")


class ResourceRequestHandler(tornado.web.RequestHandler):
    def get(self, id):
        self.write(f"Querying twee with id: {id}")


if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", BasicRequestHandler),
        (r"/static", BasicStaticHandler),
        (r"/is_even", QueryStringRequestHandler),
        (r"/tweet/([0-9]+)", ResourceRequestHandler)
    ])

    app.listen(port=8080)
    print("Your tornado app is listening on port 8080")
    
    tornado.ioloop.IOLoop.current().start()

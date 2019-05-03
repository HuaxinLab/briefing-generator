#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os.path
from pymongo import MongoClient

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
define("port", default=80, help="run on the given port", type=int)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

class ResultHandler(tornado.web.RequestHandler):
    def fetch_data(self, post_type, post_date):
        client = MongoClient()
        database = client['BgSpider']
        collection = database[post_type+'_items']
        postList = collection.find(
            {'post_date':post_date}, 
            {'_id': 0, 'post_abstract': 1, 'post_title': 1, 'post_url': 1}
        )
        client.close()
        return postList

    def post(self):
        headline = self.get_argument('headline')
        post_type = self.get_argument('post_type')
        post_date = self.get_argument('post_date')
        postList = self.fetch_data(post_type, post_date)
        self.render('result.html', headline=headline, post_date=post_date, 
            post_type=post_type, postList=postList)

if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[(r'/', IndexHandler), (r'/result', ResultHandler)],
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        debug=True
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from google.appengine.api import users
import webapp2
import jinja2
import os
import random
TEMPLATE = jinja2.Environment(
	loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
	extensions = ['jinja2.ext.autoescape'],
	autoescape = True
)

USERNAME = 'Tarik'
PASSWORD = 'password'

class Login(webapp2.RequestHandler):
    def get(self):
        error = self.request.get('error')
        content = TEMPLATE.get_template('Templates/login.html')
       
        self.response.write(content.render(error=error))
    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')
        if username == USERNAME and password == PASSWORD:
           print 'valid login'
           self.redirect('/')
        else:
            print 'incorrect login'
            self.redirect('/login?error=true')
            
        

class MainPage(webapp2.RequestHandler):
    def get(self):
    
    
        content = TEMPLATE.get_template('Templates/index.html')
 
        self.response.write(content.render())


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/login',Login)
], debug=True)

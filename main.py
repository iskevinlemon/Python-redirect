from flask import Flask, Response

app = Flask('app', static_url_path='')

url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
myport = 80

@app.route('/')
def hello_world():
  response = Response()
  response.headers['Refresh'] = '1; url=%s' % url
  return response

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=myport, debug=True)
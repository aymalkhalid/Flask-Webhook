from flask import Flask, request, Response,abort

app = Flask(__name__)

@app.route('/')
@app.route('/webhook', methods=['POST'])
def webhook():
    print(request.json);
    return Response.json(status=200,info='OK')


@app.route('/index')
def index():
    return "Hello, World!"
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
# webhook-app-305615 
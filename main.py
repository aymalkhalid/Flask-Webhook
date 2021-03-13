from flask import Flask, request, abort,json,make_response,jsonify

app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    parts = None
    if request.method == 'POST':
        request_data=request.get_json()
        print(request.json)
        d = {'status':'200','info':'OK'}
        json_str = json.dumps(request_data)
        resp = json.loads(json_str)
        resp=resp['data']
        return make_response(jsonify(d),200)
    else:
        abort(400)
    
@app.route('/')
@app.route('/index')
def index():
        return '''
<html>
    <head>
        <title>Hospital Chatbot</title>
    </head>
    <body>
        <h1>Hello, Testing Web Integration of Chatbot!</h1>
            <script>
        window.watsonAssistantChatOptions = {
            integrationID: "45a8c0ba-2bf2-425e-b3c6-b98035b6f6d5", // The ID of this integration.
            region: "us-south", // The region your integration is hosted in.
            serviceInstanceID: "3387fc01-4a6b-4264-ad97-15ad096fb477", // The ID of your service instance.
            onLoad: function(instance) {
                instance.render();
            }
        };
        setTimeout(function() {
            const t = document.createElement('script');
            t.src = "https://web-chat.global.assistant.watson.appdomain.cloud/loadWatsonAssistantChat.js";
            document.head.appendChild(t);
        });
    </script>
    </body>
</html>'''

@app.route('/Appointment', methods=['POST'])
def webhook():
    parts = None
    if request.method == 'POST':
        request_data=request.get_json()
        print(request.json)
        d = {'status':'200','info':'OK'}
        json_str = json.dumps(request_data)
        resp = json.loads(json_str)
        return make_response(jsonify(d),200)
    else:
        abort(400)

if __name__ == '__main__':
    app.run()
#lask-web-app-305810
    
#curl --location --request POST 'https://flask-web-app-305810.df.r.appspot.com/webhook' \
#--header 'Content-Type: application/json' \
#--data-raw '{​​​​​
#"uri" : "https://flask-web-app-305810.df.r.appspot.com/webhook"
#}​​​​​'
from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)

# Replace with the actual URL of your LLM API
API_URL = "https://deepseek-r1-distill-qwen-14b-maas-apicast-production.apps.prod.rhoai.rh-aiservices-bu.com:443"
API_KEY = "ce6feae9b4ceec3229d9482ee2a224b8"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form.get("user_input")
        
        # Send the user input to the LLM API
        response = requests.post(
            url=API_URL+'/v1/completions',
                json={
                "model": "deepseek-r1-distill-qwen-14b",
                "prompt": user_input,
                "max_tokens": 300,
                "temperature": 0
                },
                headers={'Authorization': 'Bearer '+API_KEY}
            ).json()

        # return render_template("index.html", user_input=None, llm_response=None)
        comp_list = response['choices']
        comp_dict = comp_list[0]
        return render_template("index.html", user_input=user_input, llm_response=comp_dict['text'])

    return render_template("index.html", user_input=None, llm_response=None)
        
"""         if response.status_code == 200:
            llm_response = response.json().get("response", "No response from LLM.")
        else:
            llm_response = "Error: Unable to get a response from the LLM." 
        
        return render_template("index.html", user_input=user_input, llm_response=llm_response) """

if __name__ == "__main__":
    app.run(debug=True)

# run this chatbot:
# > source .venv/bin/activate
# > python ask-llm.py 
from flask import Flask
import datetime

app = Flask(__name__)

@app.route('/')
def get_current_time():
    current_time = datetime.datetime.now().strftime("%m/%d/%Y  %H:%M:%S")

    return f"Current Time: {current_time}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
#Finshed
from datetime import datetime
from flask import Flask, request 
import pytz


app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'



#/convert_epoch?epoch_time=<epoch time>
@app.route('/convert_epoch', methods=['GET'])
def convert_epoch_to_datetime():
    epoch_time = request.args.get('epoch_time')
    if epoch_time is None:
        return '<h1>Error: Epoch time parameter is required.</h1>', 400

    try:
        epoch_time = float(epoch_time)
        if epoch_time < 0:
            raise ValueError("Epoch time cannot be negative.")
    except ValueError as e:
        return f'<h1>Error: {str(e)}</h1>', 400
    result = epoch_to_datetime(epoch_time)
    html_result = f'''
    <html>
    <head>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f2f2f2;
            }}
            .container {{
                margin: 50px auto;
                padding: 20px;
                background-color: #fff;
                border-radius: 5px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                width: 400px;
            }}
            h1 {{
                color: #333;
            }}
            p {{
                color: #666;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Converted Datetime:</h1>
            <p>{result}</p>
        </div>
    </body>
    </html>
    '''

    return html_result


def epoch_to_datetime(epoch_time):
    try:
        # Convert epoch time to utc
        utc_time = datetime.utcfromtimestamp(epoch_time).replace(tzinfo=pytz.utc)
        print("utc_time", utc_time)
        return utc_time.strftime('%Y-%m-%d %H:%M:%S')
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)

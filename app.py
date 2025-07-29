from flask import Flask, render_template, request
import joblib

app = Flask(__name__)


model = joblib.load('model.pkl')
interest_map = joblib.load('interest_map.pkl')
interest_map_rev = {v: k for k, v in interest_map.items()}

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        try:
            hours_studied = int(request.form['Hours_Studied'])
            attendance = int(request.form['Attendance'])

            
            pred_num = model.predict([[hours_studied, attendance]])[0]
            prediction = interest_map_rev.get(pred_num, "Unknown")
        except Exception as e:
            prediction = f"Error: {e}"

    return render_template('index.html', prediction=prediction)

if _name_ == '_main_':
    port = int(os.environ.get("PORT", 10000))  # Render sets the PORT variable
    app.run(host='0.0.0.0', port=port)
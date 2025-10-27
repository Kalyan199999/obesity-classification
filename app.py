from flask import Flask, request, jsonify,render_template
import pickle
import pandas as pd

app = Flask(__name__)

model = pickle.load(open('./models/svc.pkl', 'rb'))
preprocessor = pickle.load(open('./models/preprocessor.pkl', 'rb'))

@app.route('/')
def index():
    return render_template( 'index.html' )

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    df = pd.DataFrame([data])

    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].str.lower().str.strip()
            
    X = preprocessor.transform(df)

    pred = model.predict(X)
    return jsonify({'prediction': pred[0]})

if __name__ == '__main__':
    app.run(debug=True)

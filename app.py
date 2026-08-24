from flask import Flask, render_template_string, request
import pickle
import pandas as pd
import os

app = Flask(__name__)

# ---------------------------------------------------------
# LOAD MODEL
# ---------------------------------------------------------
MODEL_PATH = "xgboost.pkl"

with open(MODEL_PATH, "rb") as file:
    model = pickle.load(file)


# ---------------------------------------------------------
# HTML TEMPLATE
# ---------------------------------------------------------
HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Health Cost Prediction AI</title>

    <style>

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: Arial, Helvetica, sans-serif;
            min-height: 100vh;
            background:
                radial-gradient(circle at 10% 10%, rgba(99,102,241,0.18), transparent 30%),
                radial-gradient(circle at 90% 20%, rgba(14,165,233,0.18), transparent 30%),
                linear-gradient(135deg, #f8fafc, #eef2ff, #f0f9ff);
            color: #1e293b;
        }

        .container {
            width: 92%;
            max-width: 1050px;
            margin: auto;
            padding: 35px 0;
        }

        /* HERO */

        .hero {
            background: linear-gradient(
                135deg,
                #312e81,
                #4f46e5,
                #0284c7
            );

            padding: 45px;
            border-radius: 28px;
            color: white;
            box-shadow: 0 20px 50px rgba(49,46,129,0.25);
            margin-bottom: 30px;
        }

        .hero h1 {
            font-size: 42px;
            font-weight: 800;
            margin-bottom: 12px;
        }

        .hero p {
            font-size: 17px;
            opacity: 0.9;
        }

        /* CARD */

        .card {
            background: rgba(255,255,255,0.92);
            padding: 30px;
            border-radius: 24px;
            box-shadow: 0 12px 35px rgba(15,23,42,0.08);
            margin-bottom: 25px;
        }

        .card h2 {
            font-size: 23px;
            margin-bottom: 7px;
            color: #1e293b;
        }

        .subtitle {
            color: #64748b;
            margin-bottom: 25px;
            font-size: 14px;
        }

        /* FORM */

        .form-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 22px;
        }

        .form-group {
            display: flex;
            flex-direction: column;
        }

        label {
            font-size: 14px;
            font-weight: 700;
            margin-bottom: 8px;
            color: #334155;
        }

        input,
        select {
            width: 100%;
            padding: 14px 15px;
            border: 1px solid #cbd5e1;
            border-radius: 12px;
            font-size: 15px;
            background: white;
            outline: none;
            transition: 0.25s;
        }

        input:focus,
        select:focus {
            border-color: #4f46e5;
            box-shadow: 0 0 0 3px rgba(79,70,229,0.12);
        }

        /* BUTTON */

        .button-container {
            margin-top: 30px;
            text-align: center;
        }

        button {
            width: 100%;
            max-width: 420px;
            padding: 16px 25px;
            border: none;
            border-radius: 14px;
            background: linear-gradient(135deg, #4f46e5, #0284c7);
            color: white;
            font-size: 17px;
            font-weight: 700;
            cursor: pointer;
            box-shadow: 0 10px 25px rgba(79,70,229,0.25);
            transition: 0.25s;
        }

        button:hover {
            transform: translateY(-2px);
            box-shadow: 0 15px 30px rgba(79,70,229,0.35);
        }

        /* RESULT */

        .result {
            text-align: center;
            background: linear-gradient(
                135deg,
                #ffffff,
                #f8fafc
            );
            border: 1px solid #e2e8f0;
            padding: 35px;
            border-radius: 24px;
            box-shadow: 0 15px 40px rgba(15,23,42,0.10);
        }

        .result-icon {
            font-size: 50px;
            margin-bottom: 10px;
        }

        .result-title {
            color: #64748b;
            font-size: 17px;
            font-weight: 600;
        }

        .result-value {
            color: #4f46e5;
            font-size: 42px;
            font-weight: 800;
            margin: 10px 0;
        }

        .result-message {
            color: #64748b;
            font-size: 14px;
        }

        /* ERROR */

        .error {
            background: #fef2f2;
            color: #b91c1c;
            padding: 16px;
            border-radius: 12px;
            margin-bottom: 20px;
            text-align: center;
            font-weight: 600;
        }

        /* FOOTER */

        footer {
            text-align: center;
            padding: 25px;
            color: #64748b;
            font-size: 13px;
        }

        /* RESPONSIVE */

        @media (max-width: 700px) {

            .container {
                width: 94%;
                padding: 20px 0;
            }

            .hero {
                padding: 30px 25px;
            }

            .hero h1 {
                font-size: 30px;
            }

            .form-grid {
                grid-template-columns: 1fr;
            }

            .card {
                padding: 22px;
            }

            .result-value {
                font-size: 32px;
            }
        }

    </style>
</head>

<body>

<div class="container">

    <div class="hero">
        <h1>🩺 Health Cost Prediction AI</h1>
        <p>
            Predict healthcare insurance costs using an XGBoost
            Machine Learning model.
        </p>
    </div>


    <div class="card">

        <h2>👤 Patient Information</h2>

        <p class="subtitle">
            Enter the patient's details to generate an estimated healthcare cost.
        </p>


        {% if error %}
            <div class="error">
                ⚠️ {{ error }}
            </div>
        {% endif %}


        <form method="POST">

            <div class="form-grid">

                <div class="form-group">
                    <label>Age</label>
                    <input
                        type="number"
                        name="age"
                        min="1"
                        max="120"
                        placeholder="Enter age"
                        required
                    >
                </div>


                <div class="form-group">
                    <label>Sex</label>

                    <select name="sex" required>
                        <option value="">Select sex</option>
                        <option value="0">Female</option>
                        <option value="1">Male</option>
                    </select>
                </div>


                <div class="form-group">
                    <label>BMI</label>

                    <input
                        type="number"
                        name="bmi"
                        min="10"
                        max="60"
                        step="0.1"
                        placeholder="Example: 25.5"
                        required
                    >
                </div>


                <div class="form-group">
                    <label>Number of Children</label>

                    <input
                        type="number"
                        name="children"
                        min="0"
                        max="20"
                        placeholder="Enter number"
                        required
                    >
                </div>


                <div class="form-group">
                    <label>Smoking Status</label>

                    <select name="smoker" required>
                        <option value="">Select status</option>
                        <option value="0">No</option>
                        <option value="1">Yes</option>
                    </select>
                </div>


                <div class="form-group">
                    <label>Region</label>

                    <select name="region" required>

                        <option value="">Select region</option>

                        <option value="0">
                            Southwest
                        </option>

                        <option value="1">
                            Southeast
                        </option>

                        <option value="2">
                            Northwest
                        </option>

                        <option value="3">
                            Northeast
                        </option>

                    </select>

                </div>

            </div>


            <div class="button-container">

                <button type="submit">
                    🔮 Generate Prediction
                </button>

            </div>

        </form>

    </div>


    {% if prediction is not none %}

    <div class="result">

        <div class="result-icon">
            🎯
        </div>

        <div class="result-title">
            Predicted Healthcare Cost
        </div>

        <div class="result-value">
            ₹ {{ "{:,.2f}".format(prediction) }}
        </div>

        <div class="result-message">
            Prediction generated using the trained XGBoost model.
        </div>

    </div>

    {% endif %}


    <footer>
        <strong>Health Cost Prediction AI</strong>
        <br>
        Powered by XGBoost • Flask • Machine Learning
    </footer>

</div>

</body>
</html>
"""


# ---------------------------------------------------------
# ROUTE
# ---------------------------------------------------------

@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None
    error = None

    if request.method == "POST":

        try:

            age = float(request.form["age"])
            sex = float(request.form["sex"])
            bmi = float(request.form["bmi"])
            children = float(request.form["children"])
            smoker = float(request.form["smoker"])
            region = float(request.form["region"])


            # Create dataframe using the exact
            # feature names expected by the model

            input_data = pd.DataFrame(
                [[
                    age,
                    sex,
                    bmi,
                    children,
                    smoker,
                    region
                ]],
                columns=[
                    "Age",
                    "Sex",
                    "BMI",
                    "Children",
                    "Smoker",
                    "Region"
                ]
            )


            # Prediction

            prediction = float(
                model.predict(input_data)[0]
            )


        except Exception as e:

            error = f"Prediction failed: {str(e)}"


    return render_template_string(
        HTML,
        prediction=prediction,
        error=error
    )


# ---------------------------------------------------------
# RUN APP
# ---------------------------------------------------------

if __name__ == "__main__":

    port = int(os.environ.get("PORT", 5000))

    app.run(
        host="0.0.0.0",
        port=port,
        debug=False
    )

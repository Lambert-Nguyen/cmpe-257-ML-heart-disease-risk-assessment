"""
Web Application Prediction Pipeline
=====================================

This script shows exactly how to process user inputs
and make predictions in the web application.

"""

import pickle
import numpy as np
import pandas as pd

# ============================================================================
# STEP 1: LOAD SAVED PREPROCESSING ARTIFACTS
# ============================================================================

def load_preprocessing_artifacts():
    """
    Load the scaler, encodings, and feature names saved during preprocessing.
    These files are in: data/processed/
    """
    with open('data/processed/scaler.pkl', 'rb') as f:
        scaler = pickle.load(f)
    
    with open('data/processed/encodings.pkl', 'rb') as f:
        encodings = pickle.load(f)
    
    with open('data/processed/feature_names.pkl', 'rb') as f:
        feature_names = pickle.load(f)
    
    return scaler, encodings, feature_names


# ============================================================================
# STEP 2: PROCESS USER INPUT
# ============================================================================

def process_user_input(user_data, encodings, scaler, feature_names):
    """
    Convert raw user input into scaled features ready for model prediction.
    
    Parameters:
    -----------
    user_data : dict
        Dictionary containing user inputs with keys matching form field names
        Example: {'age': 63, 'sex': 'Male', 'cp': 'typical angina', ...}
    
    encodings : dict
        Dictionary of encoding mappings loaded from encodings.pkl
    
    scaler : StandardScaler
        Fitted scaler loaded from scaler.pkl
    
    feature_names : list
        List of feature names in correct order
    
    Returns:
    --------
    numpy.ndarray
        Scaled feature array ready for model.predict()
    """
    
    # Step 2.1: Encode categorical variables
    encoded_data = {
        # Numerical features - use as-is
        'age': user_data['age'],
        'trestbps': user_data['trestbps'],
        'chol': user_data['chol'],
        'thalch': user_data['thalch'],
        'oldpeak': user_data['oldpeak'],
        'ca': user_data['ca'],
        
        # Categorical features - encode using mappings
        'sex_encoded': encodings['sex'][user_data['sex']],
        'fbs_encoded': encodings['fbs'][user_data['fbs']],
        'exang_encoded': encodings['exang'][user_data['exang']],
        'cp_encoded': encodings['cp'][user_data['cp']],
        'restecg_encoded': encodings['restecg'][user_data['restecg']],
        'slope_encoded': encodings['slope'][user_data['slope']],
        'thal_encoded': encodings['thal'][user_data['thal']]
    }
    
    # Step 2.2: Create feature array in correct order
    feature_array = np.array([[encoded_data[feat] for feat in feature_names]])
    
    # Step 2.3: Apply scaling
    scaled_features = scaler.transform(feature_array)
    
    return scaled_features


# ============================================================================
# STEP 3: MAKE PREDICTION
# ============================================================================

def predict_heart_disease(model, user_data, scaler, encodings, feature_names):
    """
    Complete pipeline: process input and make prediction.
    
    Parameters:
    -----------
    model : trained model
        Your trained Random Forest, XGBoost, or SVM model
    
    user_data : dict
        Raw user input from web form
    
    scaler, encodings, feature_names : preprocessing artifacts
    
    Returns:
    --------
    dict
        Prediction results with severity level and interpretation
    """
    
    # Process the input
    scaled_features = process_user_input(user_data, encodings, scaler, feature_names)
    
    # Make prediction
    severity_level = model.predict(scaled_features)[0]
    
    # Get probability distribution if model supports it
    if hasattr(model, 'predict_proba'):
        probabilities = model.predict_proba(scaled_features)[0]
    else:
        probabilities = None
    
    # Interpret results
    severity_descriptions = {
        0: "No significant heart disease (less than 50% artery blockage)",
        1: "Mild heart disease",
        2: "Moderate heart disease", 
        3: "Severe heart disease",
        4: "Very severe heart disease"
    }
    
    recommendations = {
        0: "Continue healthy lifestyle and regular checkups.",
        1: "Consult with a cardiologist. Lifestyle changes recommended.",
        2: "Seek medical attention. Treatment may be required.",
        3: "Seek immediate medical attention. Treatment likely required.",
        4: "Seek emergency medical attention immediately."
    }
    
    result = {
        'severity_level': int(severity_level),
        'description': severity_descriptions[severity_level],
        'recommendation': recommendations[severity_level],
        'probabilities': probabilities
    }
    
    return result


# ============================================================================
# EXAMPLE USAGE
# ============================================================================

def example_usage():
    """
    Example showing how to use the prediction pipeline in a web app.
    """
    
    print("="*80)
    print("           WEB APP PREDICTION EXAMPLE")
    print("="*80)
    
    # Step 1: Load preprocessing artifacts (do this once when app starts)
    print("\n1. Loading preprocessing artifacts...")
    scaler, encodings, feature_names = load_preprocessing_artifacts()
    print("   Scaler loaded")
    print("   Encodings loaded")
    print("   Feature names loaded")
    
    # Step 2: Simulate user input from web form
    print("\n2. User fills out form...")
    user_data = {
        'age': 63,
        'sex': 'Male',  # Options: 'Male', 'Female'
        'cp': 'typical angina',  # Options: 'typical angina', 'atypical angina', 'non-anginal', 'asymptomatic'
        'trestbps': 145,
        'chol': 233,
        'fbs': True,  # Options: True, False
        'restecg': 'lv hypertrophy',  # Options: 'normal', 'st-t abnormality', 'lv hypertrophy'
        'thalch': 150,
        'exang': False,  # Options: True, False
        'oldpeak': 2.3,
        'slope': 'downsloping',  # Options: 'upsloping', 'flat', 'downsloping'
        'ca': 0,  # Range: 0-3
        'thal': 'fixed defect'  # Options: 'normal', 'fixed defect', 'reversable defect'
    }
    
    print("   User inputs:")
    for key, value in user_data.items():
        print(f"      {key}: {value}")
    
    # Step 3: Process input
    print("\n3. Processing input...")
    scaled_features = process_user_input(user_data, encodings, scaler, feature_names)
    print(f"   Input processed and scaled")
    print(f"   Scaled features shape: {scaled_features.shape}")
    print(f"   First 3 features: {scaled_features[0][:3]}")
    
    # Step 4: Make prediction (you'll need to load your trained model)
    print("\n4. Making prediction...")
    print("   Note: You need to load your trained model here")
    print("   Example:")
    print("      import joblib")
    print("      model = joblib.load('models/best_model.pkl')")
    print("      result = predict_heart_disease(model, user_data, scaler, encodings, feature_names)")
    
    # Simulated result
    print("\n5. Example prediction result:")
    result = {
        'severity_level': 0,
        'description': "No significant heart disease (less than 50% artery blockage)",
        'recommendation': "Continue healthy lifestyle and regular checkups.",
        'probabilities': [0.75, 0.15, 0.05, 0.03, 0.02]
    }
    
    print(f"\n   Severity Level: {result['severity_level']}")
    print(f"   Description: {result['description']}")
    print(f"   Recommendation: {result['recommendation']}")
    if result['probabilities'] is not None:
        print(f"\n   Probability distribution:")
        for i, prob in enumerate(result['probabilities']):
            print(f"      Severity {i}: {prob*100:.1f}%")
    
    print("\n" + "="*80)


# ============================================================================
# FLASK WEB APP EXAMPLE
# ============================================================================

def flask_app_example():
    """
    Example Flask route for making predictions.
    """
    
    example_code = '''
from flask import Flask, request, jsonify, render_template
import pickle
import joblib
import numpy as np

app = Flask(__name__)

# Load artifacts once when app starts
scaler, encodings, feature_names = load_preprocessing_artifacts()
model = joblib.load('models/best_model.pkl')

@app.route('/')
def home():
    """Render the input form"""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """Handle prediction request"""
    try:
        # Get user input from form
        user_data = {
            'age': int(request.form['age']),
            'sex': request.form['sex'],
            'cp': request.form['cp'],
            'trestbps': float(request.form['trestbps']),
            'chol': float(request.form['chol']),
            'fbs': request.form['fbs'] == 'True',
            'restecg': request.form['restecg'],
            'thalch': float(request.form['thalch']),
            'exang': request.form['exang'] == 'True',
            'oldpeak': float(request.form['oldpeak']),
            'slope': request.form['slope'],
            'ca': float(request.form['ca']),
            'thal': request.form['thal']
        }
        
        # Make prediction
        result = predict_heart_disease(
            model, user_data, scaler, encodings, feature_names
        )
        
        # Return result
        return render_template('result.html', result=result)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
'''
    
    return example_code


# ============================================================================
# FORM FIELD OPTIONS FOR WEB APP
# ============================================================================

def get_form_field_options():
    """
    Returns the valid options for each dropdown/select field in the web form.
    Le Duy Vu should use these exact values in the HTML form.
    """
    
    options = {
        'sex': ['Male', 'Female'],
        
        'cp': [
            'typical angina',
            'atypical angina', 
            'non-anginal',
            'asymptomatic'
        ],
        
        'fbs': [True, False],  # Display as "Yes" / "No" in form
        
        'restecg': [
            'normal',
            'st-t abnormality',
            'lv hypertrophy'
        ],
        
        'exang': [True, False],  # Display as "Yes" / "No" in form
        
        'slope': [
            'upsloping',
            'flat',
            'downsloping'
        ],
        
        'thal': [
            'normal',
            'fixed defect',
            'reversable defect'
        ]
    }
    
    return options


# ============================================================================
# INPUT VALIDATION
# ============================================================================

def validate_user_input(user_data, encodings):
    """
    Validate user input to ensure all values are within acceptable ranges.
    
    Returns:
    --------
    tuple: (is_valid, error_message)
    """
    
    errors = []
    
    # Validate numerical ranges
    if not (20 <= user_data['age'] <= 100):
        errors.append("Age must be between 20 and 100")
    
    if not (80 <= user_data['trestbps'] <= 220):
        errors.append("Blood pressure must be between 80 and 220")
    
    if not (100 <= user_data['chol'] <= 700):
        errors.append("Cholesterol must be between 100 and 700")
    
    if not (60 <= user_data['thalch'] <= 220):
        errors.append("Max heart rate must be between 60 and 220")
    
    if not (-5 <= user_data['oldpeak'] <= 10):
        errors.append("ST depression must be between -5 and 10")
    
    if not (0 <= user_data['ca'] <= 3):
        errors.append("Number of vessels must be between 0 and 3")
    
    # Validate categorical values
    for field in ['sex', 'cp', 'restecg', 'slope', 'thal']:
        if user_data[field] not in encodings[field]:
            errors.append(f"Invalid value for {field}: {user_data[field]}")
    
    # Validate boolean values
    if not isinstance(user_data['fbs'], bool):
        errors.append("Fasting blood sugar must be True or False")
    
    if not isinstance(user_data['exang'], bool):
        errors.append("Exercise induced angina must be True or False")
    
    if errors:
        return False, "; ".join(errors)
    
    return True, None


# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    print("\n" + "="*80)
    print("  HEART DISEASE PREDICTION - WEB APP INTEGRATION GUIDE")
    print("="*80)
    
    print("\nThis script shows Le Duy Vu how to:")
    print("   1. Load preprocessing artifacts (scaler, encodings)")
    print("   2. Process user input from web forms")
    print("   3. Make predictions with the trained model")
    print("   4. Display results to users")
    
    print("\n" + "="*80)
    
    # Run example
    try:
        example_usage()
    except FileNotFoundError:
        print("\nNote: Preprocessing artifacts not found.")
        print("   This is expected if running outside the project directory.")
        print("   The code structure is correct for use in the web app.")
    
    print("\nFor Flask integration, see the flask_app_example() function")
    print("   in this script for a complete working example.")
    
    print("\nIntegration complete! Ready for web app development.")
    print("="*80 + "\n")

# Enhanced API Response Format
## Frontend-Optimized Output for Web Application

This document defines an enhanced API response format that's optimized for frontend display, including UI elements like colors, icons, and user-friendly text.

---

## Enhanced Prediction Response

### Standard API Response
```json
{
  "success": true,
  "data": {
    "prediction": {
      "severity_level": 2,
      "severity_label": "Moderate Heart Disease",
      "risk_category": "High Risk",
      "confidence": 0.7234
    },
    "display": {
      "title": "Moderate Risk Detected",
      "message": "Our assessment indicates a moderate level of heart disease risk based on your information.",
      "severity_color": "#FF6B35",
      "severity_icon": "warning",
      "confidence_display": "72% confident",
      "confidence_bar": 72
    },
    "recommendation": {
      "primary": "Medical attention needed. Schedule appointment with cardiologist for evaluation.",
      "action_items": [
        "Schedule a cardiology consultation within the next 2-4 weeks",
        "Bring this assessment report to your appointment",
        "Continue any current medications as prescribed",
        "Monitor symptoms and seek immediate care if they worsen"
      ],
      "urgency": "medium",
      "urgency_color": "#FF6B35"
    },
    "risk_breakdown": {
      "factors": [
        {
          "name": "Blood Pressure",
          "status": "Elevated",
          "value": "145 mm Hg",
          "impact": "moderate",
          "icon": "trending_up"
        },
        {
          "name": "Cholesterol",
          "status": "High",
          "value": "260 mg/dL",
          "impact": "high",
          "icon": "warning"
        },
        {
          "name": "Exercise Tolerance",
          "status": "Reduced",
          "value": "Chest pain with exertion",
          "impact": "high",
          "icon": "warning"
        }
      ]
    },
    "probabilities": {
      "chart_data": [
        {"label": "No Disease", "value": 15.2, "color": "#4CAF50"},
        {"label": "Mild", "value": 8.5, "color": "#FFC107"},
        {"label": "Moderate", "value": 72.3, "color": "#FF6B35"},
        {"label": "Severe", "value": 3.8, "color": "#E91E63"},
        {"label": "Very Severe", "value": 0.2, "color": "#9C27B0"}
      ],
      "dominant": "Moderate (72.3%)"
    },
    "next_steps": {
      "immediate": "Schedule doctor appointment",
      "short_term": "Discuss treatment options with cardiologist",
      "long_term": "Develop heart health management plan",
      "emergency_note": "If you experience severe chest pain, shortness of breath, or other acute symptoms, call emergency services immediately (911)."
    },
    "disclaimer": {
      "text": "This is a screening tool only and not a medical diagnosis. Always consult with qualified healthcare professionals for medical advice.",
      "type": "warning"
    }
  },
  "metadata": {
    "model_version": "1.0.0",
    "prediction_time": "2024-11-15T10:30:45Z",
    "report_id": "RPT-2024-001234"
  }
}
```

---

## Color Scheme by Severity Level

### Level 0: No Disease
```json
{
  "severity_color": "#4CAF50",
  "background_color": "#E8F5E9",
  "border_color": "#4CAF50",
  "icon": "check_circle",
  "icon_color": "#4CAF50",
  "urgency": "none"
}
```

### Level 1: Mild
```json
{
  "severity_color": "#FFC107",
  "background_color": "#FFF8E1",
  "border_color": "#FFC107",
  "icon": "info",
  "icon_color": "#FFC107",
  "urgency": "low"
}
```

### Level 2: Moderate
```json
{
  "severity_color": "#FF6B35",
  "background_color": "#FFF3E0",
  "border_color": "#FF6B35",
  "icon": "warning",
  "icon_color": "#FF6B35",
  "urgency": "medium"
}
```

### Level 3: Severe
```json
{
  "severity_color": "#E91E63",
  "background_color": "#FCE4EC",
  "border_color": "#E91E63",
  "icon": "error",
  "icon_color": "#E91E63",
  "urgency": "high"
}
```

### Level 4: Very Severe
```json
{
  "severity_color": "#9C27B0",
  "background_color": "#F3E5F5",
  "border_color": "#9C27B0",
  "icon": "priority_high",
  "icon_color": "#9C27B0",
  "urgency": "critical"
}
```

---

## Icon Mapping

Use Material Icons or Font Awesome:

| Element | Icon Name (Material) | Icon Name (FontAwesome) |
|---------|---------------------|------------------------|
| No Disease | check_circle | fa-check-circle |
| Mild | info | fa-info-circle |
| Moderate | warning | fa-exclamation-triangle |
| Severe | error | fa-exclamation-circle |
| Very Severe | priority_high | fa-ambulance |
| Heart | favorite | fa-heart |
| Blood Pressure | trending_up | fa-tachometer-alt |
| Cholesterol | science | fa-flask |
| Doctor | medical_services | fa-user-md |
| Emergency | local_hospital | fa-hospital |

---

## User-Friendly Text Templates

### Severity Level Messages

**Level 0**:
```
Title: "Low Risk - Looking Good!"
Message: "Based on your information, your heart disease risk appears to be low. Keep up the healthy habits!"
```

**Level 1**:
```
Title: "Mild Risk Detected"
Message: "Your assessment shows some factors that may increase heart disease risk. A conversation with your doctor is recommended."
```

**Level 2**:
```
Title: "Moderate Risk Detected"
Message: "Your assessment indicates a moderate level of heart disease risk. We recommend scheduling a cardiology consultation."
```

**Level 3**:
```
Title: "High Risk Detected"
Message: "Your assessment shows significant heart disease risk factors. Urgent medical attention is recommended."
```

**Level 4**:
```
Title: "CRITICAL - Immediate Action Needed"
Message: "Your assessment indicates severe heart disease risk. Seek immediate emergency medical attention."
```

---

## Action Items by Severity

### Level 0 - Low Risk
```json
{
  "action_items": [
    "Maintain your current healthy lifestyle",
    "Schedule routine check-ups annually",
    "Continue regular exercise (30+ minutes, 5 days/week)",
    "Eat a heart-healthy diet rich in fruits and vegetables",
    "Monitor your blood pressure at home monthly"
  ],
  "timeline": "Next checkup in 12 months",
  "prevention_tips": true
}
```

### Level 1 - Mild Risk
```json
{
  "action_items": [
    "Schedule a consultation with your primary care doctor",
    "Discuss lifestyle modifications (diet, exercise, stress)",
    "Get a comprehensive metabolic panel blood test",
    "Consider joining a cardiac rehabilitation program",
    "Monitor symptoms and track any changes"
  ],
  "timeline": "Doctor visit within 1-2 months",
  "prevention_tips": true
}
```

### Level 2 - Moderate Risk
```json
{
  "action_items": [
    "Schedule a cardiology consultation within 2-4 weeks",
    "Bring this assessment and medical history to appointment",
    "Continue any prescribed medications",
    "Make immediate lifestyle changes (diet, exercise, smoking cessation)",
    "Monitor blood pressure daily"
  ],
  "timeline": "Cardiology appointment within 2-4 weeks",
  "prevention_tips": false
}
```

### Level 3 - Severe Risk
```json
{
  "action_items": [
    "Contact a cardiologist immediately for urgent consultation",
    "Do not delay - call within 24-48 hours",
    "Avoid strenuous physical activity until evaluated",
    "Keep a symptom diary",
    "Have someone accompany you to appointments"
  ],
  "timeline": "URGENT: Contact cardiologist within 24-48 hours",
  "emergency_info": true
}
```

### Level 4 - Critical Risk
```json
{
  "action_items": [
    "SEEK IMMEDIATE EMERGENCY CARE",
    "Go to the nearest emergency room or call 911",
    "Do not drive yourself - call ambulance or have someone drive you",
    "Bring a list of medications and medical history",
    "Inform ER staff of this risk assessment"
  ],
  "timeline": "IMMEDIATE - Do not delay",
  "emergency_info": true,
  "show_emergency_banner": true
}
```

---

## Confidence Display

Convert confidence scores to user-friendly descriptions:

```python
def get_confidence_description(confidence):
    if confidence >= 0.9:
        return {
            "text": "Very Confident",
            "color": "#4CAF50",
            "description": "The model is very confident in this prediction"
        }
    elif confidence >= 0.75:
        return {
            "text": "Confident",
            "color": "#8BC34A",
            "description": "The model is confident in this prediction"
        }
    elif confidence >= 0.60:
        return {
            "text": "Moderately Confident",
            "color": "#FFC107",
            "description": "The model has moderate confidence in this prediction"
        }
    else:
        return {
            "text": "Low Confidence",
            "color": "#FF6B35",
            "description": "The model has low confidence. Consider additional testing.",
            "warning": true
        }
```

---

## Progress Bar / Gauge Visualization

### Risk Gauge Configuration
```json
{
  "gauge": {
    "min": 0,
    "max": 4,
    "value": 2,
    "zones": [
      {"from": 0, "to": 0.5, "color": "#4CAF50", "label": "Low"},
      {"from": 0.5, "to": 1.5, "color": "#FFC107", "label": "Mild"},
      {"from": 1.5, "to": 2.5, "color": "#FF6B35", "label": "Moderate"},
      {"from": 2.5, "to": 3.5, "color": "#E91E63", "label": "Severe"},
      {"from": 3.5, "to": 4, "color": "#9C27B0", "label": "Critical"}
    ],
    "needle_value": 2,
    "title": "Risk Level"
  }
}
```

---

## Error Responses

### Validation Error
```json
{
  "success": false,
  "error": {
    "type": "validation_error",
    "message": "Some required information is missing or invalid",
    "fields": [
      {
        "field": "age",
        "error": "Age must be between 1 and 120",
        "current_value": 200
      },
      {
        "field": "trestbps",
        "error": "Blood pressure must be between 80 and 250 mm Hg",
        "current_value": 50
      }
    ],
    "display": {
      "title": "Please Check Your Information",
      "icon": "error_outline",
      "color": "#F44336"
    }
  }
}
```

### Server Error
```json
{
  "success": false,
  "error": {
    "type": "server_error",
    "message": "We're sorry, but we couldn't complete your assessment at this time.",
    "details": "An unexpected error occurred. Please try again in a few moments.",
    "support_message": "If this problem persists, please contact support@example.com",
    "display": {
      "title": "Something Went Wrong",
      "icon": "error",
      "color": "#F44336"
    }
  }
}
```

---

## Sample Frontend Implementation

### Displaying Results
```javascript
// After receiving API response
function displayResults(response) {
  if (!response.success) {
    showError(response.error);
    return;
  }
  
  const data = response.data;
  
  // Set colors and styling
  document.getElementById('result-card').style.borderColor = data.display.severity_color;
  document.getElementById('result-card').style.backgroundColor = data.display.background_color;
  
  // Display main result
  document.getElementById('result-title').textContent = data.display.title;
  document.getElementById('result-title').style.color = data.display.severity_color;
  document.getElementById('result-message').textContent = data.display.message;
  
  // Show icon
  document.getElementById('result-icon').innerHTML = 
    `<i class="material-icons" style="color: ${data.display.severity_color}">${data.display.severity_icon}</i>`;
  
  // Confidence bar
  document.getElementById('confidence-bar').style.width = `${data.display.confidence_bar}%`;
  document.getElementById('confidence-text').textContent = data.display.confidence_display;
  
  // Action items
  const actionList = document.getElementById('action-items');
  actionList.innerHTML = '';
  data.recommendation.action_items.forEach(item => {
    const li = document.createElement('li');
    li.textContent = item;
    actionList.appendChild(li);
  });
  
  // Show emergency banner if needed
  if (data.next_steps.show_emergency_banner) {
    document.getElementById('emergency-banner').style.display = 'block';
  }
}
```

---

## Responsive Design Breakpoints

```css
/* Mobile First */
.result-card {
  padding: 1rem;
  margin: 1rem auto;
  max-width: 100%;
}

/* Tablet */
@media (min-width: 768px) {
  .result-card {
    padding: 2rem;
    max-width: 700px;
  }
}

/* Desktop */
@media (min-width: 1024px) {
  .result-card {
    padding: 2.5rem;
    max-width: 900px;
  }
}
```

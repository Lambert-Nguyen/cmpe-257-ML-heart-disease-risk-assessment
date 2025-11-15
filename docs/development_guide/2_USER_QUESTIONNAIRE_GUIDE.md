# User-Friendly Questionnaire Guide
## For Heart Disease Risk Assessment Web Application

This guide helps translate clinical features into user-friendly questions for the web interface.

---

## Patient Information Form

### 1. Basic Demographics

#### Age
**Question**: "What is your age?"
**Input Type**: Number input (years)
**Range**: 1-120
**Help Text**: "Please enter your current age in years"
**Required**: Yes
**Example**: 45

---

#### Sex
**Question**: "What is your biological sex?"
**Input Type**: Radio buttons or dropdown
**Options**:
- Male
- Female
**Help Text**: "Select your biological sex as recorded in medical records"
**Required**: Yes
**Default**: None

---

### 2. Symptoms & Pain

#### Chest Pain Type (cp)
**Question**: "What type of chest discomfort do you experience, if any?"
**Input Type**: Radio buttons with descriptions
**Options**:
1. **"Typical angina"** 
   - *Description*: "Classic heart-related chest pain that occurs with exertion and is relieved by rest"
   - *User-friendly*: "Pressure or squeezing in the chest during physical activity, relieved by rest"

2. **"Atypical angina"** 
   - *Description*: "Chest pain that may be heart-related but doesn't follow the classic pattern"
   - *User-friendly*: "Chest discomfort that doesn't follow a clear pattern"

3. **"Non-anginal"** 
   - *Description*: "Chest pain unlikely to be from the heart"
   - *User-friendly*: "Sharp or stabbing chest pain, not related to exertion"

4. **"Asymptomatic"** 
   - *Description*: "No chest pain or discomfort"
   - *User-friendly*: "No chest pain or discomfort"

**Help Text**: "Describe any chest discomfort you've experienced. If unsure, select 'No chest pain'"
**Required**: Yes
**Icon/Visual**: Heart icon with pain indicators

---

### 3. Vital Signs

#### Resting Blood Pressure (trestbps)
**Question**: "What is your resting blood pressure? (Systolic/Top Number)"
**Input Type**: Number input (mm Hg)
**Range**: 80-250
**Help Text**: "The top/first number from your blood pressure reading (e.g., if your BP is 120/80, enter 120). If you don't know, leave blank."
**Required**: No (can handle missing)
**Example**: 120
**Visual Aid**: Blood pressure gauge showing categories:
- < 120: Normal (green)
- 120-129: Elevated (yellow)
- 130-139: High Stage 1 (orange)
- 140+: High Stage 2 (red)

---

#### Cholesterol (chol)
**Question**: "What is your total cholesterol level?"
**Input Type**: Number input (mg/dL)
**Range**: 100-600
**Help Text**: "Your total cholesterol from a recent blood test in mg/dL. If you don't know, leave blank."
**Required**: No
**Example**: 200
**Visual Aid**: Cholesterol level chart:
- < 200: Desirable (green)
- 200-239: Borderline high (yellow)
- 240+: High (red)

---

### 4. Blood Sugar

#### Fasting Blood Sugar (fbs)
**Question**: "Is your fasting blood sugar greater than 120 mg/dL?"
**Input Type**: Radio buttons
**Options**:
- Yes (TRUE)
- No (FALSE)
- I don't know
**Help Text**: "Fasting blood sugar from a blood test after not eating for 8+ hours. Normal is below 100 mg/dL. If you have diabetes or prediabetes, select 'Yes'."
**Required**: Yes
**Default**: FALSE

---

### 5. Heart Tests

#### Resting ECG Results (restecg)
**Question**: "What were your resting ECG/EKG results?"
**Input Type**: Radio buttons with info tooltips
**Options**:
1. **"Normal"**
   - *Description*: "No abnormalities detected"

2. **"ST-T wave abnormality"**
   - *Description*: "Minor changes in heart rhythm, may indicate strain"
   - *User-friendly*: "Minor irregularities detected"

3. **"Left ventricular hypertrophy"**
   - *Description*: "Thickening of the heart's main pumping chamber"
   - *User-friendly*: "Heart muscle thickening detected"

**Help Text**: "If you've had an ECG/EKG (heart rhythm test), select your most recent result. If you haven't had one, select 'Normal' or 'I don't know'."
**Required**: Yes (default to Normal if unknown)
**Info Icon**: "What's an ECG?" tooltip

---

#### Maximum Heart Rate Achieved (thalch)
**Question**: "What was your maximum heart rate during exercise or a stress test?"
**Input Type**: Number input (beats per minute)
**Range**: 60-220
**Help Text**: "From a stress test or exercise test. If you don't know, leave blank. For reference, estimated max heart rate is about 220 minus your age."
**Required**: No
**Example**: 150
**Auto-calculate option**: "Calculate estimated max (220 - age)"

---

#### Exercise-Induced Angina (exang)
**Question**: "Do you experience chest pain during exercise or physical activity?"
**Input Type**: Radio buttons
**Options**:
- Yes (TRUE)
- No (FALSE)
**Help Text**: "Does physical activity or exercise trigger chest pain or discomfort?"
**Required**: Yes
**Default**: FALSE

---

### 6. Exercise Test Results

#### ST Depression (oldpeak)
**Question**: "ST depression value from exercise test"
**Input Type**: Number input (decimal)
**Range**: 0.0-6.0
**Help Text**: "This value comes from an exercise stress test and measures changes in your heart's electrical activity. If you haven't had a stress test, enter 0 or leave blank."
**Required**: No
**Example**: 1.0
**Note for UI**: Consider "I haven't had this test" checkbox that auto-fills with 0

---

#### ST Slope (slope)
**Question**: "Slope of peak exercise ST segment (from stress test)"
**Input Type**: Radio buttons
**Options**:
1. **"Upsloping"** - Generally favorable
2. **"Flat"** - Possibly concerning
3. **"Downsloping"** - More concerning
4. **"I haven't had this test"** - Will use default

**Help Text**: "From an exercise stress test. If you haven't had this test, select 'I haven't had this test'."
**Required**: No
**Note**: This is a technical feature - consider simplifying to "Have you had a stress test? Yes/No"

---

### 7. Advanced Cardiac Tests

#### Number of Major Vessels (ca)
**Question**: "Number of major heart vessels with blockage (from angiography)"
**Input Type**: Dropdown or radio buttons
**Options**:
- 0 - No blockages
- 1 - One vessel
- 2 - Two vessels  
- 3 - Three vessels
- 4 - Four vessels
- I haven't had this test

**Help Text**: "From a cardiac catheterization or angiogram. This test uses dye to visualize blood vessels. If you haven't had this test, select 'I haven't had this test'."
**Required**: No
**Note**: Very technical - many users won't have this

---

#### Thalassemia Test (thal)
**Question**: "Thalassemia or blood flow test result"
**Input Type**: Radio buttons
**Options**:
1. **"Normal"** - Normal blood flow
2. **"Fixed defect"** - Permanent blood flow problem
3. **"Reversible defect"** - Temporary blood flow problem
4. **"I haven't had this test"**

**Help Text**: "From a nuclear stress test or similar imaging. If you haven't had this test, select 'I haven't had this test'."
**Required**: No
**Note**: Consider simplifying or making optional

---

## Form Design Recommendations

### Progressive Disclosure
Organize into sections that users complete step-by-step:

**Section 1: About You** (always show)
- Age, Sex

**Section 2: Symptoms** (always show)
- Chest pain type
- Exercise-induced chest pain

**Section 3: Basic Health Metrics** (always show)
- Blood pressure
- Cholesterol
- Blood sugar

**Section 4: Test Results** (collapsible/optional)
- Heart rate, ECG results, exercise test results

**Section 5: Advanced Tests** (collapsible/optional)
- ST slope, major vessels, thalassemia
- Include "I haven't had these tests" option that auto-fills defaults

### Visual Design
- **Color coding**: Use green/yellow/orange/red for risk levels
- **Progress indicator**: Show completion percentage
- **Help icons**: ? tooltip on every question
- **Examples**: Show sample values
- **Units**: Always display units (mg/dL, mm Hg, bpm)

### User Experience
- **Auto-save**: Save progress as user fills out form
- **Skip options**: "I don't know" or "Not tested" for optional fields
- **Validation**: Real-time feedback on valid ranges
- **Mobile-friendly**: Large tap targets, single-column layout
- **Accessibility**: Screen reader compatible, keyboard navigation

### Sample UI Flow
```
┌─────────────────────────────────────┐
│  Heart Disease Risk Assessment      │
│  Step 1 of 5: Basic Information    │
│  ●●●○○                              │
└─────────────────────────────────────┘

  Age: [45]  years

  Sex: ○ Male  ● Female

       [Continue →]

┌─────────────────────────────────────┐
│  Step 2 of 5: Symptoms             │
│  ●●●●○                              │
└─────────────────────────────────────┘

  Do you experience chest pain?
  
  ○ Pressure/squeezing during activity
  ○ Irregular chest discomfort  
  ○ Sharp/stabbing pain
  ● No chest pain
  
       [← Back]  [Continue →]
```

---

## Default Values for Missing Data

When users select "I don't know" or skip optional fields:

| Feature | Default Value | Rationale |
|---------|--------------|-----------|
| trestbps | 130 | Median blood pressure |
| chol | 240 | Median cholesterol |
| fbs | FALSE | Most people don't have elevated blood sugar |
| restecg | normal | Most common result |
| thalch | 220 - age | Estimated max heart rate formula |
| exang | FALSE | Most people don't have exercise angina |
| oldpeak | 0.0 | Indicates no stress test |
| slope | upsloping | Most favorable/common |
| ca | 0 | No angiogram done / no blockages |
| thal | normal | No nuclear test done / normal result |

---

## Accessibility Considerations

1. **Screen readers**: Proper ARIA labels on all inputs
2. **Keyboard navigation**: Tab order follows logical flow
3. **Color blindness**: Don't rely solely on color (use icons + text)
4. **Language**: Provide translations for common languages
5. **Reading level**: Use 6th-8th grade reading level
6. **Error messages**: Clear, actionable error text

---

## Mobile-Specific Considerations

1. **Touch targets**: Minimum 44x44 pixels
2. **Input types**: Use `type="number"` for numeric fields
3. **Dropdowns**: Native mobile dropdowns work better than custom
4. **Layout**: Single column, vertical scrolling
5. **Keyboard**: Numeric keyboard for number inputs
6. **Autocomplete**: Disable where not applicable

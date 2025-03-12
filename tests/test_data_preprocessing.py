import pytest
import pandas as pd
from io import StringIO
from pcosdiagnosis.utils.main_utils.utils import load_object

# Sample CSV data
csv_data = """
Age (yrs),Weight (Kg),Height(Cm),BMI,Blood Group,Pulse rate(bpm),RR (breaths/min),Hb(g/dl),Cycle(R/I),Cycle length(days),Marraige Status (Yrs),Pregnant(Y/N),No. of aborptions,I beta-HCG(mIU/mL),II beta-HCG(mIU/mL),FSH(mIU/mL),LH(mIU/mL),FSH/LH,Hip(inch),Waist(inch),Waist:Hip Ratio,TSH (mIU/L),AMH(ng/mL),PRL(ng/mL),Vit D3 (ng/mL),PRG(ng/mL),RBS(mg/dl),Weight gain(Y/N),hair growth(Y/N),Skin darkening (Y/N),Hair loss(Y/N),Pimples(Y/N),Fast food (Y/N),Reg.Exercise(Y/N),BP _Systolic (mmHg),BP _Diastolic (mmHg),Follicle No. (L),Follicle No. (R),Avg. F size (L) (mm),Avg. F size (R) (mm),Endometrium (mm)
33,68.8,165.0,25.27089073,11,72,18,11.8,2,5,10.0,1,0,494.08,494.08,5.54,0.88,6.295454545,40,36,0.9,2.54,6.63,10.52,49.7,0.36,84.0,0,0,0,1,1,1.0,0,120,80,13,15,18.0,20.0,10.0
"""

# Read the CSV data into a DataFrame
data = pd.read_csv(StringIO(csv_data))

@pytest.fixture
def preprocessor():
    return load_object("final_model/preprocessor.pkl")

def test_preprocessor_loading(preprocessor):
    assert preprocessor is not None

def test_data_preprocessing(preprocessor):
    # Ensure the test data has the same column names as the training data
    feature_names = preprocessor.named_steps['imputer'].feature_names_in_
    data.columns = feature_names

    processed_data = preprocessor.transform(data)
    assert processed_data.shape == (1, len(data.columns))
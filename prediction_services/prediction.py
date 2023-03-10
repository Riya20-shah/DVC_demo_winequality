import yaml
import os
import json
import joblib
import numpy as np

params_path = "/home/scaledge-riya/Desktop/MLops_demo_projects/wine_predicton_DVC/params.yaml"
schema_path = os.path.join("prediction_services","schema_in.json")

class NotInRange(Exception):
    def __init__(self,message="value entered are not in range"):
        self.message = message
        super().__init__(self.message)

class NotIncols(Exception):
    def __init__(self,message="Not in columns"):
        self.message = message
        super().__init__(self.message)

def read_params(config_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config
def predict(data):
    config = read_params(params_path)
    model_dir_path = config["webapp_model_dir"]
    model = joblib.load(model_dir_path)
    prediction = model.predict(data).tolist()[0]
    try:
        if 3 <= prediction <= 8:
            return prediction
        else:
            raise NotInRange
    except NotInRange:
        return "Unexpected result"


def get_schema(schema_path=schema_path):
    with open(schema_path) as json_file:
        schema = json.load(json_file)
    return schema

def validate_input(dict_request):

    def _validate_cols(col):
        schema = get_schema()
        actual_cols = schema.keys()
        if col not in actual_cols:
            raise NotIncols

    def _validate_values(col , val):
        schema = get_schema()
        if not (schema[col]["min"] <= float(dict_request[col]) <= schema[col]["max"]):
            raise NotInRange
    for col , val in dict_request.items():
        _validate_cols(col)
        _validate_values(col , val)

    return True

def form_response(dict_request):
    if validate_input(dict_request):
        data = dict_request.values()
        data = [list(map(float, data))]
        response = predict(data)
        return response

def api_response(dict_request):
    try:
        if validate_input(dict_request):
            data = np.array([list(dict_request.json.values())])
            response = predict(data)
            response = {"response": response}
            print("response =",response)
            return response
    except Exception as e:
        response = {"the_expected_range":get_schema(),"response":str(e)}


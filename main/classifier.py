from google.cloud import aiplatform
from google.oauth2 import service_account

# prediction using model endpoint
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'main/azaan.json'

def predict_text_classification_single_label_sample(project, location, endpoint, content):
    try:
        aiplatform.init(project=project, location=location)
        predictor = aiplatform.Endpoint(endpoint)

        result = predictor.predict(instances=[{"content": content}], parameters={})

        names = result[0][0]['displayNames'].copy()
        values = result[0][0]['confidences'].copy()

        print(names,values)

        max_index = values.index(max(values))

        print(names[max_index])

        return names[max_index]

    except Exception as e:
        print(f"An error occurred: {e}")
        return None  # Return None in case of an error

def classifier_azaan(user_input):
    project = "spherical-list-412116"
    location = "us-central1"
    endpoint = "4741826413714210816"
    content = user_input

    return predict_text_classification_single_label_sample(project, location, endpoint, content)


def classifier_gopika(user_input):
    project = "theta-cell-406519"
    location = "us-central1"
    endpoint = "398667523068788736"
    content = user_input

    return predict_text_classification_single_label_sample(project, location, endpoint, content)




def classify_text(user_input):
    # Trying Azaan's model
    result = classifier_azaan(user_input)

    # If Azaan's model fails, trying Gopika's model
    if result is None:
        print("Gopika's Model")
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'main/gopika.json'
        result = classifier_gopika(user_input)

    return result

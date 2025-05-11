import joblib
from extract_features import extract_features

def check_url(url):
    model = joblib.load("phishing_model.pkl")
    features = extract_features(url)
    input_data = [list(features.values())]
    prediction = model.predict(input_data)[0]
    print("\nResult: ", "Phishing" if prediction == 1 else "Legitimate")

if __name__ == "__main__":
    url_input = input("Enter a URL to check: ")
    check_url(url_input)
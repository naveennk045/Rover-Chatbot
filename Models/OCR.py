from google.cloud import vision
from google.oauth2 import service_account
import io

def Extract(imageInput):
    # Path to the service account JSON file
    service_account_path = r"V:\Projects\Python Projects\Rover Chatbot\Jamsith.json"
    
    # Load the credentials
    credentials = service_account.Credentials.from_service_account_file(service_account_path)
    
    # Initialize the client with the credentials
    client = vision.ImageAnnotatorClient(credentials=credentials)

    # Determine the type of imageInput and read the content accordingly
    if isinstance(imageInput, str):
        # If imageInput is a file path, read the file
        with io.open(imageInput, 'rb') as image_file:
            content = image_file.read()
    elif isinstance(imageInput, io.BytesIO):
        # If imageInput is a BytesIO object, read the content directly
        content = imageInput.read()
    else:
        raise ValueError("Unsupported input type. Expected a file path or BytesIO object.")

    image = vision.Image(content=content)

    # Define the features you want to use
    features = [
        vision.Feature(type=vision.Feature.Type.TEXT_DETECTION),
        vision.Feature(type=vision.Feature.Type.DOCUMENT_TEXT_DETECTION),  # Handwritten text detection
        vision.Feature(type=vision.Feature.Type.LANDMARK_DETECTION),
        vision.Feature(type=vision.Feature.Type.LABEL_DETECTION),
        vision.Feature(type=vision.Feature.Type.LOGO_DETECTION)
    ]

    # Create the request with multiple features
    requests = [vision.AnnotateImageRequest(image=image, features=features)]

    # Send the request
    response = client.batch_annotate_images(requests=requests)

    # Collect all detected information
    detectedText = ""
    labels = []

    for i, resp in enumerate(response.responses):
        if resp.error.message:
            print(f"Error for image {i}: {resp.error.message}")
            continue

        # Text detection
        if resp.text_annotations:
            detectedText = resp.full_text_annotation.text

        # Label detection
        if resp.label_annotations:
            labels += [label.description for label in resp.label_annotations]

    label_list = ", ".join(labels)
    text = detectedText.replace('\n', ' ')

    detectedText = f"""
    \"{text.strip()}\",
    The image also contains visual elements related to {label_list},
    """
    return detectedText

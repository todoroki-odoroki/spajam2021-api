from app.dependencies.aws import rekognition_client


def show_custom_labels(model: str, bucket: str, file: bytes):
    response = rekognition_client.detect_custom_labels(
        Image={"Bytes": file}, ProjectVersionArn=model
    )
    return response["CustomLabels"]


def detect_face(model: str, bucket: str, file: bytes):
    response = rekognition_client.detect_faces(
        Image={"Bytes": file}, Attributes=["ALL"]
    )
    return response["FaceDetails"][0]

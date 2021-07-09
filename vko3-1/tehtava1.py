import requests
import json

#gets json data
response = requests.get("https://2ri98gd9i4.execute-api.us-east-1.amazonaws.com/dev/academy-checkpoint2-json")
data = response.json()
human_data = data["items"]

final_data = []
for i in human_data:
    final_data.append(i["parameter"])

#writes data from "parameter" to a file
with open("checkpoint.txt", "w") as tiedosto:
    for rivi in final_data:
        tiedosto.write(rivi)
        tiedosto.write("\n")

#function to make a new bucket
def makeStorage(bucket_name:str):
    # Imports the Google Cloud client library
    from google.cloud import storage

    # Instantiates a client
    storage_client = storage.Client()

    # Creates the new bucket
    bucket = storage_client.create_bucket(bucket_name)

    print("Bucket {} created.".format(bucket.name))

#funtion to upload object to bucket
def upload_blob(bucket_name, source_file_name, destination_blob_name):
    from google.cloud import storage
    """Uploads a file to the bucket."""
    # The ID of your GCS bucket
    # bucket_name = "your-bucket-name"
    # The path to your file to upload
    # source_file_name = "local/path/to/file"
    # The ID of your GCS object
    # destination_blob_name = "storage-object-name"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(
        "File {} uploaded to {}.".format(
            source_file_name, destination_blob_name
        )
    )

#makes bucket checkpoint3 and uploads file to it
makeStorage("checkpoint3")
upload_blob("checkpoint3", "checkpoint.txt", "checkpoint.txt")
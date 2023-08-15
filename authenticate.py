import os
from google_auth_oauthlib.flow import InstalledAppFlow
import googleapiclient.discovery
from google.oauth2.credentials import Credentials
import requests
import re

# Replace with your own credentials
CLIENT_ID = '782925300094-s0nnqlhsgl81t771uopqh770eku3e79d.apps.googleusercontent.com'
CLIENT_SECRET = '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'
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']  # Adjust scope as needed

# Create the flow
flow = InstalledAppFlow.from_client_secrets_file(
    './credentials.json',  # Path to your client secret JSON file
    scopes=SCOPES
)

def get_auth_token():
    # Run the authorization flow
    credentials = flow.run_local_server()
    return (credentials.token)
    
def get_video_id():
    link =input("Enter the youtube video link:")
    match = re.match(r"https://www.youtube.com/watch\?v=(.*)", link)

    if match:
        return match.group(1)
    else:
        raise Exception("Invalid YouTube link.") 

# You can now use `credentials` to make authenticated requests to the YouTube Data API.

if __name__ == "__main__":
  auth_token = get_auth_token()
  print(auth_token)
  video_id=get_video_id()
  url = f'https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&access_token={auth_token}'
  comment_data = {
    "snippet": {
        "videoId": video_id,
        "topLevelComment": {
            "snippet": {
                "textOriginal": "This is a test comment."
            }
        }
    }
}
  response = requests.post(url, json=comment_data)

# Check the response
if response.status_code == 200:
    print("Comment added successfully.")
else:
    print("Error adding comment.")
    print("Response:", response.text)
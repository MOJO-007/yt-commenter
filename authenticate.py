import os
from google_auth_oauthlib.flow import InstalledAppFlow
import googleapiclient.discovery
from google.oauth2.credentials import Credentials
import requests
import re

def youtube_bot():
    print("You are using youtube Bot:")
    auth_token = get_auth_token()
    video_id=get_video_id()
    comment_text=input("Enter the comment to be added: ")
    url = f'https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&access_token={auth_token}'
    comment_data = {
    "snippet": {
        "videoId": video_id,
        "topLevelComment": {
            "snippet": {
                "textOriginal": comment_text
            }
        }
    }
    }
    response = requests.post(url, json=comment_data)

    if response.status_code == 200:
        print("Comment added successfully.")
    else:
        print("Error adding comment.")
        print("Response:", response.text)



    return 0

def get_auth_token():
    SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
    flow = InstalledAppFlow.from_client_secrets_file(
    './credentials.json',  # Path to your client secret JSON file
    scopes=SCOPES
    )
    credentials = flow.run_local_server()
    return (credentials.token)
    
def get_video_id():
    link =input("Enter the youtube video link:")
    match = re.match(r"https://www.youtube.com/watch\?v=(.*)", link)

    if match:
        return match.group(1)
    else:
        raise Exception("Invalid YouTube link.") 

if __name__ == "__main__":
    youtube_bot()
  
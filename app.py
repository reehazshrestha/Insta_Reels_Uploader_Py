from instagrapi import Client

cl = Client()

username = 'your_user_name'
password = 'your_password'
cl.login(username, password)

video_path = 'reel_name.mp4'

caption = 'You can add your caption here !!!'

while True:
    media = cl.video_upload(video_path, caption)
    print("Reel uploaded successfully!")
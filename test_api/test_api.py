import subprocess
import json


def run_curl_command(url):
    process = subprocess.Popen(['curl', '-s', url], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if process.returncode == 0:
        print("HTTP Request Successful")
    else:
        print(f"HTTP Request Failed with status code: {process.returncode}")

    if process.returncode != 0:
        print(f"Error: {stderr.decode('utf-8')}")
        return None
    response = stdout.decode('utf-8')
    return json.loads(response)


data_posts = run_curl_command('https://jsonplaceholder.typicode.com/posts/1')
data_comments = run_curl_command('https://jsonplaceholder.typicode.com/comments/1')
data_albums = run_curl_command('https://jsonplaceholder.typicode.com/albums/1')

if 'userId' in data_posts and 'id' in data_posts and 'title' in data_posts:
    print("Test /posts/1: PASSED")
else:
    print("Test /posts/1: FAILED")

if 'postId' in data_comments and 'id' in data_comments and 'name' in data_comments:
    print("Test /comments/1: PASSED")
else:
    print("Test /comments/1: FAILED")

if 'userId' in data_albums and 'id' in data_albums and 'title' in data_albums:
    print("Test /albums/1: PASSED")
else:
    print("Test /albums/1: FAILED")
    
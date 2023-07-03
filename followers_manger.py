import requests

# Set up your access token
access_token = 'ghphhhhhhhhhhYrU0l'

# Specify the username for which you want to collect followers and following
username = 'YassinTalssis'

# Make API requests to retrieve followers and following
headers = {
    'Authorization': f'token {access_token}',
    'Accept': 'application/vnd.github.v3+json'
}

# Function to handle pagination and retrieve all pages
def get_all_pages(url):
    all_data = []
    while url:
        response = requests.get(url, headers=headers)
        data = response.json()
        all_data.extend(data)
        url = None
        if 'Link' in response.headers:
            links = response.headers['Link'].split(', ')
            for link in links:
                if 'rel="next"' in link:
                    url = link[link.index('<') + 1:link.index('>')]
    return all_data
def user_didnt_follow_back(lst1, lst2):
    lst3=[]
    for l in lst1:
        if l not in lst2:
            lst3.append(l)
    return lst3
# Fetch followers
followers_url = f'https://api.github.com/users/{username}/followers'
all_followers = get_all_pages(followers_url)

# Fetch following
following_url = f'https://api.github.com/users/{username}/following'
all_following = get_all_pages(following_url)

# Print followers
followers=[]
following=[]
print(f'{username}\'s followers:')
for follower in all_followers:
    followers.append(follower['login'])
print(len(followers))
print()

# Print following
print(f'{username} is following:')
for user in all_following:
    following.append(user['login'])
print(len(following))
print('The users didnt follow back:')
print(user_didnt_follow_back(following,followers))

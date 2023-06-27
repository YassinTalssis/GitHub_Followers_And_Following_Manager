# GitHub_Followers_And_Following_Manager
This code is designed to retrieve a user's followers and users they are following on GitHub using the GitHub API. The code requires an access token for authentication.

After setting up the access token and specifying the username for which to collect followers and following, the code makes API requests using the access token to retrieve the data. The function get_all_pages is used to handle pagination and retrieve all pages of data.

Once the data is retrieved, the code prints the number of followers and following for the specified user. It also determines the users who are not following the specified user back and prints that list.

In summary, this code allows you to fetch a user's followers and following on GitHub and identify the users who are not following the specified user back.

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

# Print first 50 links for a YouTube search query
def search_keyword(query):
    api_key = ''
    q = query.replace(' ', '%20')
    url = 'https://www.googleapis.com/youtube/v3/search?part=snippet&type=video&maxResults=50&q='
    final_url = url + q + '&key=' + api_key
    data = requests.get(final_url)
    data_json = data.json()
    print(query + ':\n')
    for item in data_json['items']:
        print('https://www.youtube.com/watch?v=' + item['id']['videoId'])

# Print first 50 links for multiple YouTube search queries (input list as array)
def search_keywords(query_list):
    for key in query_list:
        search_keyword(key)
        print('\n')

# Print first 50 links of a playlist
def playlist_links(playlist_ID):
    api_key = ''
    url = 'https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=50&playlistId='
    final_url = url + playlist_ID + '&key=' + api_key
    data = requests.get(final_url)
    data_json = data.json()
    for item in data_json['items']:
        print('https://www.youtube.com/watch?v=' + item['snippet']['resourceId']['videoId'])

# Return uploads playlist ID for a channel username
def uploads_ID(channel_username_or_ID, username_or_ID_binary):
    api_key = ''
    usr_or_ID = channel_username_or_ID.replace(' ', '%20')
    url = 'https://www.googleapis.com/youtube/v3/channels?part=contentDetails&'
    if username_or_ID_binary == 'username':
        temp_url = url + 'forUsername='
    else:
        temp_url = url + 'id='
    final_url = temp_url + usr_or_ID + '&key=' + api_key
    data = requests.get(final_url)
    data_json = data.json()
    for item in data_json['items']:
        return(item['contentDetails']['relatedPlaylists']['uploads'])

# Return uploads playlist ID for a channel username
def uploads_ID_2(channel_username_or_ID, username_or_ID_binary):
    if username_or_ID_binary == 'id':
        upload_ID = 'UU' + channel_username_or_ID[2:]
        return upload_ID
    else:
        api_key = ''
        usr_nm = channel_username_or_ID.replace(' ', '%20')
        url = 'https://www.googleapis.com/youtube/v3/channels?part=contentDetails&forUsername='
        final_url = url + usr_nm + '&key=' + api_key
        data = requests.get(final_url)
        data_json = data.json()
        for item in data_json['items']:
            return(item['contentDetails']['relatedPlaylists']['uploads'])

# Print first 50 links of a channel's uploads
def channel_uploads(channel_username_or_ID):
    uploads_playlist_ID = uploads_ID_2(channel_username, 'username')
    api_key = ''
    print(channel_username + ' upload list:\n')
    playlist_links(uploads_playlist_ID)

# Pick uploads_ID or uploads_ID_2 based on legitimacy of 2's logic
# Figure out how best to input difference between username & id
# 1. add a second input specifying username or ID
# 2. require something concatenated to end of first input - not intuitive enough
# 3. use separate functions (meh)


# Print first 50 links of multiple channels' uploads
def mult_channel_uploads_pull(username_list):
    for username in username_list:
        channel_uploads(username)
        print('\n')


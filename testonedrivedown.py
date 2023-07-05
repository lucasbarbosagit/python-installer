import os
import requests
from ms_graph import generate_access_token, GRAPH_API_ENDPOINT

APP_ID = '40966430-b2eb-4769-ae2a-3027a1ec97c2'
SCOPES = ['Files.Read']
save_location = os.getcwd()
directory = "programas_baixados"
parent_dir = save_location
  
path = os.path.join(parent_dir, directory)

file_ids = []

access_token = generate_access_token(APP_ID, scopes=SCOPES)
headers = {
	'Authorization': 'Bearer ' + access_token['access_token']
}

def baixarprogs(file_ids):
 if not os.path.isdir(path):
   os.mkdir(path) 
# Step 1. get the file name
 for file_id in file_ids:
   response_file_info = requests.get(
		GRAPH_API_ENDPOINT + f'/me/drive/items/{file_id}',
		headers=headers,
		params={'select': 'name'}
	)
   file_name = response_file_info.json().get('name')

	# Step 2. downloading OneDrive file
   response_file_content = requests.get(GRAPH_API_ENDPOINT + f'/me/drive/items/{file_id}/content', headers=headers)
   with open(os.path.join(path, file_name), 'wb') as _f:
     _f.write(response_file_content.content)
 file_ids.clear()
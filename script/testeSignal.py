import requests

app_id = 'script'
api_key = 'YTM5NGFhZmMtODFlNi00ODVkLTk4NjMtOTZlOWI4OTBlM2Yw'
headers = {'Authorization': f'Basic {api_key}', 'Content-Type': 'application/json'}

# Mensagem de notificação
payload = {
    'app_id': app_id,
    'included_segments': ['All'],
    'contents': {'en': 'Corpo da notificação'},
    'headings': {'en': 'Título da notificação'}
}

# Enviar a mensagem de notificação
response = requests.post('https://onesignal.com/api/v1/notifications', json=payload, headers=headers)
print('Mensagem enviada:', response.json())
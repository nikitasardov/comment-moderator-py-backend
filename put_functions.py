import json

def put_user_info(user_id, new_name, app_data):
    new_users = []
    for user in app_data['users']:
        if user['id'] == user_id:
            new_users.append({'id': user_id, 'name': new_name})
        else:
            new_users.append(user)
    app_data.update({'users': new_users})
    print(app_data['users'])

    path = 'data.json'
    try:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(app_data, f)
        return True
    except Exception:
        return False
    finally:
        f.close()


import json

def dump_data(app_data, path = 'data.json'):
    try:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(app_data, f)
        return True
    except Exception:
        return False
    finally:
        f.close()

def put_comment_info(comment_id, new_text, app_data):
    new_comments = []
    id_found = False
    for comment in app_data['comments']:
        if comment['id'] == comment_id:
            id_found = True
            new_comments.append({'id': comment_id, 'text': new_text, 'commenter': comment['commenter']})
        else:
            new_comments.append(comment)
    if not id_found:
        return False
    app_data.update({'comments': new_comments})
    print(app_data['comments'])
    if dump_data(app_data):
        return True
    else:
        return False

def put_user_info(user_id, new_name, app_data):
    new_users = []
    id_found = False
    for user in app_data['users']:
        if user['id'] == user_id:
            id_found = True
            new_users.append({'id': user_id, 'name': new_name})
        else:
            new_users.append(user)
    if not id_found:
        return False
    app_data.update({'users': new_users})
    print(app_data['users'])
    if dump_data(app_data):
        return True
    else:
        return False
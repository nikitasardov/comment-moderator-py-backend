def get_author_info(author_id, app_data):
    for user in app_data['users']:
        if user['id'] == author_id:
            author = {
                'id': user['id'],
                'name': user['name']
            }
    if 'author' in locals():
        return {
            'id': author['id'],
            'name': author['name']
        }
    else:
        return {
            'id': '',
            'name': ''
        }

def get_comments(comments_id_array, app_data):
    comments_info_array = []
    for comment_id in comments_id_array:
        for comment in app_data['comments']:
            if comment['id'] == comment_id:
                prepared_comment = {
                    'id': comment['id'],
                    'text': comment['text'],
                    'commenter': get_author_info(comment['commenter'], app_data)
                }
                comments_info_array.append(prepared_comment)
    return comments_info_array

def get_comments_by_author(author_id):
    comments_info_array = []
    return comments_info_array

def get_article_by_id(article_id, app_data):
    for article in app_data['articles']:
        if article['id'] == article_id:
            article_info = {
                'id': article['id'],
                'author': get_author_info(article['author'], app_data),
                'title': article['title'],
                'text': article['text'],
                'comments': get_comments(article['comments'], app_data)
            }

    if 'article_info' in locals():
        return {
            'id': article_info['id'],
            'author': article_info['author'],
            'title': article_info['title'],
            'text': article_info['text'],
            'comments': article_info['comments']
        }
    else:
        return {
            'id': '',
            'author': '',
            'title': '',
            'text': '',
            'comments': ''
        }


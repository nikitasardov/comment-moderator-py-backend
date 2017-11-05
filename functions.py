def get_author_info(author_id, app_data):
    author_info = {
        'id': '',
        'name': ''
    }
    for user in app_data['users']:
        if user['id'] == author_id:
            author_info = user
    return {
        'id': author_info['id'],
        'name': author_info['name']
    }

def get_comments(comments_id_array, app_data):
    comments_info_array = []
    for comment_id in comments_id_array:
        for comment in app_data['comments']:
            if comment['id'] == comment_id:
                prepared_comment = comment
                prepared_comment['commenter'] = get_author_info(prepared_comment['commenter'], app_data)
                comments_info_array.append(prepared_comment)
    return comments_info_array

def get_comments_by_author(author_id):
    comments_info_array = []
    return comments_info_array

def get_article_by_id(article_id, app_data):
    article_info = {
        'id': '',
        'author': '',
        'title': '',
        'text': '',
        'comments': ''
    }
    for article in app_data['articles']:
        if article['id'] == article_id:
            article_info = article
            article_info['author'] = get_author_info(article_info['author'], app_data)
            article_info['comments'] = get_comments(article_info['comments'], app_data)

    return {
        'id': article_info['id'],
        'author': article_info['author'],
        'title': article_info['title'],
        'text': article_info['text'],
        'comments': article_info['comments']
    }

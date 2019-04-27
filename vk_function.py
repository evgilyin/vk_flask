import vk_api
import settings

def get_data(group_url):
    login, password = settings.LOGIN, settings.PASSWORD
    vk_session = vk_api.VkApi(login, password)
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    tools = vk_api.VkTools(vk_session)
    group_link = group_url
    vk = vk_session.get_api()

    if 'https://vk.com/' in group_link:
        if group_link[:21] == 'https://vk.com/public':
            group_data = -int(group_link[21:])
            posts_likes={}
            posts_comments={}
            group_id = group_data
            posts = tools.get_all('wall.get', 100, {'owner_id': group_id, 'filter': 'owner'})
            for elements in posts["items"]:
                post_id = elements.get("id")
                likes = elements.get("likes").get("count")
                comments = elements.get("comments").get("count")
                posts_likes.update({f'https://vk.com/wall{group_id}_{post_id}':likes})
                posts_comments.update({f'https://vk.com/wall{group_id}_{post_id}':comments})
            max_value = max(posts_likes.items(), key=lambda k: k[1])
            post = max_value[0]
            likes = max_value[1]
            max_comments = max(posts_comments.items(), key=lambda k: k[1])
            post_for_comments = max_comments[0]
            comments = max_comments[1]
            return str(f'Наибольшее количество лайков ({likes}) в посте {post}, наибольшее количество комментариев ({comments}) в посте {post_for_comments}')
        elif group_link[:19] == 'https://vk.com/club':
            group_data = -int(group_link[19:])
            posts_likes={}
            posts_comments={}
            group_id = group_data
            posts = tools.get_all('wall.get', 100, {'owner_id': group_id, 'filter': 'owner'})
            for elements in posts["items"]:
                post_id = elements.get("id")
                likes = elements.get("likes").get("count")
                comments = elements.get("comments").get("count")
                posts_likes.update({f'https://vk.com/wall{group_id}_{post_id}':likes})
                posts_comments.update({f'https://vk.com/wall{group_id}_{post_id}':comments})
            max_value = max(posts_likes.items(), key=lambda k: k[1])
            post = max_value[0]
            likes = max_value[1]
            max_comments = max(posts_comments.items(), key=lambda k: k[1])
            post_for_comments = max_comments[0]
            comments = max_comments[1]            
            return str(f'Наибольшее количество лайков ({likes}) в посте {post}, наибольшее количество комментариев ({comments}) в посте {post_for_comments}')          
        else:
            group_data = vk.groups.getById(group_id=group_link[15:])
            for elements in group_data:
                group_data = -int(elements.get("id"))
                posts_likes={}
                posts_comments={}
                group_id = group_data
                posts = tools.get_all('wall.get', 100, {'owner_id': group_id, 'filter': 'owner'})
                for elements in posts["items"]:
                    post_id = elements.get("id")
                    likes = elements.get("likes").get("count")
                    comments = elements.get("comments").get("count")
                    posts_likes.update({f'https://vk.com/wall{group_id}_{post_id}':likes})
                    posts_comments.update({f'https://vk.com/wall{group_id}_{post_id}':comments})
                max_value = max(posts_likes.items(), key=lambda k: k[1])
                post = max_value[0]
                likes = max_value[1]
                max_comments = max(posts_comments.items(), key=lambda k: k[1])
                post_for_comments = max_comments[0]
                comments = max_comments[1]            
                return str(f'Наибольшее количество лайков ({likes}) в посте {post}, наибольшее количество комментариев ({comments}) в посте {post_for_comments}')
    else:
        a = 'Некорректный ввод. Пожалуйста, введите ссылку на сообщество в следующем формате: https://vk.com/...:' 
        return a

if __name__ == "__main__":
    main()


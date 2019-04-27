import vk_api
import settings

def get_name(group_url):
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
            group_data = int(group_link[21:])
            group_info = vk.groups.getById(group_id=group_data)
            name = group_info[0]['name']
            return name
        elif group_link[:19] == 'https://vk.com/club':
            group_data = int(group_link[19:])
            group_info = vk.groups.getById(group_id=group_data)
            name = group_info[0]['name']
            return name
        else:
            group_data = vk.groups.getById(group_id=group_link[15:])
            for elements in group_data:
                group_data = int(elements.get("id"))
            group_info = vk.groups.getById(group_id=group_data)
            name = group_info[0]['name']
            return name
    else:
        a = 'Некорректный ввод. Пожалуйста, введите ссылку на сообщество в следующем формате: https://vk.com/...:' 
        return a



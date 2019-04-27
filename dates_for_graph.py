import vk_api
import settings
from datetime import datetime
from collections import OrderedDict


def dates_for_graph(group_url):
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
            dates = []
            group_id = group_data
            posts = tools.get_all('wall.get', 100, {'owner_id': group_id, 'filter': 'owner'})
            for elements in posts["items"]:
                a = datetime.fromtimestamp(elements.get("date")).strftime('%Y')
                dates.append(a)
            years_dict = {}
            for date in dates:
                years_dict[date] = years_dict.get(date, 0) + 1
            return OrderedDict(sorted(years_dict.items(), key=lambda t: t[0]))
        elif group_link[:19] == 'https://vk.com/club':
            group_data = -int(group_link[19:])
            dates = []
            group_id = group_data
            posts = tools.get_all('wall.get', 100, {'owner_id': group_id, 'filter': 'owner'})
            for elements in posts["items"]:
                a = datetime.fromtimestamp(elements.get("date")).strftime('%Y')
                dates.append(a)
            years_dict = {}
            for date in dates:
                years_dict[date] = years_dict.get(date, 0) + 1
            return OrderedDict(sorted(years_dict.items(), key=lambda t: t[0]))
        else:
            group_data = vk.groups.getById(group_id=group_link[15:])
            for elements in group_data:
                group_data = -int(elements.get("id"))
            dates = []
            group_id = group_data
            posts = tools.get_all('wall.get', 100, {'owner_id': group_id, 'filter': 'owner'})
            for elements in posts["items"]:
                a = datetime.fromtimestamp(elements.get("date")).strftime('%Y')
                dates.append(a)
            years_dict = {}
            for date in dates:
                years_dict[date] = years_dict.get(date, 0) + 1
            return OrderedDict(sorted(years_dict.items(), key=lambda t: t[0]))
    else:
        a = 'Некорректный ввод. Пожалуйста, введите ссылку на сообщество в следующем формате: https://vk.com/...:' 
        return a






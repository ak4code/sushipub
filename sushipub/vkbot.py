import vk_api
from vk_api.utils import get_random_id
from decouple import config
from django.template.loader import get_template

vk_session = vk_api.VkApi(token=config('VK_API_KEY'))

vk = vk_session.get_api()


def notify_manager_vk(instance, user_id=456349964):
    template = get_template('notifications/notify_vk_message.txt')
    msg = template.render({'order': instance})
    vk.messages.send(
        user_id=user_id,
        random_id=get_random_id(),
        message=msg
    )

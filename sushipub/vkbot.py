import vk_api
from vk_api.utils import get_random_id
from decouple import config

vk_session = vk_api.VkApi(token=config('VK_API_KEY'))

vk = vk_session.get_api()

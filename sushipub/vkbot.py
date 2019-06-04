import vk_api
from vk_api.utils import get_random_id
from decouple import config

vk_session = vk_api.VkApi(token=config('VK_API_KEY'))

vk = vk_session.get_api()


def notify_manager_vk(instance, user_id=456349964):
    inputs = ['%s' % (item) for item in instance.items.all()]
    items = '\n'.join(inputs)
    total = instance.total()
    message = f'Новый заказ! \n' \
        f'Имя: {instance.name}\n' \
        f'Телефон: {instance.phone}\n' \
        f'Район доставки: {instance.area.name}\n' \
        f'Адрес: {instance.address}\n' \
        f'Кол-во персон: {instance.person}\n' \
        f'Комментарий: {instance.comment}\n' \
        f'-----------------------\n' \
        f'Заказ: \n{items}\n' \
        f'-----------------------\n' \
        f'Сумма: {total}'
    vk.messages.send(
        user_id=user_id,
        random_id=get_random_id(),
        message=message
    )

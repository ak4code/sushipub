from rest_framework import permissions

class ClientAppPermission(permissions.BasePermission):
    """
    Global permission check for client app.
    """
    message = 'Доступ для сторонних клиентов закрыт.'

    def has_permission(self, request, view):
        try:
            return request.META['HTTP_CLIENT_APP'] == 'sushipub'
        except KeyError as error:
            print(error)
            return False

from rest_framework import permissions


class ClientAppPermission(permissions.BasePermission):
    """
    Global permission check for client app.
    """
    message = 'Доступ для сторонних клиентов закрыт.'

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            try:
                return request.META['HTTP_CLIENT_APP'] == 'sushipub'
            except KeyError as error:
                return False
        else:
            try:
                return request.META['HTTP_CLIENT_APP'] == 'sushipub'
            except KeyError as error:
                return False

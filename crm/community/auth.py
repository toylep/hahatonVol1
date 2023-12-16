from rest_framework.permissions import BasePermission
from community.models import MySession

class SessionPermition(BasePermission):
    
    def has_permission(self, request, view):
        cookie = request.COOKIES['session_id']
        session = MySession.objects.filter(session_id=cookie)
        if len(session)!=0:
            return True
        else:
            return False

#!/usr/bin/env python3
"""
Session auth class
"""

import uuid
from api.v1.auth.auth import Auth
from models.user import User


class SessionAuth(Auth):
    """ Session auth class"""

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ create session
        """
        if user_id is None or type(user_id) != str:
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ user id for session id
        """
        if session_id is None or type(session_id) != str:
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """ current user
        """
        cookie = self.session_cookie(request)
        user_id = self.user_id_for_session_id(cookie)
        return User.get(user_id)

    def destroy_session(self, request=None):
        """ destroy session
        """
        if request is None:
            return False
        cookie = self.session_cookie(request)
        if cookie is None:
            return False
        user_id = self.user_id_for_session_id(cookie)
        if user_id is None:
            return False
        del self.user_id_by_session_id[cookie]
        return True

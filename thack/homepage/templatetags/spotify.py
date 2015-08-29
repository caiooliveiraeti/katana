import spotipy
from django import template

register = template.Library()


@register.filter(name='spotify')
def spotify(user):
    try:
        social_user = user.social_auth.get(provider='spotify')
    except user.DoesNotExist:
        return ''

    class SpotifyUser(object):
        def __init__(self, user):
            self.user = user
            self.api = spotipy.Spotify(auth=social_user.access_token)
            self._me = self.api.me()
            self._pl = self.api.user_playlists(self._me['id'])

        def me(self):
            return self._me

        def playlists(self):
            return self._pl

    return SpotifyUser(user)


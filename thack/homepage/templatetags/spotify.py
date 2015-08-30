import spotipy
from django import template

register = template.Library()


@register.filter(name='spotify')
def spotify(user):
    if not user.is_authenticated():
        return None

    try:
        social_user = user.social_auth.get(provider='spotify')
    except user.DoesNotExist:
        return None

    class SpotifyUser(object):
        def __init__(self, user):
            self.user = user
            self.api = spotipy.Spotify(auth=social_user.access_token)
            self._me = self.api.me()
            self._playlists = self.api.user_playlists(self._me['id'])
            self._followed = self.api.current_user_followed_artists();

        def me(self):
            return self._me

        def playlists(self):
            return self._playlists

        def followed_lists(self):
            return self._followed

    return SpotifyUser(user)


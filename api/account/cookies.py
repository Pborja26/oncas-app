from django.conf import settings

def set_auth_cookies(response, access, refresh=None):
    cookie = settings.JWT_COOKIE
    jwt = settings.SIMPLE_JWT
    response.set_cookie(
        cookie["ACCESS"], access,
        max_age=int(jwt["ACCESS_TOKEN_LIFETIME"].total_seconds()),
        httponly=True, secure=cookie["SECURE"], samesite=cookie["SAMESITE"], path="/"
    )
    if refresh:
        response.set_cookie(
            cookie["REFRESH"], refresh,
            max_age=int(jwt["REFRESH_TOKEN_LIFETIME"].total_seconds()),
            httponly=True, secure=cookie["SECURE"], samesite=cookie["SAMESITE"], path=cookie["REFRESH_PATH"],
        )

def delete_auth_cookies(response):
    cookie = settings.JWT_COOKIE
    response.delete_cookie(cookie["ACCESS"], path="/", samesite=cookie["SAMESITE"])
    response.delete_cookie(cookie["REFRESH"], path=cookie["REFRESH_PATH"], samesite=cookie["SAMESITE"])

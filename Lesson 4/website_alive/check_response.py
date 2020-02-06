from website_alive.make_request import request


def site_response(a):
    if request(a).status_code == 200:
        return True
    else:
        return False

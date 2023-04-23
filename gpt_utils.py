# write a function that checks status code from requests and returns status code with tex
def check_status_code(response):
    if response.status_code == 200:
        return response.status_code, "Success"
    else:
        return response.status_code, "Something went wrong"
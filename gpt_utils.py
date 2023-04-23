# write a function that checks status code from requests and returns status code with tex
def check_status_code(response):
    if response.status_code == 200:
        return response.status_code, "Success"
    else:
        return response.status_code, " Something went wrong"

def check_response(response):
    if response.json():
        return response.json()['choices'][0]['text']
    else:
        return "Something went wrong"
def get_text(response):
    #check if response is a valid json object
    if response.json():
        #return the text of the first choice
        return response.json()['choices'][0]['text']

# write a function that checks status code from requests and returns status code with text. please consider 2xx as success and anything else aas error
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

#write a function that checks status code from requests and returns status code with text. please consider 2xx as success and anything else aas error
def check_status_code(response):
    #check if status code starts with 2 and has 3 digits
    if str(response.status_code).startswith('2') and len(str(response.status_code)) == 3:
        return response.status_code, "Success"
    else: #return status code and error message that comes from the server
        return response.status_code, response.json()['error']


#check if response contains json object and if yes returns true, otherwise false
def check_json(response):
    if response.json():
        return True
    else:
        return False





import json
 
# Opening JSON file
def convert():
    with open('/home/ec2-user/environment/glassdoor-app/python_library/tech-companies.json') as json_file:
        data = json.load(json_file)
        for dic in data:
            url = str(dic['Name'])
            url2 = url.lower()
            url3 = url2.replace(" ", "")
            print(url3 + '.com/careers')

print(convert())
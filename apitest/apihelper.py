import requests
import json
import os


class Apihelper:


    def __init__(self):
        self.api = "https://swapi.co/api/people"
        self.character_data = {}



    def star_wars_characters(self, page_nr):
        # Get name,height and gender for each character
        return (page_nr['name'],page_nr['height'],page_nr['gender'])


    def append_to_file(self, filepath,name,height,gender):
        with open(filepath, "a")as f:
                f.write(",".join([name,height,gender]))
                f.write("\n")

    def get_results(self):
        response = requests.get(url=self.api)
        results = response.json()
        count = len(response.json()['results'])
        # get all characters in json
        page_nr_data_list = []
        for i in range(1,count):
            newapi = self.api+"/?page="+str(i)
            newresponse = requests.get(url=newapi)

            for item in newresponse.json()['results']:
                page_nr_data_list.append(self.star_wars_characters(item))
                self.append_to_file(os.getcwd()+"\\data.txt",item['name'].encode('utf-8'),item['height'].encode('utf-8'),item['gender'].encode('utf-8'))
        return page_nr_data_list




# if __name__ == '__main__':
#     x = Apihelper()
#     page_nr_data_list = x.get_results()
#     for item in page_nr_data_list:
#         x.append_to_file(os.getcwd()+"\\data.txt",item[0],item[1],item[2])

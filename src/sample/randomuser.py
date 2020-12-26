import requests, json

class User:
    def getUser(self):
        return json.loads(requests.get('https://randomuser.me/api/').content)

    def getUsers(self, n):
        return json.loads(requests.get('https://randomuser.me/api/?results='+str(n)).content)

    def getBySeed(self, seed):
        return json.loads(requests.get('https://randomuser.me/api/?seed='+seed).content)

    def getByNation(self, nation):
        return json.loads(requests.get('https://randomuser.me/api/?nat='+nation).content)

    def getWithOpt(self, array):
        temp = ''

        for i in array:
            if temp == '':
                temp += i
            else:
                temp+= ','+i 

        return json.loads(requests.get('https://randomuser.me/api/?inc='+temp).content)
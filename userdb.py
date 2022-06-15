from asyncio.windows_events import NULL
import json
from config import DATABASE


class User:
    def __init__(self, id, name, password):
        self.id = str(id)
        self.name = name
        self.password = password

class Users:
    def __init__(self, list):
        data_file = open(DATABASE, 'r')
        array = data_file.read()
        data = json.loads(array)
        data_file.close()
        self.list = data['users']

    def Save(self):
        data_file = open(DATABASE, 'w')
        jsonStr = '{ "users": ' + json.dumps(self.list, default = lambda x: x.__dict__) + '}'
        data_file.write(jsonStr)
        data_file.close()

    def getUser(self, id):
        id = str(id)
        for u in self.list:
            if (type(u) is User):
                if u.id == id:
                    return u
            else:
                if u['id'] == id:
                    return User(u['id'], u['name'], u['password']) 

    def updateUser(self, user):
        id = user.id
        for i, u in enumerate(self.list):
            if (type(u) is User):
                if u.id == id:
                    self.list[i] = user
                    return
            else:   
                if u['id'] == id:

                    self.list[i] = user
                    return

    def insertUser(self, user):
        self.list.append(user)

    def deleteUser(self, id):
        uid = str(id)
        for i, u in enumerate(self.list):
            if (type(u) is User):
                if u.id == uid:
                    self.list.pop(i)
                    return
            else:
                if u['id'] == uid:
                    self.list.pop(i)
                    return

userDB = Users([])


u = userDB.getUser(2)
u.password = '22244222222'
u.name = 'ilia'
userDB.updateUser(u)


u = userDB.getUser(2)
u.password = '223332444444222222'
u.name = 'il423344ia'
userDB.updateUser(u)

userDB.deleteUser(1)
userDB.deleteUser(4)
userDB.Save()


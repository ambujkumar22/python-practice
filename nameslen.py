users = []
for i in range(5):
        names = input('Type the names of 5 users: ')
        users.append(names)
print(users)
def find():
        more = 0
        less = 0
        for j in users:
                if len(j) > 5:
                        more += 1
                else:
                        less += 1
        return more,less

more,less = find()
print('The users with the names more than 5 characters is {} and less than or equals to 5 characters is {}'.format(more,less))
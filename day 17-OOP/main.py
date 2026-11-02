# Class name should be PascalCase
# Object class naming should be snake_case

class User:
    # Constructor
    # def __init__(self):
    #     print("New user has been created.")

    def __init__(self, user_id, username, followers, following):
        self.id = user_id
        self.name = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1 

# user_one = User()
# user_one.id = "001"
# user_one.name = "John"

# print(user_one.name)

user_two = User("002", "Don", 0, 0)
user_three = User("003", "Sam", 0, 0)
print(user_two.id) # 002
print(user_three.followers) # 0

print("===================")

user_two.follow(user_three)

print(user_two.followers)
print(user_two.following)

print(user_three.followers)
print(user_three.following)

print("===================")

def function():
    pass

print("Hello")

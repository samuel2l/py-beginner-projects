# class Car:
#     pass
# car=Car()
# car.wheels=4
# print(car.wheels)
# car1=Car()
class User:
    def __init__(self,username,id):
        self.user_id=id
        self.username=username
        self.followers=0
        self.following = 0
    def follow(self,other_user):
        self.following+=1
    #person will have number of people following increase by one
# the person being followed will have followers inc by one
        other_user.followers+=1
user1= User('01','kri_hu')
user2= User('02','kyo_hr')
user1.follow(user2)
print(user2.followers)
print(user1.following)



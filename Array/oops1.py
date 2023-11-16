class Youtube:
    def __init__(self,username,subscribers=0,subscription=0):
        self.username=username
        self.subscribers=subscribers
        self.subscription=subscription
    def subscribe(self,user):
        user.subscribers+=1
        self.subscription+=1
    def unsubscribe(self,user):
        user.subscribers-=1
        self.subscription-=1
user1=Youtube('neeraj')
user2=Youtube('sonu')
print(f"{user1.username}'s subscribers are {user1.subscribers}")
print(user1.subscription)
print(user2.subscribers)
print(user2.subscription)
print()
user1.subscribe(user2)
print(user1.subscribers)
print(user1.subscription)
print(user2.subscribers)
print(user2.subscription)
user1.unsubscribe(user2)
print()
print(user1.subscribers)
print(user1.subscription)
print(user2.subscribers)
print(user2.subscription)
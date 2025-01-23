class Student:
    def learn(self):
        print('Inside the learn')
        print(self.name,'is learning')
    def play(self):
       print('Inside play Method') #takes 0 positional arguments but 1 was given

s1 = Student()

s1.name='RAM'
s1.learn()
s1.play()

print('name is',s1.name)

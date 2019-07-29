from my01_class import Myclass

me = Myclass()

if me.sex == '男':
    print ('My name is %s, I am a boy.' % me.name)
elif me.sex == '女':
    print ('My name is %s, I am a girl.' % me.name)
else:
    print ('My name is %s, I am a ...' % me.name)

me.work()
me.study()

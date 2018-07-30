class Singleton(object):
    ans = None

    @staticmethod
    def instance():
        ''' we do not instantiate instances of Singleton class we just use this static method to allow access'''
        if '_instance' not in Singleton.__dict__:
            Singleton._instance = Singleton()
            # this is how we ensure we only have one instance by doing reflection
        return Singleton._instance


s1 = Singleton.instance()
s2 = Singleton.instance()

assert s1 is s2
s1.ans = 42 #hilarious I just fucking love python nerdy shit

assert s2.ans == s1.ans
print("assertions all passed")
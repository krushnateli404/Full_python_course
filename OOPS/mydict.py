class exercise_dict:
    def __init__(self,d):
        self.d = d
        
    def get_keys(self):
        """This fuction gives the all the key of dictinory"""
        if type(self.d) == dict:
            return self.d.keys()
        
    def get_values(self):
        """This fuction gives the all the values of dictinory"""
        """"""
        if type(self.d) == dict:
            return self.d.values()
        
    def get_exception(self):
        """This fuction gives exception if the given input is not dictinory"""
        """"""
        try:
            if type(self.d) == dict:
                return self.d
        except Exception as e:
            print("The given input is not dictionary: ",e)
        else:
            print("The given input is not dictionary")
        
    def get_add_key_value(self,key,value):
        """This fuction adds the key-value pair"""
        """"""
        if type(self.d) == dict:
            self.d[key] = value
            print(self.d)
            
    def get_dict(self):
        """This fuction gives the all the items of dictinory"""
        """"""
        if type(self.d) == dict:
            return self.d.items()
            
    def create_own_except(self):
        if type(self.d) != dict:
            raise Exception(self.d,"The given input is not dictionary")
            
            
    def userinput(self):
        self.a = eval(input())
        print(self.a.keys())
        print(self.a.values())
    
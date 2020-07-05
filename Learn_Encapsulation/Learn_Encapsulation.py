class testleaf:

    mentors = ['B', 'G', 'B', 'S']
    ph_tr  = '044565656'
    __ATM = '1234'

    def get_phone_num(self):
        return testleaf.__ATM

    @classmethod
    def __private_impl(cls): # class methods, static methods , instance methods
        return 100

    def get_imple(self):
        return testleaf.__private_impl()

    def set_atm_pin(self, val):
        testleaf.__ATM = val


per1 = testleaf()
print(per1.get_phone_num())    # data hidding
print(per1.get_imple())        # iml hidding

per1.set_atm_pin(7878)
print(per1.get_phone_num())    # data hidding




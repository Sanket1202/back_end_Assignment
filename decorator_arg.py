def role_base_access(lis):
    def deco(func):
        def inner(*args,**kwargs):
            user_input = input("enter the input:")

            if user_input in lis:
                print("It is accessible...")
                return func(*args,**kwargs)
            else:
                print("Its not accessible!!,Only admins can access")

        return inner

    return deco


class Access:
    @role_base_access(['admin', 'name', '161119'])
    def ordinary(self):
        print("Here that you can access:")
        details = [
            {
                "name": "Shiv",
                "role": "Developer",
                "salary": 500000
            },
            {
                "name": "Sank",
                "role": "Backend",
                "salary": 900000
            },
            {
                "name": "Sam",
                "role": "Frontend",
                "salary": 1000000
            }
        ]
        for i in details:
            print(i)


obj = Access()
obj.ordinary()

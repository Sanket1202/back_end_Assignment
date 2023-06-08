def role_base_access(func):
    User = ["Admin", "Sanket", "161119"]

    def inner(*args, **kwargs):
        user_input = input("enter the input:")
        if user_input in User:
            print("It is accessible...")
            return func(*args, **kwargs)
        else:
            print("Its not accessible!!,Only Admin can access")

    return inner


# class access: we can also create class
@role_base_access
def ordinary():
    print("Here that you can access:")
    Details = [
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
    for i in Details:
        print(i)
'''obj = access()
obj.ordinary()'''
ordinary()

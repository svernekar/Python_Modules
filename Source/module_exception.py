try:
    f=open('os.log')
    x=y+10
    if x >= 10:
        raise Exception
    print('Check if execution occurs')
except (FileNotFoundError,NameError) as e:
    print(e)
except Exception as e:
    print("Not a valid value for x")
else:
    print("No exception")
finally:
    print("Iam always there")

#This shoudld be on master
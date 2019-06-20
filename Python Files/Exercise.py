'''
prompt user to enter data and concurrent users
determine if the bandwidth is sufficient
'''
def calculate(data, users):
    bandwidth = data * users
    print("Total bandwidth required: {:.2f} MBps".format(bandwidth))
    if bandwidth > 125:
        sufficient = "False"
    else:
        sufficient = "True"
    print("1Gbps bandwidth sufficient {}?".format(sufficient))
        

data = float(input("Enter amount of data (MB) required per second: "))
users = float(input("Enter number of concurrent users: "))
calculate(data, users)
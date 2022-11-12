from faker import Faker
from faker.providers import *
fake = Faker()  # initialise faker module


# use this function to create a dataframe containing n number of fake usernames using the faker module
def create_data_faker(num=1):
    output = [{
        "Negotiating Users": fake.simple_profile()['username']
    }
        for x in range(num)
    ]
    return output

# check_columns, check_rows, and create_access_granting functions can be used as an alternate way to determine negotiating users and creating an access granting vector matrix


def check_columns(board):
    for column in board:
        if len(set(column)) == 1 and column[0] is not None:
            return column[0]


def check_rows(board):
    return check_columns(zip(*reversed(board)))


def create_access_granting(name, i, df_target):
    z = 0
    v = [[], [], []]
    for y in name['Negotiating Users']:
        print("this is y:", y)
        for x in df_target['Negotiating Users']:
            print("this is x:", x)
            if(x == y):
                v[i].append(0)
            else:
                v[i].append(1)
        z = z+1
    print(v)
#   v = np.array(v)
    print(check_rows(v))
    return v


# use this function to calculate PR and SL for any given negotiating users
def calculate_pr_sl(beta, sensi, alpha, lambd=0.5):
    PR = 0
    for (i, j) in zip(beta, sensi):
        PR = PR+(i*j) * alpha  # calculating privacy risk
    print("PR:", PR)

    SL = 0
    for(i, j) in zip(beta, sensi):
        SL = SL+((1-i)*(1-j) * alpha)  # calculating sharing loss
    print("SL:", SL)
    sum = 0
    for i in sensi:
        sum = sum+i
    # lambd = 0.209725  # try different values for lambda to see a difference in results
    lambd = 0.5  # 0.5 gives an equal weightage for privacy risk and sharing loss
    # print(lambd*PR) # print values to identify whether imp of privacy risk is higher
    # print((1-lambd)*SL) # or sharing loss
    if(lambd*PR > ((1-lambd)*SL)):  # conflict resolution
        return "DENY"
    else:
        return "PERMIT"

# use this function to calculate PR and SL for any given negotiating users


def return_pr_sl(beta, sensi, alpha, lambd=0.5):
    PR = 0
    for (i, j) in zip(beta, sensi):
        PR = PR+(i*j) * alpha  # calculating privacy risk
    print("PR:", PR)

    SL = 0
    for(i, j) in zip(beta, sensi):
        SL = SL+((1-i)*(1-j) * alpha)  # calculating sharing loss
    print("SL:", SL)
    sum = 0
    for i in sensi:
        sum = sum+i
    # lambd = 0.209725  # try different values for lambda to see a difference in results
    lambd = 0.5  # 0.5 gives an equal weightage for privacy risk and sharing loss
    # print(lambd*PR) # print values to identify whether imp of privacy risk is higher
    # print((1-lambd)*SL) # or sharing loss
    
    return PR, SL

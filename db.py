from tinydb import TinyDB, Query

db = TinyDB('users.json', indent=4)
users = db.table('users')


def get_user_by_document_id(document_id):
    q = Query()
     

def get_user_by_first_name(first_name):
    q = Query()
    return users.search(q.first_name == first_name)

def get_users_by_country(country):
    q = Query()
    return users.search(q.country == country)

def get_users_by_city(city):
    q = Query()
    return users.search(q.city == city)

def get_users_by_age(age):
    q = Query()
    return users.search(q.age == age)

def get_users_by_in_range_age(min_age, max_age):
    q = Query()
    return users.search((q.age == min_age) & (q.age == max_age))

def get_all_full_names():
 # ['John Doe', 'Jane Doe', 'John Smith', ...]
    a=[]
    
    q= users.all()

    for i in q:
        a.append(i["first_name"])
        a.append(i["last_name"])
    return a

        
def get_all_countries():
     # ['USA', 'Canada', 'Mexico', ...]
    a=[]
    
    q= users.all()

    for i in q:
        a.append(i["country"])
    return a

def get_all_cities():
     # ['New York', 'Los Angeles', 'Chicago', ...]
    a=[]
    
    q= users.all()

    for i in q:
        a.append(i["city"])
    return a

def get_all_emails():
     # ['john.doe@example', 'jane.doe@example', ...]a=[]
    a=[]
    q= users.all()

    for i in q:
        a.append(i["email"])
    return a

def delete_user_by_document_id(document_id):
    pass

def delete_user_by_first_name(first_name):
    q = Query()
    return users.remove(q.first_name == first_name)


def delete_users_by_country(country):
    q = Query()
    return users.remove(q.counttry==country)

def delete_users_by_city(city):
    q = Query()
    return users.remove(q.city == city)

def delete_users_by_age(age):
    q = Query()
    return users.remove(q.age == age)

def delete_users_by_in_range_age(min_age, max_age):
    q = Query()
    return users.remove((q.age == min_age) & (q.age == max_age))

def delete_all_users():
    pass

# print(get_user_by_document_id(6))
# print(get_user_by_first_name("Victor"))
# print(get_users_by_country("Spain"))
# print(get_users_by_city("Filderstadt"))
# print(get_users_by_age(44))
# print(get_users_by_in_range_age(22 , 66))
print(get_all_full_names())
# print(get_all_countries())
# print(get_all_cities())
# print(get_all_emails())
# print(delete_user_by_document_id("10"))
# print(delete_user_by_first_name("Carmen"))
# print(delete_users_by_country("Ukraine"))
# print(delete_users_by_city("Roskilde"))
# print(delete_users_by_age(77))
# print(delete_users_by_in_range_age(55 , 88))
# print(delete_all_users())
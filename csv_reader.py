from csv import writer, reader, DictReader


# def add_user(first, last):
#     with open("users.csv.txt", 'a') as file:
#         csv_writer = writer(file)
#         csv_writer.writerow([first, last])


# add_user("Nasim", "Rajabi")
# add_user("Abbas", "Rajabi")
# add_user("Mahboobeh", "Rajabi")
##############################################################
# def print_users():
#     with open("users.csv") as file:
#         csv_reader = DictReader(file)
#         next(csv_reader)
#         for i in csv_reader:
#             print(i['Name'], i["Country"])


# print_users()

################################################################
def find_user(name, family):
    index = 0
    with open("users.csv") as file:
        csv_reader = DictReader(file)
        for i in csv_reader:
            index += 1
            if i['Name'] == name and i['Family'] == family:
                print(index)


find_user("Nasim", "Rajabi")

from csv import writer


def add_user(first, last):
    with open("users.csv.txt", 'a') as file:
        csv_writer = writer(file)
        csv_writer.writerow([first, last])


add_user("Nasim", "Rajabi")
add_user("Abbas", "Rajabi")
add_user("Mahboobeh", "Rajabi")
##############################################################

import re
# pattern = re.compile(r'\d{3} \d{3}-\d{4}')
# res = pattern.search('call me at 415 555-4242!')
# print(res.group())

##########################################################
# def is_valid_time(str):
#     pattern = re.compile(r'^\d\d?:\d\d$')
#     if pattern.search(str):
#         return True
#     else:
#         return False


# print(is_valid_time("44:55"))
# print(is_valid_time("12:55"))
# print(is_valid_time("4e4:55"))
# print(is_valid_time("44:550"))
# print(is_valid_time("44:sdj55"))


#########################################################


# def parse_bytes(str):
#     pattern = re.compile(r'\b[10]{8}\b')
#     x = pattern.findall(str)
#     return x


# print(parse_bytes('10101101  11011111'))


##########################################################
# def parse_date(str):
#     regex = re.compile(
#         r'^([0-3]\d)([.,\/])([01]\d)([.,\/])(1\d\d\d)$')
#     result = regex.findall(str)
#     return {'d': result[0][0], 'm': result[0][2], "y": result[0][4]}


# print(parse_date('30/12/1390'))


##########################################################

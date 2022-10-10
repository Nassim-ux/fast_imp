from datetime import datetime
import re


o = "couleur 1"
_m = re.findall( r'\ ([a-zA-Z0-9]+)', o.lower())
print(_m)
# opt = "[couleur oui][recto-verso oui][copies 1][livraison non]"
# # opt = opt[1:-1]
# # c = opt.split('][')
# match = re.findall( r'(?<=\[)(.*?)(?=\])',opt)
# # match = re.search(r"(?<=\[).+?(?=\])",opt)
# print(match)


# mydate = "29Sep2022125456"
# # mydate = mydate[4:]
# othdate = "28Sep2022202651"
# # othdate = othdate[4:]

# mydate_object = datetime.strptime(mydate, "%d%b%Y%H%M%S")
# othdate_object = datetime.strptime(othdate, "%d%b%Y%H%M%S")

# print(mydate_object < othdate_object)

# m = "[Demande de confirmation][n° 1838919bbe01666f] Service d'impression en ligne"
# m = m[25:]
# match = re.search(r"°.+?]", m)
# m = match.group()
# m = m[2:-1]
# print(m)
# m = 'nor.eply@lyfpedia.com'
# match = re.search(r"@.+?[.]", m)
# _to = match.group()
# _to = _to[1:-1]
# print(_to)

# date_string = "Tue,27Sep2022203941"
# date_string = date_string[4:]
# print("date_string =", date_string)

# date_object = datetime.strptime(date_string, "%d%b%Y%H%M%S")
# print("date_object =", date_object)

# date_string2 = "Tue,27Sep2022213941"
# date_string2 = date_string2[4:]
# print("date_string =", date_string2)

# date_object2 = datetime.strptime(date_string2, "%d%b%Y%H%M%S")
# print("date_object =", date_object2)

# print(date_object == date_object2)


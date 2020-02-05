import protogen.person_pb2 as person_pb2

person = person_pb2.Person()


# scalar values
person.id = 123
person.name = "Akash"
person.age = 26


# array values
person.languages_known.append("English")
person.languages_known.append("Spanish")


# enum values
person.gender = person_pb2.Male


# nested message values
person.address.city = "Bangalore"
person.address.state = "Karnataka"
person.address.country = "India"
person.address.pincode = 560035


# print message
print(person)
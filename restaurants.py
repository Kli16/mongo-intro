from pymongo import MongoClient

connection = MongoClient('homer.stuy.edu')
db = connection.test
collection = db.restaurants

#All restaurants in a specified borough.
def get_borough(borough):
    return collection.find( {'borough': borough} )

#All restaurants in a specified zip code.
def get_zipcode(zipcode):
    return collection.find( {'address.zipcode': zipcode} )
#All restaurants in a specified zip code and with a specified grade.
def get_zip_grade(zipcode, grade):
    return collection.find( {'address.zipcode': zipcode, 'grades.grade': grade} )

#All restaurants in a specified zip code with a score below a specified threshold.
def get_zip_score(zipcode, score):
    return collection.find( {'address.zipcode': zipcode, 'grades.score': {'$lt': score} } )

#Something more clever.

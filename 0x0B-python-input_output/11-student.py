#!/usr/bin/python3
""" Defines a student by name and age """


class Student:
    """ Defines a Student """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        mydict = {}
        if type(attrs) is list:
            for attr in attrs:
                if type(attr) is not str:
                    return self.__dict__

                if attr in self.__dict__:
                    mydict[attr] = self.__dict__[attr]

            return mydict
        return self.__dict__

    def reload_from_json(self, json):
        for i in json:
            if i in self.__dict__.keys():
                self.__dict__[i] = json[i]

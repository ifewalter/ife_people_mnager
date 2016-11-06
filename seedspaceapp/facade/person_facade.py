from seedspaceapp.models import Person

__author__ = 'ife'

class PersonFacade():

    def __init__(self):
        pass

    @staticmethod
    def create_person(full_name, email_address):
        if full_name and email_address:
            person_model = Person()
            person_model.email_address = email_address
            person_model.full_name = full_name
            try:
                person_model.save()
                return True
            except ValueError as value_error:
                print value_error.message
            except Exception as e:
                print e.message
        return False


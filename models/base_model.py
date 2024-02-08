import uuid
import datetime

class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key is not '__class__':
                    setattr(self, key, value)
            if 'created_at' in kwargs:
                self.created_at = datetime.datetime.strptime(kwargs['created_at'], "%Y-%m-%dT%H:%M:%S.%f")        
            if 'updated_at' in kwargs:
                self.updated_at = datetime.datetime.strptime(kwargs['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.utcnow()
            self.updated_at = datetime.datetime.utcnow()
    def __str__(self):
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """ updates instance attributes with current datetime"""
        self.updated_at = datetime.datetime.utcnow()
    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

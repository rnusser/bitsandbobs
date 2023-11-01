from dataclasses import dataclass
import datetime
from marshmallow import Schema, fields, post_load


# The "model" of a User
@dataclass(frozen=True)
class User:
    name: fields.Str = None
    email: fields.Str = None
    created_at: datetime = datetime.datetime.now()


# The marshmallow shema for serialising and deserialising
class UserSchema(Schema):
    name = fields.Str(allow_none=True)
    email = fields.Email()
    created_at = fields.DateTime()

    @post_load
    def make_user(self, data, **kwargs):
        return User(**data)


user = User(name="Monty", email="monty@python.org")
print(user)  # User(name='Monty', email='monty@python.org', created_at=datetime.datetime(2023, 8, 3, 11, 5, 56, 848769))

# Serializing Objects (“Dumping”), in this case to a dictionary from an object - no validation is done for dump
schema = UserSchema()
result: dict = schema.dump(user)
json_result = schema.dumps(user)
print(result)  # {'name': 'Monty', 'email': 'monty@python.org', 'created_at': '2023-08-03T11:09:27.970114'}
print(json_result)  # {"name": "Monty", "email": "monty@python.org", "created_at": "2023-08-03T11:09:27.970114"}

result["name"] = None

# Deserialise our dictionary to get back to an object - validation can be added
object: User = UserSchema().load(result)
print(object)
# User(name='Monty', email='monty@python.org', created_at=datetime.datetime(2023, 8, 3, 11, 19, 49, 519289))

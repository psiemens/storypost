from django.db.models import Model, IntegerField, CharField, TextField

class List(Model):

    mc_list_id = IntegerField() # Mapped to MailChmip List instance
    title = CharField(max_length=255)
    description = TextField()



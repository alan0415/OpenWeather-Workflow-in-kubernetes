from django.db import models

# Create your models here.
class User_list(models.Model):
    def __str__(self):
        return self.subscribe_dataset_number
    
    user = models.TextField()
    email = models.TextField()
    subscribe_dataset_number = models.CharField(max_length=20)
    subscribe_city = models.CharField(max_length=20)
    api_token = models.CharField(max_length=255)
    last_modify_date = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "user_list"
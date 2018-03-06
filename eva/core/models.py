from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class MessagingService(BaseModel):
    name = models.CharField(max_length=100)


class User(BaseModel):
    first_name = models.CharField(max_length=100)


class Message(BaseModel):
    content = models.CharField(max_length=255)
    intent = models.CharField(max_length=50)
    received_at = models.DateField(auto_now_add=True)


class MessagingServiceUserIdentifier(BaseModel):
    messaging_service = models.ForeignKey(
        MessagingService, related_name="messaging_service_user_identifier", on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, related_name="messaging_service_user_identifier", on_delete=models.CASCADE)


class UserMessage(BaseModel):
    message = models.ForeignKey(
        Message, related_name="user_messages", on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, related_name="user_messages", on_delete=models.CASCADE)

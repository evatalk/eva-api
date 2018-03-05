from django.db import models


class MessagingService(models.Models):
    name = models.CharField(max_length=100)


class User(models.Models):
    first_name = models.CharField(max_length=100)


class Message(models.Models):
    content = models.CharField(max_length=255)
    intent = models.CharField(max_length=50)
    received_at = models.DateField(auto_now_add=True)


class MessagingServiceUserIdentifier(models.Models):
    messaging_service_id = models.ForeignKey(
        User, related_name="messaging_service_user_identifier")
    user_id = models.ForeignKey(
        User, related_name="messaging_service_user_identifier")


class UserMessage(models.Models):
    message_id = models.ForeignKey(Message, related_name="user_messages")
    user_id = models.ForeignKey(User, related_name="user_messages")

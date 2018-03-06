from django.db import models


class MessagingService(models.Model):
    name = models.CharField(max_length=100)


class User(models.Model):
    first_name = models.CharField(max_length=100)


class Message(models.Model):
    content = models.CharField(max_length=255)
    intent = models.CharField(max_length=50)
    received_at = models.DateField(auto_now_add=True)


class MessagingServiceUserIdentifier(models.Model):
    messaging_service = models.ForeignKey(
        MessagingService, related_name="messaging_service_user_identifier", on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, related_name="messaging_service_user_identifier", on_delete=models.CASCADE)


class UserMessage(models.Model):
    message = models.ForeignKey(
        Message, related_name="user_messages", on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, related_name="user_messages", on_delete=models.CASCADE)

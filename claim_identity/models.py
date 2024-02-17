from django.db import models
from django.contrib.auth.models import User
#from events.models import Event


STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts"
    )
    content = models.TextField(
        max_length=2000,
        help_text="Write your blog content here"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | written by {self.author}"

class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"

#class Ticket(models.Model):
#    ticket_holder = models.ForeignKey(
#        User,
#        on_delete=models.CASCADE,
#        related_name="users_tickets"
#    )
#    date_issued = models.DateTimeField(auto_now_add=True)
#    event = models.ForeignKey(
#        Event,
#        on_delete=models.CASCADE,
#        related_name="event_tickets"
#    )

    def __str__(self):
        return f"Ticket for {self.ticket_holder}"

# Models for MetaMask Integration
class UserWallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    wallet_address = models.CharField(max_length=255, unique=True)
    metamask_installed = models.BooleanField()

class Transaction(models.Model):
    transaction_id = models.CharField(max_length=255, primary_key=True)
    user = models.ForeignKey(UserWallet, on_delete=models.CASCADE)
    token_amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateTimeField()

class Claim(models.Model):
    claim_id = models.CharField(max_length=255, primary_key=True)
    user = models.ForeignKey(UserWallet, on_delete=models.CASCADE)
    successful = models.BooleanField()
    claim_date = models.DateTimeField()

class IdentityOwner(models.Model):
    owner_id = models.CharField(max_length=255, primary_key=True)
    is_claimed = models.BooleanField()

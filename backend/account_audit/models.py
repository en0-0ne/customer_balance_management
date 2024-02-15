from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _

# Create your models here.
class User(models.Model):

    USER_ROLES = {
        "user": "User",
        "customer": "Customer",
    }

    name = models.CharField(_("Name"), max_length=200)
    slug = models.SlugField(_("Slug"), null=True, blank=True)
    address = models.TextField(_("Address"))
    email = models.EmailField(_("Email"), max_length=100)
    phone = models.CharField(_("Phone"), max_length=50)

    login = models.EmailField(_("Login"), max_length=254)
    password = models.CharField(_("Password"), max_length=50)
    access_type = models.CharField(_("Access"), max_length=30, choices=USER_ROLES, default=USER_ROLES["customer"])
    

    class Meta:
        db_table = 'user'
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})


class Account(models.Model):

    account_no = models.CharField(_("Account No"), max_length=50)
    name = models.CharField(_("Name"), max_length=100)
    slug = models.SlugField(_("Slug"))
    balance = models.FloatField(_("Balance"))

    customer_id = models.ForeignKey("account_audit.User", verbose_name=_("Customer"), on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'account'
        ordering = ['-account_no']
        verbose_name = _("Account")
        verbose_name_plural = _("Accounts")

    def __str__(self):
        return f'{self.account_no} {self.name}'

    # def get_absolute_url(self):
    #     return reverse("Account_detail", kwargs={"pk": self.pk})


class Audit(models.Model):
    STATES = {
        "draft": "Draft",
        "valid": "Valid",
        "cancel": "Cancel",
    }

    reference = models.CharField(_("Reference"), max_length=50, unique=True)
    description = models.TextField(_("Description"))
    old_balance = models.FloatField(_("Old balance"))
    new_balance = models.FloatField(_("New balance"))
    state = models.CharField(_("State"), max_length=20, choices=STATES)

    account_ids = models.ManyToManyField("account_audit.Account", verbose_name=_("Accounts"))
    user_id = models.ForeignKey("account_audit.User", verbose_name=_("User"), on_delete=models.DO_NOTHING)
    customer_id = models.SmallIntegerField(_("Customer ID"))

    action = models.CharField(_("Action"), max_length=15)
    write_date = models.DateTimeField(_("Write date"), auto_now=True)
    write_id = models.SmallIntegerField(_("Write ID"))


    class Meta:
        db_table = 'audit'
        ordering = ['-write_date']
        verbose_name = _("Audit")
        verbose_name_plural = _("Audits")

    def __str__(self):
        return self.reference

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})

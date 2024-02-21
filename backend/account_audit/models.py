from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'[{self.user.id}] {self.user.username}'

class Account(models.Model):

    account_no = models.CharField(_("Account No"), max_length=50, null=True, blank=True)
    name = models.CharField(_("Name"), max_length=100)
    balance = models.FloatField(_("Balance"))

    # user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    profile = models.ForeignKey(
        "account_audit.UserProfile",
        verbose_name=_("Profile"),
        on_delete=models.DO_NOTHING,
        null=True
    )

    class Meta:
        db_table = 'account'
        ordering = ['-account_no']
        verbose_name = _("Account")
        verbose_name_plural = _("Accounts")

    def __str__(self):
        return f'{self.account_no} {self.name}'



class Audit(models.Model):
    STATES = {
        "draft": "Draft",
        "valid": "Valid",
        "cancel": "Cancel",
    }

    ACTIONS = {
        "INS": "Insert",
        "UPD": "Update",
        "DEL": "Delete",
    }

    reference = models.CharField(_("Reference"), max_length=50, unique=True)
    description = models.TextField(_("Description"))
    old_balance = models.FloatField(_("Old balance"))
    new_balance = models.FloatField(_("New balance"))
    state = models.CharField(_("State"), max_length=20, choices=STATES, default=STATES["draft"])

    account_ids = models.ManyToManyField("account_audit.Account", verbose_name=_("Accounts"))
    # user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    profile = models.ForeignKey(
        "account_audit.UserProfile",
        verbose_name=_("Profile"),
        on_delete=models.DO_NOTHING,
        null=True
    )
    customer_id = models.SmallIntegerField(_("Customer ID"))

    action = models.CharField(_("Action"), max_length=15, choices=ACTIONS)
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

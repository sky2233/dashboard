# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    demisto_id = models.IntegerField()
    comment_details = models.TextField(blank=True, null=True)
    comment_date = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comment'

class Internship(models.Model):
    demisto_id = models.AutoField(primary_key=True)
    ticket_title = models.TextField(blank=True, null=True)
    ticket_created = models.TextField(blank=True, null=True)
    ticket_priority = models.IntegerField(blank=True, null=True)
    ticket_priority2 = models.IntegerField(blank=True, null=True)
    ticket_status = models.TextField(blank=True, null=True)
    ticket_owner = models.TextField(blank=True, null=True)
    ticket_sourceip = models.TextField(db_column='ticket_sourceIP', blank=True, null=True)  # Field name made lowercase.
    ticket_details = models.TextField(blank=True, null=True)
    ticket_vib_owner = models.TextField(blank=True, null=True)
    ticket_id = models.IntegerField(blank=True, null=True)
    created_by = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'internship'
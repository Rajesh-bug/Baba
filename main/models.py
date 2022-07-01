from django.db import models

class GotraData(models.Model):
    gotra_name = models.CharField(max_length=50)
    # id = models.AutoField(unique=True)

    class Meta:
        managed = False
        db_table = 'gotra_data'


class WorkData(models.Model):
    # id = models.AutoField(unique=True)
    work_name = models.CharField(max_length=50)
    rate = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'work_data'


class Customerdata(models.Model):
    # id = models.AutoField(unique=True)
    account_name = models.CharField(unique=True, max_length=150)
    address = models.CharField(max_length=250, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    gotra = models.CharField(max_length=50, blank=True, null=True)
    code = models.CharField(max_length=50, blank=True, null=True)
    remarks = models.CharField(max_length=150, blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now_add=True)
    main_account = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=50,blank=True, null=True)
    series_no = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customerdata'


class SlipData(models.Model):
    # id = models.AutoField()
    series_no = models.CharField(max_length=50,blank=True, null=True,default=4)
    slip_no = models.CharField(max_length=50, blank=True, null=True, default=1)
    voucher_date = models.DateTimeField(auto_now_add=True)
    client_name = models.CharField(max_length=50, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    gotra = models.IntegerField(blank=True, null=True)
    work_type = models.IntegerField()
    amount = models.IntegerField()
    baba = models.IntegerField(blank=True, null=True)
    user_name = models.CharField(max_length=10)
    is_cancel = models.BooleanField(blank=True, null=True)
    counter = models.CharField(max_length=20, blank=True, null=True, default=1)
    slip_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'slip_data'
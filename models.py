# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CityData(models.Model):
    city = models.CharField(max_length=50)
    id = models.AutoField(unique=True)

    class Meta:
        managed = False
        db_table = 'City_Data'


class PrintSaleBill(models.Model):
    program = models.CharField(max_length=127)
    colm_n = models.CharField(max_length=127)
    selected = models.BooleanField(blank=True, null=True)
    lenth = models.IntegerField()
    width = models.IntegerField(blank=True, null=True)
    decimal = models.IntegerField(db_column='Decimal', blank=True, null=True)  # Field name made lowercase.
    cont = models.CharField(max_length=50, blank=True, null=True)
    fixed = models.BooleanField(db_column='Fixed', blank=True, null=True)  # Field name made lowercase.
    ordr = models.IntegerField()
    colid = models.AutoField()
    field_name = models.CharField(max_length=50, blank=True, null=True)
    no_store = models.BooleanField(blank=True, null=True)
    not_null = models.BooleanField(db_column='Not_null', blank=True, null=True)  # Field name made lowercase.
    auto_generation = models.CharField(db_column='Auto_generation', max_length=15, blank=True, null=True)  # Field name made lowercase.
    for_print = models.BooleanField(blank=True, null=True)
    horizontal_show = models.BooleanField(blank=True, null=True)
    custom_field = models.BooleanField(blank=True, null=True)
    total_field = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Print_sale_bill'


class AttributeSetting(models.Model):
    program = models.CharField(max_length=127)
    column = models.CharField(db_column='Column', max_length=127)  # Field name made lowercase.
    selected = models.BooleanField(blank=True, null=True)
    length = models.IntegerField()
    width = models.IntegerField(blank=True, null=True)
    decimal = models.IntegerField(db_column='Decimal', blank=True, null=True)  # Field name made lowercase.
    bold = models.BooleanField(db_column='Bold', blank=True, null=True)  # Field name made lowercase.
    italic = models.BooleanField(db_column='Italic', blank=True, null=True)  # Field name made lowercase.
    underline = models.BooleanField(db_column='Underline', blank=True, null=True)  # Field name made lowercase.
    content = models.CharField(max_length=50, blank=True, null=True)
    fixed = models.BooleanField(db_column='Fixed', blank=True, null=True)  # Field name made lowercase.
    ordr = models.IntegerField()
    colid = models.AutoField()
    field_name = models.CharField(max_length=50, blank=True, null=True)
    no_store = models.BooleanField(blank=True, null=True)
    auto_generation = models.CharField(db_column='Auto_generation', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ser_list = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attribute_setting'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BillSeries(models.Model):
    id = models.AutoField()
    series_name = models.CharField(max_length=50, blank=True, null=True)
    short_name = models.CharField(max_length=50, blank=True, null=True)
    row = models.IntegerField(blank=True, null=True)
    account_id = models.IntegerField(blank=True, null=True)
    tax_type = models.IntegerField(blank=True, null=True)
    prefix = models.CharField(max_length=255, blank=True, null=True)
    challan_allow = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bill_series'


class CounterData(models.Model):
    id = models.AutoField()
    counter_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'counter_data'


class Customerdata(models.Model):
    id = models.AutoField(unique=True)
    account_name = models.CharField(unique=True, max_length=150)
    address = models.CharField(max_length=250, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    gotra = models.CharField(max_length=50, blank=True, null=True)
    code = models.CharField(max_length=50, blank=True, null=True)
    remarks = models.CharField(max_length=150, blank=True, null=True)
    create_date = models.DateTimeField()
    update_date = models.DateTimeField()
    main_account = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=50)
    series_no = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customerdata'


class DailySummary(models.Model):
    row = models.IntegerField(blank=True, null=True)
    v_name = models.CharField(max_length=50, blank=True, null=True)
    isplus = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'daily_summary'


class Daywisecalculation(models.Model):
    row = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    field_name = models.CharField(max_length=50, blank=True, null=True)
    isplus = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'daywisecalculation'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class GeneralReportCol(models.Model):
    program = models.CharField(max_length=127)
    colm_n = models.CharField(max_length=127)
    selected = models.BooleanField(blank=True, null=True)
    lenth = models.IntegerField()
    width = models.IntegerField(blank=True, null=True)
    decimal = models.IntegerField(db_column='Decimal', blank=True, null=True)  # Field name made lowercase.
    cont = models.CharField(max_length=50, blank=True, null=True)
    ordr = models.IntegerField()
    colid = models.AutoField()
    field_name = models.CharField(max_length=50, blank=True, null=True)
    no_store = models.BooleanField(blank=True, null=True)
    is_print = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'general_report_col'


class GotraData(models.Model):
    gotra_name = models.CharField(max_length=50, blank=True, null=True)
    id = models.AutoField(unique=True)

    class Meta:
        managed = False
        db_table = 'gotra_data'


class GroupData(models.Model):
    group_name = models.CharField(primary_key=True, max_length=50)
    id = models.AutoField()

    class Meta:
        managed = False
        db_table = 'group_data'


class MainGotraData(models.Model):
    gotra_name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'main_gotra_data'


class MainPerson(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'main_person'


class MasterSetting(models.Model):
    id = models.AutoField()
    setting = models.CharField(max_length=50, blank=True, null=True)
    status = models.BooleanField(blank=True, null=True)
    description = models.CharField(db_column='Description', max_length=50, blank=True, null=True)  # Field name made lowercase.
    program = models.CharField(max_length=50, blank=True, null=True)
    data = models.CharField(max_length=20, blank=True, null=True)
    other_data = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'master_setting'


class MsgTemplate(models.Model):
    id = models.AutoField()
    msg_temp = models.CharField(max_length=160, blank=True, null=True)
    default_type = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'msg_template'


class Msgs(models.Model):
    mobile = models.CharField(max_length=15, blank=True, null=True)
    msg_type = models.CharField(max_length=10, blank=True, null=True)
    msg_txt = models.CharField(max_length=160, blank=True, null=True)
    dues = models.FloatField(blank=True, null=True)
    dated = models.CharField(max_length=20, blank=True, null=True)
    serial = models.CharField(max_length=20, blank=True, null=True)
    valu = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'msgs'


class MthOrder(models.Model):
    id = models.AutoField()
    mont_name = models.CharField(max_length=10, blank=True, null=True)
    mont_no = models.IntegerField(blank=True, null=True)
    mont_ord = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mth_order'


class MyInvoicePrint(models.Model):
    id = models.AutoField()
    print_line = models.CharField(max_length=255, blank=True, null=True)
    print_type = models.CharField(max_length=50, blank=True, null=True)
    line_no = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'my_invoice_print'


class MyOtherPrint(models.Model):
    id = models.AutoField()
    print_line = models.CharField(max_length=255, blank=True, null=True)
    print_type = models.CharField(max_length=50, blank=True, null=True)
    line_no = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'my_other_print'


class MyPrnPrint(models.Model):
    id = models.AutoField()
    print_line = models.CharField(max_length=255, blank=True, null=True)
    print_type = models.CharField(max_length=50, blank=True, null=True)
    line_no = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'my_prn_print'


class ReportCol(models.Model):
    program = models.CharField(max_length=50)
    colm_n = models.CharField(max_length=50)
    selected = models.BooleanField(blank=True, null=True)
    lenth = models.IntegerField()
    width = models.IntegerField(blank=True, null=True)
    decimal = models.IntegerField(db_column='Decimal', blank=True, null=True)  # Field name made lowercase.
    cont = models.CharField(max_length=50, blank=True, null=True)
    ordr = models.IntegerField()
    colid = models.AutoField()
    field_name = models.CharField(max_length=50, blank=True, null=True)
    no_store = models.BooleanField(blank=True, null=True)
    is_print = models.BooleanField(blank=True, null=True)
    optional_col = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_col'


class ReportInfo(models.Model):
    id = models.AutoField()
    table_name = models.CharField(max_length=50, blank=True, null=True)
    prg = models.CharField(max_length=50, blank=True, null=True)
    part1 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_info'


class SlipData(models.Model):
    id = models.AutoField()
    series_no = models.IntegerField()
    slip_no = models.CharField(max_length=50)
    voucher_date = models.DateTimeField(blank=True, null=True)
    client_name = models.CharField(max_length=50, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    gotra = models.IntegerField(blank=True, null=True)
    work_type = models.IntegerField()
    amount = models.IntegerField()
    baba = models.IntegerField(blank=True, null=True)
    user_name = models.CharField(max_length=10)
    is_cancel = models.BooleanField(blank=True, null=True)
    counter = models.CharField(max_length=20)
    slip_time = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'slip_data'


class UserAcc(models.Model):
    u_name = models.CharField(max_length=10)
    user_type = models.CharField(max_length=20)
    passw = models.CharField(max_length=10, blank=True, null=True)
    is_block = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_acc'


class UserProgram(models.Model):
    id = models.AutoField()
    prg_name = models.CharField(max_length=50, blank=True, null=True)
    row = models.IntegerField(blank=True, null=True)
    user_option = models.IntegerField(blank=True, null=True)
    master_option = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_program'


class WorkData(models.Model):
    id = models.AutoField(unique=True)
    work_name = models.CharField(max_length=50)
    rate = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'work_data'

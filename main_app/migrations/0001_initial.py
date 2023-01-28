# Generated by Django 4.1.5 on 2023-01-26 13:22

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='contact_us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200)),
                ('contact_no', models.PositiveIntegerField()),
                ('gmail_id', models.CharField(max_length=200)),
                ('facbook_id', models.CharField(max_length=200)),
                ('instagram_id', models.CharField(max_length=200)),
                ('twitter_id', models.CharField(max_length=200)),
                ('linkedin_id', models.CharField(max_length=200, null=True)),
            ],
            options={
                'db_table': 'Company_Details',
            },
        ),
        migrations.CreateModel(
            name='GST_Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_date', models.DateTimeField(auto_now_add=True)),
                ('gst_amt', models.FloatField(default=0.0)),
            ],
            options={
                'db_table': 'GST_Log',
            },
        ),
        migrations.CreateModel(
            name='Level_Plan_Referrals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Level_Plan_Sponsors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Levels',
            fields=[
                ('level', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'Levels',
            },
        ),
        migrations.CreateModel(
            name='Min_Amount_For_Free_Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
            ],
            options={
                'db_table': 'Min_Amount_For_Free_Delivery',
            },
        ),
        migrations.CreateModel(
            name='MLM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'MLM',
            },
        ),
        migrations.CreateModel(
            name='MLMAdmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'MLMAdmin',
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification_date', models.DateTimeField(auto_now=True)),
                ('text', models.CharField(max_length=200)),
                ('read', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'Notification',
            },
        ),
        migrations.CreateModel(
            name='OrderItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('per_item_cost', models.FloatField()),
                ('subtotal', models.FloatField()),
                ('tax', models.FloatField()),
                ('plan', models.CharField(blank=True, max_length=500, null=True)),
                ('total', models.FloatField()),
                ('delivery_status', models.CharField(default='Order Placed', max_length=50)),
                ('delivered_on', models.DateTimeField(blank=True, null=True)),
                ('cancellation_reason', models.CharField(blank=True, max_length=500, null=True)),
                ('cancelled_on', models.DateTimeField(blank=True, null=True)),
                ('return_reason', models.CharField(blank=True, max_length=500, null=True)),
                ('return_status', models.CharField(choices=[('None', 'None'), ('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')], default='None', max_length=100)),
                ('return_raised_on', models.DateTimeField(blank=True, null=True)),
                ('return_on', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'OrderItems',
            },
        ),
        migrations.CreateModel(
            name='OrderItemVariant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'OrderItemVariant',
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField()),
                ('delivery_charges', models.FloatField(default=0.0)),
                ('subtotal', models.FloatField()),
                ('tax', models.FloatField()),
                ('total', models.FloatField()),
                ('point_value', models.FloatField(default=0.0)),
                ('self_pickup', models.BooleanField(default=False)),
                ('paid', models.BooleanField(default=False)),
                ('delivery_status', models.CharField(default='Order Placed', max_length=50)),
            ],
            options={
                'db_table': 'Orders',
            },
        ),
        migrations.CreateModel(
            name='privacypolicy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Privacy and Policy',
            },
        ),
        migrations.CreateModel(
            name='PV_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_pv', models.CharField(blank=True, max_length=15, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'PV data',
            },
        ),
        migrations.CreateModel(
            name='RazorpayOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razorpay_order_id', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'RazorpayOrder',
            },
        ),
        migrations.CreateModel(
            name='RazorpayTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_id', models.CharField(max_length=100)),
                ('order_id', models.CharField(max_length=100)),
                ('signature', models.CharField(max_length=300)),
            ],
            options={
                'db_table': 'RazorpayTransaction',
            },
        ),
        migrations.CreateModel(
            name='Reason',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Reasons',
            },
        ),
        migrations.CreateModel(
            name='termsandcondition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Terms and Condition',
            },
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_balance', models.FloatField(default=0.0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Wallet',
            },
        ),
        migrations.CreateModel(
            name='WalletTransferApproval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.BooleanField(default=True)),
                ('vendor', models.BooleanField(default=True)),
                ('admin', models.BooleanField(default=True)),
                ('lastupdate_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='WalletTransfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('senderusername', models.CharField(max_length=256)),
                ('reciverusername', models.CharField(max_length=256)),
                ('transection_id', models.CharField(max_length=256, unique=True)),
                ('amount', models.IntegerField(default=0)),
                ('transection_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WalletTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_date', models.DateTimeField()),
                ('transaction_type', models.CharField(max_length=20)),
                ('transaction_amount', models.FloatField()),
                ('previous_amount', models.FloatField()),
                ('remaining_amount', models.FloatField()),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.wallet')),
            ],
            options={
                'db_table': 'WalletTransaction',
            },
        ),
        migrations.CreateModel(
            name='UserLinkType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(blank=True, max_length=400, null=True)),
                ('links', models.CharField(blank=True, max_length=400, null=True)),
                ('link_type', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TDS_Log_Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_balance', models.FloatField(default=0.0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TDS_Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_date', models.DateTimeField(auto_now_add=True)),
                ('transaction_type', models.CharField(max_length=20, null=True)),
                ('amount', models.FloatField(default=0.0)),
                ('credited_amt', models.FloatField(default=0.0)),
                ('tds_amt', models.FloatField(default=0.0)),
                ('previous_amount', models.FloatField(blank=True, null=True)),
                ('remaining_amount', models.FloatField(blank=True, null=True)),
                ('tds_log_wallet', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.tds_log_wallet')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'TDS_Log',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.levels')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='role', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Role',
            },
        ),
    ]

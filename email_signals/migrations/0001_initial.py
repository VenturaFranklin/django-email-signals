# Generated by Django 3.2.9 on 2021-12-01 22:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Signal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('plain_text_email', models.TextField(blank=True, null=True)),
                ('html_email', models.TextField(blank=True, null=True)),
                ('subject', models.CharField(max_length=255)),
                ('from_email', models.EmailField(max_length=254)),
                ('to_emails_opt', models.PositiveIntegerField(default=1, help_text='The choice of the user to send the email to. For each             integer `i`, the method `get_email_signal_emails_<i>` will be             called on the model instance. The method should return a list of             emails to send to.')),
                ('template', models.CharField(blank=True, help_text='Custom template to use for the email.', max_length=100, null=True)),
                ('signal_type', models.CharField(choices=[('pre_save', 'Pre Save'), ('post_save', 'Post Save'), ('pre_delete', 'Pre Delete'), ('post_delete', 'Post Delete')], max_length=20)),
                ('active', models.BooleanField(default=True)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
        ),
        migrations.CreateModel(
            name='SignalConstraint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('param_1', models.CharField(max_length=255)),
                ('comparision', models.CharField(choices=[('exact', 'Is Equal To'), ('iexact', 'Is Equal To (case insensitive)'), ('contains', 'Contains'), ('icontains', 'Contains (case insensitive)'), ('in', 'Is One Of'), ('gt', 'Greater Than'), ('gte', 'Greater Than or Equal To'), ('lt', 'Less Than'), ('lte', 'Less Than or Equal To'), ('startswith', 'Starts With'), ('istartswith', 'Starts With (case insensitive)'), ('endswith', 'Ends With'), ('iendswith', 'Ends With (case insensitive)'), ('regex', 'Matches Regular Expression'), ('iregex', 'Matches Regular Expression (case insensitive)'), ('isnull', 'Is Null'), ('isnotnull', 'Is Not Null'), ('true', 'Is True'), ('false', 'Is False')], max_length=20)),
                ('param_2', models.CharField(blank=True, max_length=255, null=True)),
                ('signal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='email_signals.signal')),
            ],
        ),
    ]

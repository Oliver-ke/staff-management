# Generated by Django 2.1.1 on 2018-09-10 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_management', '0002_auto_20180909_1543'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='a_staff',
            options={'ordering': ['name'], 'verbose_name_plural': 'Academic Staff Database'},
        ),
        migrations.AlterField(
            model_name='a_staff',
            name='dFirstAppointment',
            field=models.DateField(verbose_name='Date of first appointment'),
        ),
        migrations.AlterField(
            model_name='a_staff',
            name='duePromotion',
            field=models.BooleanField(verbose_name='Due Promotion'),
        ),
        migrations.AlterField(
            model_name='a_staff',
            name='nYearsPresentG',
            field=models.IntegerField(blank=True, verbose_name='No of years on present grade'),
        ),
        migrations.AlterField(
            model_name='a_staff',
            name='name',
            field=models.CharField(max_length=64, verbose_name='staff name'),
        ),
        migrations.AlterField(
            model_name='a_staff',
            name='pressentYear',
            field=models.DateField(verbose_name='Present Year'),
        ),
        migrations.AlterField(
            model_name='a_staff',
            name='publicationS',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=1, verbose_name='Publication Score'),
        ),
        migrations.AlterField(
            model_name='a_staff',
            name='qualification',
            field=models.CharField(max_length=30, verbose_name='Top Qualification'),
        ),
        migrations.AlterField(
            model_name='a_staff',
            name='rank',
            field=models.CharField(choices=[('assistant_lec', 'Assistant lecturer'), ('lecturer_one', 'Lecturer one'), ('lecturer_two', 'Lecturer two'), ('senior_lec', 'Senior lecturer'), ('reader', 'Reader'), ('professor', 'Professor')], default='assistant_lec', max_length=30, verbose_name='Rank'),
        ),
        migrations.AlterField(
            model_name='a_staff',
            name='responsibilityS',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=1, verbose_name='Responsibility Score'),
        ),
        migrations.AlterField(
            model_name='a_staff',
            name='salaryGLevel',
            field=models.IntegerField(verbose_name='Salary grade Level'),
        ),
        migrations.AlterField(
            model_name='a_staff',
            name='step',
            field=models.IntegerField(verbose_name='Step'),
        ),
        migrations.AlterField(
            model_name='a_staff',
            name='systemRecomUpgrade',
            field=models.CharField(max_length=20, verbose_name='System Upgrade'),
        ),
        migrations.AlterField(
            model_name='a_staff',
            name='teachingE',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=1, verbose_name='Teaching Effectiveness'),
        ),
        migrations.AlterField(
            model_name='a_staff',
            name='totalScore',
            field=models.IntegerField(verbose_name='Total score'),
        ),
        migrations.AlterField(
            model_name='a_staff',
            name='yLastPromotion',
            field=models.DateField(verbose_name='Year of last promotion'),
        ),
    ]
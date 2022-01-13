from django.db import models


class Driver(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=13)
    car_number = models.CharField(max_length=13, null=True)
    car_type = models.CharField(max_length=25, null=True)
    joined = models.DateTimeField(auto_now_add=True, null=True)


class Client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=13)


class Order(models.Model):
    ORDER_STATUSES = (
        (1, 'Created'),
        (2, 'Cancelled'),
        (3, 'Accepted'),
        (4, 'Finished'),
    )
    driver = models.ForeignKey(Driver, on_delete=models.DO_NOTHING)
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
    order_status = models.PositiveSmallIntegerField(choices=ORDER_STATUSES, default=1)
    order_start_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order_start_time']
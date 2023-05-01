from django.db import models


# Create your models here.
class Local(models.Model):
    date = models.DateField(blank=False)
    amount = models.IntegerField(blank=False)
    account = (
        (1, "Samansco"),
        (2, "Lucidity"),
    )

    paid_from = models.IntegerField(choices=account, default=0)
    tools_rate = models.IntegerField(blank=False)
    sam_rate = models.FloatField(blank=False)

    # calculated/
    total_revenue = models.FloatField()
    profit = models.FloatField()
    notes = models.CharField(max_length=500)

    def __str__(self):
        return self.date

    # getting total revenue
    def get_revenue(self):
        mark_up = 1.15  # 15% markup
        rev = self.amount * mark_up
        rtgs_rev = rev * self.tools_rate

        # getting total revenue
        total_revenue = rtgs_rev / self.sam_rate

        self.total_revenue = total_revenue

    # getting profit
    def get_profit(self):
        profit = float(self.total_revenue - self.amount)
        self.profit = profit

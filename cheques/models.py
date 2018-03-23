from django.db import models
from app.models import BaseModel
from decimal import Decimal
from django.utils.translation import ugettext_lazy as _

class Cheque(BaseModel):
    shop = models.ForeignKey('shops.Shop',limit_choices_to={"is_deleted":False})
    date = models.DateTimeField()
    vendor = models.ForeignKey('vendors.Vendor',limit_choices_to={"is_deleted":False},blank=True,null=True)
    cheque_number = models.CharField(max_length=128,null=True,blank=True)
    name = models.CharField(max_length=128)
    account_number = models.CharField(max_length=128,null=True,blank=True)
    amount = models.DecimalField(default=0,decimal_places=2,max_digits=15)
    details = models.TextField(max_length=256,null=True,blank=True)
    
    is_notified = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
     
    class Meta:
        db_table = 'cheque'
        verbose_name = _('cheque')
        verbose_name_plural = _('cheques')
        ordering = ('-date',)        
  
    def __unicode__(self):
        return self.name
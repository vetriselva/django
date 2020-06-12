from django.db import models
import jsonfield
from django.contrib.postgres.fields import JSONField
class Estimates(models.Model):
	
	QUOTE_STATUS = (
	('IQ', 'Initial Quote'),
	('QS', 'Quote Send'),
	('WP', 'Waiting for Payment'),
	('QC', 'Completed'),
	)
	quote_id   			= models.AutoField(primary_key=True)
	quote_number		= models.IntegerField(null= False)
	quote_date 			= models.DateField()
	customer_name		= models.CharField(max_length= 255, null= False)
	salse_person 		= models.CharField(max_length= 255, null= False)
	quote_status		= models.CharField(max_length= 2, choices= QUOTE_STATUS, default='FIXED')
	quote_info			= JSONField()
	quote_summary 		= JSONField()
	
	class Meta:
		db_table = 'tbl_estiamtes'



	

	

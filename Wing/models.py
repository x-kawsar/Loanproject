from django.db import models

LOAN_GRANT = (
    ('Loan', 'Loan'),
    ('Grant', 'Grant'),
)

CURRENCY = (
    ('USD', 'USD'),
    ('JPY', 'JPY'),
)

SECTOR = (
    ('General Public Services', 'General Public Services'),
    ('Defence', 'Defence'),
    ('Public Order and Safety', 'Public Order and Safety'),
    ('Industrial and Economic Services', 'Industrial and Economic Services'),
    ('Agriculture', 'Agriculture'),
    ('Power and Energy', 'Power and Energy'),
    ('Transport and Communications', 'Transport and Communications'),
    ('Local Government and Rural Development', 'Local Government and Rural Development'),
    ('Environment, Climate Change (CC) and Water Resources (WR)', 'Environment, Climate Change (CC) and Water Resources (WR)'),
    ('Housing and Community Amenities', 'Housing and Community Amenities'),
    ('Health', 'Health'),
    ('Recreation, Culture and Religion', 'Recreation, Culture and Religion'),
    ('Education', 'Education'),
    ('Science and IT', 'Science and IT'),
    ('Social Protection', 'Social Protection'),
)

class Wing_One(models.Model):
    name                             = models.CharField(max_length=3000, null=True)
    currency                         = models.CharField(max_length=100, choices=CURRENCY, default='USD')
    amount_as_per_agreement_currency = models.FloatField()
    amount_in_equivalent_million_us  = models.FloatField()
    date_of_signature                = models.DateTimeField(auto_now_add=True)
    development_partner              = models.CharField(max_length=100)
    loan_or_grant                    = models.CharField(max_length=200, choices=LOAN_GRANT, default='Loan')
    sector                           = models.CharField(max_length=500, choices=SECTOR, default='General Public Services')
    comments                         = models.TextField()

    def __str__(self):
        return self.name





from base import engine
from crm.models import models

models.Base.metadata.create_all(bind=engine)

print('Base de données initialisée avec succès !')
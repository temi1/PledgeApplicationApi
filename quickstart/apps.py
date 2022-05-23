from django.apps import AppConfig
import os
from django.apps import AppConfig
from django.conf import settings
from tensorflow.keras.models import load_model
from tensorflow import keras


class ProdModelConfig(AppConfig):
    name = 'prodAPI'
    MODEL_FILE = os.path.join(settings.MODELS, "Productionmodel.h5")
    model = keras.models.load_model(MODEL_FILE)

class QuickstartConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'quickstart'

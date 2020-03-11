# Custom models should be declared before importing
# django-machina models

from django.db import models
from machina.apps.forum_conversation.abstract_models import AbstractTopic

# Custom models should be declared before importing
# django-machina models

class Topic(AbstractTopic):
    icon = models.ImageField(verbose_name="Icon", upload_to="forum/topic_icons")

from machina.apps.forum_conversation.models import *  # noqa

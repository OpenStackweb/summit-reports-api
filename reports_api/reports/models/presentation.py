"""
 * Copyright 2019 OpenStack Foundation
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 * http://www.apache.org/licenses/LICENSE-2.0
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
"""

from django.db import models
from .speaker import Speaker
from .summit_event import SummitEvent
import django_filters


class Presentation(SummitEvent):
    level = models.TextField(db_column='Level')
    status = models.TextField(db_column='Status')
    to_record = models.BooleanField(db_column='ToRecord')
    attending_media = models.BooleanField(db_column='AttendingMedia')

    summitevent_ptr = models.OneToOneField(
        SummitEvent, on_delete=models.CASCADE, parent_link=True, db_column='ID')

    speakers = models.ManyToManyField(Speaker, related_name='presentations', through='PresentationSpeakers',
                                       through_fields=('presentation_id', 'speaker_id'))


    def __str__(self):
        return self.id

    class Meta:
        app_label = 'reports'
        db_table = 'Presentation'


class PresentationSpeakers(models.Model):
    presentation_id = models.ForeignKey(Presentation, db_column='PresentationID', on_delete=models.CASCADE)
    speaker_id = models.ForeignKey(Speaker, db_column='PresentationSpeakerID', on_delete=models.CASCADE)

    def __str__(self):
        return self.presentation_id + ' - ' + self.speaker_id

    class Meta:
        app_label = 'reports'
        db_table = 'Presentation_Speakers'


class PresentationFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method='search_filter')
    summit_id = django_filters.NumberFilter(field_name='summit__id')

    class Meta:
        model = Presentation
        fields = ['title', 'abstract', 'summit__id', 'published']

    def search_filter(self, queryset, name, value):
        queryset = queryset.filter(
            models.Q(title__icontains=value) |
            models.Q(abstract__icontains=value) |
            models.Q(speakers__last_name=value) |
            models.Q(speakers__member__email=value)
        )

        return queryset


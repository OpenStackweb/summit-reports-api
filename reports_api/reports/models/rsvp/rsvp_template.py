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


class RsvpTemplate(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)
    title = models.TextField(db_column='Title')
    enabled = models.BooleanField(db_column='Enabled')


    def __str__(self):
        return self.id

    class Meta:
        app_label = 'reports'
        db_table = 'RSVPTemplate'


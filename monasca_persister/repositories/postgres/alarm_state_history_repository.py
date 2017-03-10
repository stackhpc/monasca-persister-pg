#
# Copyright 2017 StackHPC Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from oslo_log import log

from monasca_persister.repositories.postgres import abstract_repository
from monasca_persister.repositories.utils import parse_alarm_state_hist_message

LOG = log.getLogger(__name__)

class AlarmStateHistPostgresRepository(
    abstract_repository.AbstractPostgresRepository):

    def __init__(self):
        super(AlarmStateHistPostgresRepository, self).__init__()
        self._statement = self._conf.alarm_statement

    def process_message(self, message):
        data = parse_alarm_state_hist_message(message)
        LOG.debug(data)
        return data

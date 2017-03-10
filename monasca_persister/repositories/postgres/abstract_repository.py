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

import abc
import psycopg2
import psycopg2.extensions
import psycopg2.extras
import six

from oslo_config import cfg
from oslo_log import log

from monasca_persister.repositories import abstract_repository

LOG = log.getLogger(__name__)

@six.add_metaclass(abc.ABCMeta)
class AbstractPostgresRepository(abstract_repository.AbstractRepository):

    def __init__(self):
        super(AbstractPostgresRepository, self).__init__()
        self._conf = cfg.CONF.postgres

        args = {
            'host': self._conf.host,
            'port': self._conf.port,
            'user': self._conf.user,
            'password': self._conf.password,
            'dbname': self._conf.dbname
        }
        LOG.debug(args)

        psycopg2.extensions.register_adapter(dict, psycopg2.extras.Json)
        self._connection = psycopg2.connect(**args)

    def write_batch(self, data_points):
        with self._connection.cursor() as cursor:
            cursor.executemany(self._statement, data_points)
            self._connection.commit()

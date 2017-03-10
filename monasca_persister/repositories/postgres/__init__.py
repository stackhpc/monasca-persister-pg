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

from oslo_config import cfg

postgres_opts = [cfg.StrOpt('dbname'),
                 cfg.StrOpt('host'),
                 cfg.StrOpt('port'),
                 cfg.StrOpt('user'),
                 cfg.StrOpt('password', secret=True),
                 cfg.StrOpt('metric_statement'),
                 cfg.StrOpt('alarm_statement')]

postgres_group = cfg.OptGroup(name='postgres', title='postgres')
cfg.CONF.register_group(postgres_group)
cfg.CONF.register_opts(postgres_opts, postgres_group)

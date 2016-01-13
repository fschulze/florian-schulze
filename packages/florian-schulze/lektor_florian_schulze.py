# -*- coding: utf-8 -*-
from lektor.pluginsystem import Plugin
from lektor.types import Type
import datetime
import dateutil.parser


class DatetimeType(Type):
    def value_from_raw(self, raw):
        return dateutil.parser.parse(raw.value, dayfirst=False, yearfirst=True)


def format_dt_utc(dt):
    return "{0}-{1:02d}-{2:02d} {3:02d}:{4:02d}:{5:02d}".format(*dt.utctimetuple())


class FlorianSchulzePlugin(Plugin):
    name = u'florian-schulze'
    description = u'Add your description here.'

    def on_setup_env(self, **extra):
        class fs_utils:
            def strptime(self, raw):
                return dateutil.parser.parse(raw, dayfirst=False, yearfirst=True)

        self.env.types['datetime'] = DatetimeType
        self.env.jinja_env.filters['format_dt_utc'] = format_dt_utc
        self.env.jinja_env.globals['fs_utils'] = fs_utils()

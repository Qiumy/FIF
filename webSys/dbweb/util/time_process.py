#! /usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from flask_babel import gettext
from . import filter_blueprint


@filter_blueprint.app_template_filter('natural_time')
def natural_time(dt):
    """ Returns string representing "time since", 3 days ago, 5 hours ago etc.

    For datetime values, returns a string representing how many seconds,
    minutes or hours ago it was – falling back to the timesince format
    if the value is more than a day old.
    """
    now = datetime.now()
    # print "-->", now   2016-07-18 09:27:25.840414
    # print "---", dt    2016-07-18 09:27:26
    # The dt is truncated to seconds when saved in mysql.  So sometimes now may be small than dt.
    diff = now - dt if now >= dt else now - now

    periods = (
        (diff.days / 365, gettext("year"), gettext("years")),
        (diff.days / 30, gettext("month"), gettext("months")),
        (diff.days / 7, gettext("week"), gettext("weeks")),
        (diff.days, gettext("day"), gettext("days")),
        (diff.seconds / 3600, gettext("hour"), gettext("hours")),
        (diff.seconds / 60, gettext("minute"), gettext("minutes")),
        (diff.seconds, gettext("second"), gettext("seconds")),
    )

    for period, singular, plural in periods:
        if period:
            return "%d %s%s" % (period, singular if period == 1 else plural, gettext(' ago'))

    return gettext("Just now")


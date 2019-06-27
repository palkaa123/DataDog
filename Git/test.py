# Configure the module according to your needs
from datadog import initialize

options = {
    'api_key':'',
    'app_key':''
}

initialize(**options)

# Use Datadog REST API client
from datadog import api

title = "Something big happened!"
text = 'And let me tell you all about it here!'
tags = ['version:1', 'application:web']

api.Event.create(title=title, text=text, tags=tags)


# Use Statsd, a Python client for DogStatsd
from datadog import statsd

# Increment a counter.
statsd.increment('page.views')

# Or ThreadStats, an alternative tool to collect and flush metrics,using Datadog REST API
from datadog import ThreadStats
stats = ThreadStats()
stats.start()
stats.increment('page.views')
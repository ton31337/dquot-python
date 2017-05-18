#### Overview

#### Install

* pip install dquot-python

#### Usage

```
DQuotNotifications(provider=DQuotNotificationProviderStdout()).run()
DQuotNotifications(provider=DQuotNotificationProviderRedis(port=6380)).run()
DQuotNotifications(provider=DQuotNotificationProviderRabbitMQ()).run()

```

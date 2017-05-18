from dquota import DQuotNotifications
from dquota.providers.stdout import DQuotNotificationProviderStdout

DQuotNotifications(provider=DQuotNotificationProviderStdout()).run()

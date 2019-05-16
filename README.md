# octoparse-python

octoparse-python is an API wrapper for Octoparse written in Python

# Installing

# Usage
##### Client instantiation
```
from octoparse.client import Client

client = Client(advanced_api=True)
```

##### Get a new token
```
r = client.new_token('OCTOPARSE USERNAME', 'OCTOPARSE PASSWORD')
```

##### Refresh a token
```
r = client.refresh_token('REFRESH_TOKEN')
```

##### Set access token to client
```
client.set_access_token('ACCESS_TOKEN')
```

##### List all task groups
```
r = client.list_task_groups()
```

##### List all tasks in a group
```
r = client.list_group_tasks('GROUP_ID')
```

##### Get task status
```
TASK_LIST = ['TASK_ID1']
r = client.get_task_status(TASK_LIST)

Task status code:
0 = Running,
1 = Stopped,
2 = Completed,
3 = Waiting,
5 = Never Run
```

##### Get task parameters
```
Configuration parameter name (navigateAction1.Url,loopAction1.UrlList,loopAction1.TextList, etc.)

r = client.get_task_parameters('TASK_ID', 'navigateAction1.Url')
```

##### Update task parameters
```
Configuration parameter name (navigateAction1.Url,loopAction1.UrlList,loopAction1.TextList, etc.)

r = client.update_task_parameters('TASK_ID', 'navigateAction1.Url', 'https://url.com')
```

##### Start running task
```
r = client.start_task('TASK_ID')
```

##### Stop running task
```
r = client.stop_task('TASK_ID')
```

##### Clear data
```
r = client.clear_data('TASK_ID')
```

##### Export Non-exported Data
```
r = client.export_non_exported_data('TASK_ID', 'SIZE')
```

##### Update Data Status
```
r = client.update_data_status('TASK_ID')
```

##### Update Data Status
```
r = client.get_data_by_offset('TASK_ID', 'OFFSET', 'SIZE')
```

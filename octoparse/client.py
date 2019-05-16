import requests

API_BASE_URL = 'https://dataapi.octoparse.com'
ADVANCED_API_BASE_URL = 'https://advancedapi.octoparse.com'


class Client(object):
    BASE_URL = None

    def __init__(self, advanced_api=False):
        self.access_token = None
        if advanced_api:
            self.BASE_URL = ADVANCED_API_BASE_URL
        else:
            self.BASE_URL = API_BASE_URL

    def new_token(self, username, password, grant_type='password'):
        data = {
            'username': username,
            'password': password,
            'grant_type': grant_type
        }
        return self._post(self.BASE_URL + '/token', data=data)

    def refresh_token(self, refresh_token, grant_type='password'):
        data = {
            'refresh_token': refresh_token,
            'grant_type': grant_type
        }
        return self._post(self.BASE_URL + '/token', data=data)

    def set_access_token(self, access_token):
        self.access_token = access_token

    def _get(self, url, **kwargs):
        return self._request('GET', url, **kwargs)

    def _post(self, url, **kwargs):
        return self._request('POST', url, **kwargs)

    def _put(self, url, **kwargs):
        return self._request('PUT', url, **kwargs)

    def _delete(self, url, **kwargs):
        return self._request('DELETE', url, **kwargs)

    def _request(self, method, url, headers=None, **kwargs):
        _headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'bearer {}'.format(self.access_token),
        }
        if headers:
            _headers.update(headers)

        return self._parse(requests.request(method, url, headers=_headers, timeout=60, **kwargs))

    def _parse(self, response):
        if 'Content-Type' in response.headers and 'application/json' in response.headers['Content-Type']:
            r = response.json()
        else:
            r = response.text
        return r

    def list_task_groups(self):
        return self._get(self.BASE_URL + '/api/TaskGroup')

    def list_group_tasks(self, group_id):
        params = {
            'taskGroupId': group_id
        }
        return self._get(self.BASE_URL + '/api/Task', params=params)

    def get_task_status(self, tasks):
        """
        Task status code:
            0 = Running,
            1 = Stopped,
            2 = Completed,
            3 = Waiting,
            5 = Never Run

        Args:
            tasks:

        Returns:

        """
        if not isinstance(tasks, list):
            raise Exception
        data = {
            'taskIdList': tasks
        }
        return self._post(self.BASE_URL + '/api/task/GetTaskStatusByIdList', json=data)

    def get_task_parameters(self, task_id, name):
        """
        Configuration parameter name (navigateAction1.Url,loopAction1.UrlList,loopAction1.TextList, etc.)

        Args:
            task_id:
            name:

        Returns:

        """
        params = {
            'taskId': task_id,
            'name': name
        }
        return self._post(self.BASE_URL + '/api/task/GetTaskRulePropertyByName', params=params)

    def update_task_parameters(self, task_id, name, value):
        data = {
            'taskId': task_id,
            'name': name,
            'value': value
        }
        return self._post(self.BASE_URL + '/api/task/UpdateTaskRule', json=data)

    def add_url_text_to_loop(self, task_id, name, value):
        data = {
            'taskId': task_id,
            'name': name,
            'value': value
        }
        return self._post(self.BASE_URL + '/api/task/AddUrlOrTextToTask', json=data)

    def start_task(self, task_id):
        params = {
            'taskId': task_id,
        }
        return self._post(self.BASE_URL + '/api/task/StartTask', params=params)

    def stop_task(self, task_id):
        params = {
            'taskId': task_id,
        }
        return self._post(self.BASE_URL + '/api/task/StopTask', params=params)

    def clear_data(self, task_id):
        params = {
            'taskId': task_id,
        }
        return self._post(self.BASE_URL + '/api/task/RemoveDataByTaskId', params=params)

    def export_non_exported_data(self, task_id, size):
        params = {
            'taskId': task_id,
            'size': size
        }
        return self._get(self.BASE_URL + '/api/notexportdata/gettop', params=params)

    def update_data_status(self, task_id):
        params = {
            'taskId': task_id,
        }
        return self._post(self.BASE_URL + '/api/notexportdata/update', params=params)

    def get_data_by_offset(self, task_id, offset, size):
        params = {
            'taskId': task_id,
            'offset': offset,
            'size': size
        }
        return self._get(self.BASE_URL + '/api/alldata/GetDataOfTaskByOffset', params=params)

import unittest
import requests
from unittest import TestCase


class TestYD(TestCase):
    def setUp(self):
        self.headers = {'Authorization': 'y0_AgAAAABw_kJ7AADLWwAAAAEF0Op_AADOOQrP8iNK36U5xT0UbiMvEqT9FA'}

    def test_API_YD_with_params(self):
        for i, (param, folder_name, expected) in enumerate([
            ('path', 'test_folder', '<Response [201]>'),
            ('path', 'test_folder', '<Response [409]>'),
            ('pa', 'test_f','<Response [400]>'),

        ]):
            with self.subTest(i):
                def create_folder(params, folder_name):
                    params = {
                        param: folder_name
                    }
                    response = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                                            params=params,
                                            headers=self.headers)
                    return str(response)

                result = create_folder(param, folder_name)
                self.assertEqual(expected, result)

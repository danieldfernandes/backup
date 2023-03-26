import unittest, requests, json 

class TestAPIFIServ(unittest.TestCase):
    url = 'https://websrviqa.wm.cashedge.com/WealthManagementWeb/ws/'

    def test_FI_Infos_Listcase_1(self):
        url = 'https://websrviqa.wm.cashedge.com/WealthManagementWeb/ws/'
        endpoint = 'SeedDataInq/getFinancialInstInfo'
        headers = {'Content-Type': 'application/json'}

        raw_body = '''{
            "RqUID": "RqUID0",
            "SignonRq": {
                "UserInfo": {
                    "UserID": "XMLAdminlcmpdz",
                    "HomeID": 51090001,
                    "UserPassword": {
                        "CryptType": "None",
                        "CryptVal": "Fiserv01$"
                    },
                    "Role": "Admin"
                }
            },
            "FIInfoRq": {
                "FIInfoRequired": "FIIDInfo"
            },
            "partnerID": 51090000,
            "version": "version1"
        }'''

        response = requests.post(url + endpoint, data=raw_body, headers=headers)
        response_json = response.json()
        
        self.assertEqual(response.status_code, 200, "Expected status code 200, but found " + str(response.status_code))
        self.assertEqual(len(response.json()['FIInfoRs']['FIIdList']['FIId']), 1500, "Expected status code 1500, but found " + str(len(response.json()['FIInfoRs']['FIIdList']['FIId'])))
        self.assertEqual(response_json['Status']['StatusDesc'], "Success", "Expected \'Success\' in Status, but found \'" + response_json['Status']['StatusDesc']+"\'")
        self.assertEqual(response_json['SignonRs']['Status']['StatusDesc'], "Success", "Expected \'Success\' in SignonRs, but found " + response_json['SignonRs']['Status']['StatusDesc']+"\'")
        self.assertEqual(response_json['FIInfoRs']['Status']['StatusDesc'], "Success", "Expected \'Success\' in FIInfoRs, but found " + response_json['FIInfoRs']['Status']['StatusDesc']+"\'")

if __name__ == '__main__':
    unittest.main()
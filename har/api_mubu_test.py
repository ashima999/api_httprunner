# NOTE: Generated By HttpRunner v3.1.6
# FROM: har\api_mubu.har


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseApiMubu(HttpRunner):

    config = Config("testcase description").verify(False)

    teststeps = [
        Step(
            RunRequest("/v3/api/user/phone_login")
            .post("https://api2.mubu.com/v3/api/user/phone_login")
            .with_headers(
                **{
                    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
                    "version": "3.0.0-2.0.0.1824",
                    "sec-ch-ua-mobile": "?0",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
                    "data-unique-id": "a2933ade-b323-4a3f-8433-da3c8d5ece1c",
                    "content-type": "application/json;charset=UTF-8",
                    "accept": "application/json, text/plain, */*",
                    "jwt-token": "",
                    "x-request-id": "c1f970e0-9d30-4768-83f5-fce2b0c8d0d9",
                    "sec-ch-ua-platform": '"Windows"',
                    "origin": "https://mubu.com",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://mubu.com/",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                    "content-length": "66",
                }
            )
            .with_json(
                {"phone": "17328856339", "password": "LXE@19951101", "callbackType": 0}
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v3/api/user/profile")
            .post("https://api2.mubu.com/v3/api/user/profile")
            .with_headers(
                **{
                    "content-length": "0",
                    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
                    "sec-ch-ua-mobile": "?0",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
                    "data-unique-id": "a2933ade-b323-4a3f-8433-da3c8d5ece1c",
                    "accept": "application/json, text/plain, */*",
                    "jwt-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiMTcyMjY2NTQiLCJsb2dpblR5cGUiOiJtb2JpbGUiLCJleHAiOjE2NTI1Mzc0MjYsImlhdCI6MTY0OTk0NTQyNn0.ZAx7fli8VFc6S4t1-jUAYf1SK23WspJGMi8N9J61PoaZ1cMb3xZ4DIRTVZCmZ5cs8GdeOXt29YZ2cCfQx19tlg",
                    "sec-ch-ua-platform": '"Windows"',
                    "x-request-id": "d5332946-4a1a-48b5-9e73-792c83a5397d",
                    "version": "3.0.0-2.0.0.1824",
                    "origin": "https://mubu.com",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://mubu.com/",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
            .with_data("")
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v3/api/activity/five_years/participation")
            .post("https://api2.mubu.com/v3/api/activity/five_years/participation")
            .with_headers(
                **{
                    "content-length": "0",
                    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
                    "sec-ch-ua-mobile": "?0",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
                    "data-unique-id": "a2933ade-b323-4a3f-8433-da3c8d5ece1c",
                    "accept": "application/json, text/plain, */*",
                    "jwt-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiMTcyMjY2NTQiLCJsb2dpblR5cGUiOiJtb2JpbGUiLCJleHAiOjE2NTI1Mzc0MjYsImlhdCI6MTY0OTk0NTQyNn0.ZAx7fli8VFc6S4t1-jUAYf1SK23WspJGMi8N9J61PoaZ1cMb3xZ4DIRTVZCmZ5cs8GdeOXt29YZ2cCfQx19tlg",
                    "sec-ch-ua-platform": '"Windows"',
                    "x-request-id": "5638e751-d31d-4e4a-aa2e-3bfc9e9b3033",
                    "version": "3.0.0-2.0.0.1824",
                    "origin": "https://mubu.com",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://mubu.com/",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
            .with_data("")
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 4011)
            .assert_equal("body.msg", "unknown error")
        ),
        Step(
            RunRequest("/v3/api/list/star_relation/get")
            .get("https://api2.mubu.com/v3/api/list/star_relation/get")
            .with_headers(
                **{
                    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
                    "sec-ch-ua-mobile": "?0",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
                    "data-unique-id": "a2933ade-b323-4a3f-8433-da3c8d5ece1c",
                    "accept": "application/json, text/plain, */*",
                    "jwt-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiMTcyMjY2NTQiLCJsb2dpblR5cGUiOiJtb2JpbGUiLCJleHAiOjE2NTI1Mzc0MjYsImlhdCI6MTY0OTk0NTQyNn0.ZAx7fli8VFc6S4t1-jUAYf1SK23WspJGMi8N9J61PoaZ1cMb3xZ4DIRTVZCmZ5cs8GdeOXt29YZ2cCfQx19tlg",
                    "sec-ch-ua-platform": '"Windows"',
                    "x-request-id": "99ab6a54-b8b2-456e-b6d5-6ff3473bd61f",
                    "version": "3.0.0-2.0.0.1824",
                    "origin": "https://mubu.com",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://mubu.com/",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v3/api/list/get_all_documents_page")
            .post("https://api2.mubu.com/v3/api/list/get_all_documents_page")
            .with_headers(
                **{
                    "content-length": "12",
                    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
                    "version": "3.0.0-2.0.0.1824",
                    "sec-ch-ua-mobile": "?0",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
                    "data-unique-id": "a2933ade-b323-4a3f-8433-da3c8d5ece1c",
                    "content-type": "application/json;charset=UTF-8",
                    "accept": "application/json, text/plain, */*",
                    "jwt-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiMTcyMjY2NTQiLCJsb2dpblR5cGUiOiJtb2JpbGUiLCJleHAiOjE2NTI1Mzc0MjYsImlhdCI6MTY0OTk0NTQyNn0.ZAx7fli8VFc6S4t1-jUAYf1SK23WspJGMi8N9J61PoaZ1cMb3xZ4DIRTVZCmZ5cs8GdeOXt29YZ2cCfQx19tlg",
                    "x-request-id": "9cc57edc-0ece-4c98-a126-6a955efb672c",
                    "sec-ch-ua-platform": '"Windows"',
                    "origin": "https://mubu.com",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://mubu.com/",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
            .with_json({"start": ""})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v3/api/user/get_user_params")
            .post("https://api2.mubu.com/v3/api/user/get_user_params")
            .with_headers(
                **{
                    "content-length": "0",
                    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
                    "sec-ch-ua-mobile": "?0",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
                    "data-unique-id": "a2933ade-b323-4a3f-8433-da3c8d5ece1c",
                    "accept": "application/json, text/plain, */*",
                    "jwt-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiMTcyMjY2NTQiLCJsb2dpblR5cGUiOiJtb2JpbGUiLCJleHAiOjE2NTI1Mzc0MjYsImlhdCI6MTY0OTk0NTQyNn0.ZAx7fli8VFc6S4t1-jUAYf1SK23WspJGMi8N9J61PoaZ1cMb3xZ4DIRTVZCmZ5cs8GdeOXt29YZ2cCfQx19tlg",
                    "sec-ch-ua-platform": '"Windows"',
                    "x-request-id": "9a81e54f-72bd-49a4-8044-bdef859de3df",
                    "version": "3.0.0-2.0.0.1824",
                    "origin": "https://mubu.com",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://mubu.com/",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
            .with_data("")
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v3/api/message/get_message_unread")
            .post("https://api2.mubu.com/v3/api/message/get_message_unread")
            .with_headers(
                **{
                    "content-length": "10",
                    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
                    "version": "3.0.0-2.0.0.1824",
                    "sec-ch-ua-mobile": "?0",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
                    "data-unique-id": "a2933ade-b323-4a3f-8433-da3c8d5ece1c",
                    "content-type": "application/json;charset=UTF-8",
                    "accept": "application/json, text/plain, */*",
                    "jwt-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiMTcyMjY2NTQiLCJsb2dpblR5cGUiOiJtb2JpbGUiLCJleHAiOjE2NTI1Mzc0MjYsImlhdCI6MTY0OTk0NTQyNn0.ZAx7fli8VFc6S4t1-jUAYf1SK23WspJGMi8N9J61PoaZ1cMb3xZ4DIRTVZCmZ5cs8GdeOXt29YZ2cCfQx19tlg",
                    "x-request-id": "48f8cf34-6a37-4ffb-86e9-de34c07d3ad1",
                    "sec-ch-ua-platform": '"Windows"',
                    "origin": "https://mubu.com",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://mubu.com/",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
            .with_json({"page": 1})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v3/api/user/get_onboard_state")
            .post("https://api2.mubu.com/v3/api/user/get_onboard_state")
            .with_headers(
                **{
                    "content-length": "2",
                    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
                    "version": "3.0.0-2.0.0.1824",
                    "sec-ch-ua-mobile": "?0",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
                    "data-unique-id": "a2933ade-b323-4a3f-8433-da3c8d5ece1c",
                    "content-type": "application/json;charset=UTF-8",
                    "accept": "application/json, text/plain, */*",
                    "jwt-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiMTcyMjY2NTQiLCJsb2dpblR5cGUiOiJtb2JpbGUiLCJleHAiOjE2NTI1Mzc0MjYsImlhdCI6MTY0OTk0NTQyNn0.ZAx7fli8VFc6S4t1-jUAYf1SK23WspJGMi8N9J61PoaZ1cMb3xZ4DIRTVZCmZ5cs8GdeOXt29YZ2cCfQx19tlg",
                    "x-request-id": "97209542-d205-4b2f-82c1-b1ed7652f471",
                    "sec-ch-ua-platform": '"Windows"',
                    "origin": "https://mubu.com",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://mubu.com/",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
            .with_json({})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v3/api/list/item_count")
            .post("https://api2.mubu.com/v3/api/list/item_count")
            .with_headers(
                **{
                    "content-length": "30",
                    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
                    "version": "3.0.0-2.0.0.1824",
                    "sec-ch-ua-mobile": "?0",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
                    "data-unique-id": "a2933ade-b323-4a3f-8433-da3c8d5ece1c",
                    "content-type": "application/json;charset=UTF-8",
                    "accept": "application/json, text/plain, */*",
                    "jwt-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiMTcyMjY2NTQiLCJsb2dpblR5cGUiOiJtb2JpbGUiLCJleHAiOjE2NTI1Mzc0MjYsImlhdCI6MTY0OTk0NTQyNn0.ZAx7fli8VFc6S4t1-jUAYf1SK23WspJGMi8N9J61PoaZ1cMb3xZ4DIRTVZCmZ5cs8GdeOXt29YZ2cCfQx19tlg",
                    "x-request-id": "a9ccd9fe-1021-4b31-b882-24f243ec8e8f",
                    "sec-ch-ua-platform": '"Windows"',
                    "origin": "https://mubu.com",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://mubu.com/",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
            .with_json({"folderId": 0, "source": "home"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v3/api/advertisement/get")
            .post("https://api2.mubu.com/v3/api/advertisement/get")
            .with_headers(
                **{
                    "content-length": "10",
                    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
                    "version": "3.0.0-2.0.0.1824",
                    "sec-ch-ua-mobile": "?0",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
                    "data-unique-id": "a2933ade-b323-4a3f-8433-da3c8d5ece1c",
                    "content-type": "application/json;charset=UTF-8",
                    "accept": "application/json, text/plain, */*",
                    "jwt-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiMTcyMjY2NTQiLCJsb2dpblR5cGUiOiJtb2JpbGUiLCJleHAiOjE2NTI1Mzc0MjYsImlhdCI6MTY0OTk0NTQyNn0.ZAx7fli8VFc6S4t1-jUAYf1SK23WspJGMi8N9J61PoaZ1cMb3xZ4DIRTVZCmZ5cs8GdeOXt29YZ2cCfQx19tlg",
                    "x-request-id": "3e5e674f-04af-43ef-8c9b-4bbecdbd4fec",
                    "sec-ch-ua-platform": '"Windows"',
                    "origin": "https://mubu.com",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://mubu.com/",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
            .with_json({"type": 1})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v3/api/notify/new_tip/get")
            .post("https://api2.mubu.com/v3/api/notify/new_tip/get")
            .with_headers(
                **{
                    "content-length": "10",
                    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
                    "version": "3.0.0-2.0.0.1824",
                    "sec-ch-ua-mobile": "?0",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
                    "data-unique-id": "a2933ade-b323-4a3f-8433-da3c8d5ece1c",
                    "content-type": "application/json;charset=UTF-8",
                    "accept": "application/json, text/plain, */*",
                    "jwt-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiMTcyMjY2NTQiLCJsb2dpblR5cGUiOiJtb2JpbGUiLCJleHAiOjE2NTI1Mzc0MjYsImlhdCI6MTY0OTk0NTQyNn0.ZAx7fli8VFc6S4t1-jUAYf1SK23WspJGMi8N9J61PoaZ1cMb3xZ4DIRTVZCmZ5cs8GdeOXt29YZ2cCfQx19tlg",
                    "x-request-id": "8059149f-cb92-46a3-a017-ecaffc917a3a",
                    "sec-ch-ua-platform": '"Windows"',
                    "origin": "https://mubu.com",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://mubu.com/",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
            .with_json({"type": 1})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v3/api/list/create_doc")
            .post("https://api2.mubu.com/v3/api/list/create_doc")
            .with_headers(
                **{
                    "content-length": "25",
                    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
                    "version": "3.0.0-2.0.0.1824",
                    "sec-ch-ua-mobile": "?0",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
                    "data-unique-id": "a2933ade-b323-4a3f-8433-da3c8d5ece1c",
                    "content-type": "application/json;charset=UTF-8",
                    "accept": "application/json, text/plain, */*",
                    "jwt-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiMTcyMjY2NTQiLCJsb2dpblR5cGUiOiJtb2JpbGUiLCJleHAiOjE2NTI1Mzc0MjYsImlhdCI6MTY0OTk0NTQyNn0.ZAx7fli8VFc6S4t1-jUAYf1SK23WspJGMi8N9J61PoaZ1cMb3xZ4DIRTVZCmZ5cs8GdeOXt29YZ2cCfQx19tlg",
                    "x-request-id": "38c7dd95-68ac-4fab-9391-f637822dc04b",
                    "sec-ch-ua-platform": '"Windows"',
                    "origin": "https://mubu.com",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://mubu.com/",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
            .with_json({"folderId": "0", "type": 0})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v3/api/list/item_count")
            .post("https://api2.mubu.com/v3/api/list/item_count")
            .with_headers(
                **{
                    "content-length": "30",
                    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
                    "version": "3.0.0-2.0.0.1824",
                    "sec-ch-ua-mobile": "?0",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
                    "data-unique-id": "a2933ade-b323-4a3f-8433-da3c8d5ece1c",
                    "content-type": "application/json;charset=UTF-8",
                    "accept": "application/json, text/plain, */*",
                    "jwt-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiMTcyMjY2NTQiLCJsb2dpblR5cGUiOiJtb2JpbGUiLCJleHAiOjE2NTI1Mzc0MjYsImlhdCI6MTY0OTk0NTQyNn0.ZAx7fli8VFc6S4t1-jUAYf1SK23WspJGMi8N9J61PoaZ1cMb3xZ4DIRTVZCmZ5cs8GdeOXt29YZ2cCfQx19tlg",
                    "x-request-id": "edd529e4-21b1-4a87-918e-2f1a91dbce57",
                    "sec-ch-ua-platform": '"Windows"',
                    "origin": "https://mubu.com",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://mubu.com/",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
            .with_json({"folderId": 0, "source": "home"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v3/api/document/edit/get")
            .post("https://api2.mubu.com/v3/api/document/edit/get")
            .with_headers(
                **{
                    "content-length": "37",
                    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
                    "version": "3.0.0-2.0.0.1824",
                    "sec-ch-ua-mobile": "?0",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
                    "data-unique-id": "a2933ade-b323-4a3f-8433-da3c8d5ece1c",
                    "content-type": "application/json;charset=UTF-8",
                    "accept": "application/json, text/plain, */*",
                    "jwt-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiMTcyMjY2NTQiLCJsb2dpblR5cGUiOiJtb2JpbGUiLCJleHAiOjE2NTI1Mzc0MjYsImlhdCI6MTY0OTk0NTQyNn0.ZAx7fli8VFc6S4t1-jUAYf1SK23WspJGMi8N9J61PoaZ1cMb3xZ4DIRTVZCmZ5cs8GdeOXt29YZ2cCfQx19tlg",
                    "x-request-id": "c519493d-cb08-4c67-a0d7-3e67ae3142cf",
                    "sec-ch-ua-platform": '"Windows"',
                    "origin": "https://mubu.com",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://mubu.com/",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
            .with_json({"docId": "4qBvWxMIq9e", "password": ""})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v3/api/colla/events")
            .post("https://api2.mubu.com/v3/api/colla/events")
            .with_headers(
                **{
                    "content-length": "94",
                    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
                    "sec-ch-ua-mobile": "?0",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
                    "data-unique-id": "a2933ade-b323-4a3f-8433-da3c8d5ece1c",
                    "content-type": "application/json;charset=UTF-8",
                    "accept": "application/json, text/plain, */*",
                    "jwt-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiMTcyMjY2NTQiLCJsb2dpblR5cGUiOiJtb2JpbGUiLCJleHAiOjE2NTI1Mzc0MjYsImlhdCI6MTY0OTk0NTQyNn0.ZAx7fli8VFc6S4t1-jUAYf1SK23WspJGMi8N9J61PoaZ1cMb3xZ4DIRTVZCmZ5cs8GdeOXt29YZ2cCfQx19tlg",
                    "x-request-id": "5fc9d7ad-1c32-43de-89df-370724966e65",
                    "sec-ch-ua-platform": '"Windows"',
                    "origin": "https://mubu.com",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://mubu.com/",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
            .with_json(
                {
                    "reqId": "1",
                    "type": "USER_HEARTBEAT",
                    "memberId": "4173092714903262",
                    "documentId": "4qBvWxMIq9e",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v3/api/colla/register")
            .get("https://api2.mubu.com/v3/api/colla/register")
            .with_headers(
                **{
                    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
                    "sec-ch-ua-mobile": "?0",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
                    "data-unique-id": "a2933ade-b323-4a3f-8433-da3c8d5ece1c",
                    "accept": "application/json, text/plain, */*",
                    "jwt-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiMTcyMjY2NTQiLCJsb2dpblR5cGUiOiJtb2JpbGUiLCJleHAiOjE2NTI1Mzc0MjYsImlhdCI6MTY0OTk0NTQyNn0.ZAx7fli8VFc6S4t1-jUAYf1SK23WspJGMi8N9J61PoaZ1cMb3xZ4DIRTVZCmZ5cs8GdeOXt29YZ2cCfQx19tlg",
                    "x-request-id": "15d70836-b6c3-42ea-9e2e-c77e159da600",
                    "sec-ch-ua-platform": '"Windows"',
                    "origin": "https://mubu.com",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://mubu.com/",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("/v3/api/refer/doc/list")
            .post("https://api2.mubu.com/v3/api/refer/doc/list")
            .with_headers(
                **{
                    "content-length": "29",
                    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
                    "sec-ch-ua-mobile": "?0",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
                    "data-unique-id": "a2933ade-b323-4a3f-8433-da3c8d5ece1c",
                    "content-type": "application/json;charset=UTF-8",
                    "accept": "application/json, text/plain, */*",
                    "jwt-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiMTcyMjY2NTQiLCJsb2dpblR5cGUiOiJtb2JpbGUiLCJleHAiOjE2NTI1Mzc0MjYsImlhdCI6MTY0OTk0NTQyNn0.ZAx7fli8VFc6S4t1-jUAYf1SK23WspJGMi8N9J61PoaZ1cMb3xZ4DIRTVZCmZ5cs8GdeOXt29YZ2cCfQx19tlg",
                    "x-request-id": "73c1873c-8aab-475e-bd2a-b72afa94eae5",
                    "sec-ch-ua-platform": '"Windows"',
                    "origin": "https://mubu.com",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://mubu.com/",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
            .with_json({"targetDocId": "4qBvWxMIq9e"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v3/api/refer/node/count")
            .post("https://api2.mubu.com/v3/api/refer/node/count")
            .with_headers(
                **{
                    "content-length": "29",
                    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
                    "version": "3.0.0-2.0.0.1824",
                    "sec-ch-ua-mobile": "?0",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
                    "data-unique-id": "a2933ade-b323-4a3f-8433-da3c8d5ece1c",
                    "content-type": "application/json;charset=UTF-8",
                    "accept": "application/json, text/plain, */*",
                    "jwt-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiMTcyMjY2NTQiLCJsb2dpblR5cGUiOiJtb2JpbGUiLCJleHAiOjE2NTI1Mzc0MjYsImlhdCI6MTY0OTk0NTQyNn0.ZAx7fli8VFc6S4t1-jUAYf1SK23WspJGMi8N9J61PoaZ1cMb3xZ4DIRTVZCmZ5cs8GdeOXt29YZ2cCfQx19tlg",
                    "x-request-id": "89b9b7ed-50f4-4e8d-93ce-06d784cf62cb",
                    "sec-ch-ua-platform": '"Windows"',
                    "origin": "https://mubu.com",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://mubu.com/",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
            .with_json({"targetDocId": "4qBvWxMIq9e"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v3/api/colla/members_v2")
            .post("https://api2.mubu.com/v3/api/colla/members_v2")
            .with_headers(
                **{
                    "content-length": "58",
                    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
                    "sec-ch-ua-mobile": "?0",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
                    "data-unique-id": "a2933ade-b323-4a3f-8433-da3c8d5ece1c",
                    "content-type": "application/json;charset=UTF-8",
                    "accept": "application/json, text/plain, */*",
                    "jwt-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiMTcyMjY2NTQiLCJsb2dpblR5cGUiOiJtb2JpbGUiLCJleHAiOjE2NTI1Mzc0MjYsImlhdCI6MTY0OTk0NTQyNn0.ZAx7fli8VFc6S4t1-jUAYf1SK23WspJGMi8N9J61PoaZ1cMb3xZ4DIRTVZCmZ5cs8GdeOXt29YZ2cCfQx19tlg",
                    "request-id": "members:4173092714903262:1649945467587",
                    "x-request-id": "8af02706-81fb-4476-9180-282e3063fbff",
                    "sec-ch-ua-platform": '"Windows"',
                    "origin": "https://mubu.com",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://mubu.com/",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
            .with_json({"memberId": "4173092714903262", "documentId": "4qBvWxMIq9e"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
        ),
        Step(
            RunRequest("/v3/api/refer/search_refers")
            .post("https://api2.mubu.com/v3/api/refer/search_refers")
            .with_headers(
                **{
                    "content-length": "52",
                    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
                    "sec-ch-ua-mobile": "?0",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
                    "data-unique-id": "a2933ade-b323-4a3f-8433-da3c8d5ece1c",
                    "content-type": "application/json;charset=UTF-8",
                    "accept": "application/json, text/plain, */*",
                    "jwt-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJtdWJ1Iiwic3ViIjoiMTcyMjY2NTQiLCJsb2dpblR5cGUiOiJtb2JpbGUiLCJleHAiOjE2NTI1Mzc0MjYsImlhdCI6MTY0OTk0NTQyNn0.ZAx7fli8VFc6S4t1-jUAYf1SK23WspJGMi8N9J61PoaZ1cMb3xZ4DIRTVZCmZ5cs8GdeOXt29YZ2cCfQx19tlg",
                    "x-request-id": "d0a53c4a-7a2b-433d-8625-83bcf46985a0",
                    "sec-ch-ua-platform": '"Windows"',
                    "origin": "https://mubu.com",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://mubu.com/",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "zh-CN,zh;q=0.9",
                }
            )
            .with_json({"docId": "4qBvWxMIq9e", "keywords": "test", "option": 1})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
        ),
    ]


if __name__ == "__main__":
    TestCaseApiMubu().test_start()

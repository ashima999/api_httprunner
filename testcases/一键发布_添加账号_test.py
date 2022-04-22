from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase

from testcases.一键发布_获取平台_test import TestGetType



class TestAdd(HttpRunner):
    config = Config("添加账号").verify(False).base_url("${get_host()}")

    teststeps = [
        Step(RunTestCase("获取平台id").call(TestGetType).export(*["id"])),
        Step(
            RunRequest("添加账号")
            .post("/publish/user/add")
            .with_headers(
                **{
                    "User-Agent": "HttpRunner/${get_httprunner_version()}",
                    "source-id": "8",
                    "cw-authorization": "${get_token()}",
                }
            )
            .with_json(
                {
                    "id": "$id",
                    "name": "测试账号",
                    "app_id": "2273983074",
                    "app_secret": "d0174ed3c11ec3180ba8010e20815f92"
                }
            )
            .validate()
            .assert_equal("body.code", 200)
            .assert_equal("body.message", "OK")
        ),
    ]


if __name__ == "__main__":
    TestAdd().test_start()

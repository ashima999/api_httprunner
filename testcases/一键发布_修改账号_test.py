from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from testcases.一键发布_获取账号列表_test import TestGetPageList


class TestEdit(HttpRunner):
    config = Config("修改账号").verify(False).base_url("${get_host()}")

    teststeps = [
        Step(RunTestCase("获取账号id").call(TestGetPageList).export(*["item_id"])),
        Step(
            RunRequest("修改账号")
            .post("/publish/user/edit")
            .with_headers(
                **{
                    "User-Agent": "HttpRunner/${get_httprunner_version()}",
                    "source-id": "8",
                    "cw-authorization": "${get_token()}",
                }
            )
            .with_json(
                {
                    "id": "$item_id",
                    "name": "测试账号修改",
                    "app_id": "2273983074",
                    "app_secret": "d0174ed3c11ec3180ba8010e20815f92",
                }
            )
            .validate()
            .assert_equal("body.code", 200)
            .assert_equal("body.message", "OK")
        ),
    ]


if __name__ == "__main__":
    TestEdit().test_start()

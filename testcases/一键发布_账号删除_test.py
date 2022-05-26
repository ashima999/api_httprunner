from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from testcases.一键发布_获取账号列表_test import TestGetPageList


class TestDelete(HttpRunner):
    config = Config("账号删除").verify(False).base_url("${get_host()}")

    teststeps = [
        Step(RunTestCase("获取账号id").call(TestGetPageList).export(*["item_id"])),
        Step(
            RunRequest("账号删除")
            .get("/publish/user/delete")
            .with_params(**{"id": "$item_id"})
            #.with_variables(**{"id": "$item_id", "status": "1"})
            .with_headers(
                **{
                    "User-Agent": "HttpRunner/${get_httprunner_version()}",
                    "source-id": "8",
                    "cw-authorization": "${get_token()}",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 200)
            #.assert_equal("body.success", True)
        )
    ]


if __name__ == "__main__":
    TestDelete.test_start()

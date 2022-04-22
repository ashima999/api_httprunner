import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from testcases.一键发布_获取账号列表_test import TestGetPageList


class TestGetItem(HttpRunner):
    config = Config("获取账号详情").verify(False).base_url("${get_host()}")

    teststeps = [
        Step(
            RunTestCase("获取账号id")
            .with_variables(**{})
            .call(TestGetPageList)
            .export(*["item_id"])
        ),
        Step(
            RunRequest("获取账号详情")
            .get("/publish/user/getItem")
            .with_params(**{"id": "$item_id"})
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
            .assert_equal("body.message", "OK")
        ),
    ]

if __name__ == "__main__":
    TestGetItem().test_start()

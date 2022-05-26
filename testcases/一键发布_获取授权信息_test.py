from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from testcases.一键发布_获取平台_test import TestGetType


class TestOauth(HttpRunner):
    config = Config("获取授权信息").verify(False).base_url("${get_host()}")

    teststeps = [
        Step(RunTestCase("获取平台id").call(TestGetType).export(*["id"])),
        Step(
            RunRequest("获取授权信息")
            .get("/publish/user/oauth")
            .with_headers(
                **{
                    "User-Agent": "HttpRunner/${get_httprunner_version()}",
                    "source-id": "8",
                    "cw-authorization": "${get_token()}",
                }
            )
            .with_params(**{"id": "$id"})
            .validate()
            .assert_equal("body.code",200)
            .assert_equal("body.message","OK")
        )
    ]


if __name__ == "__main__":
    TestOauth().test_start()
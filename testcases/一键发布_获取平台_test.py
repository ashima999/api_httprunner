from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
import pytest

class TestGetType(HttpRunner):
    config = (
        Config("获取平台")
        .verify(False)
        # .base_url("https://apisaastest.kpinfo.cn/api")
        .base_url("${get_host()}")
        .export(*["id"])
    )

    teststeps = [
        Step(
            RunRequest("获取平台")
            .get("publish/user/getType")
            .with_headers(
                **{
                    "User-Agent": "HttpRunner/${get_httprunner_version()}",
                    "source-id": "8",
                    "cw-authorization": "${get_token()}",
                }
            )
            .with_params(**{"type_id": "2017001"})
            .extract()
            .with_jmespath("body.data","data")
            .with_jmespath("body.data[-1].id", "id")
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 200)
            .assert_equal("body.message", "OK")
        )
    ]


if __name__ == "__main__":
    TestGetType().test_start()

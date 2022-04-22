from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestGetPageList(HttpRunner):
    config = (
        Config("获取账号列表")
        .verify(False)
        # .base_url("https://apisaastest.kpinfo.cn/api")
        .base_url("${get_host()}")
        .export(*["item_id"])
    )

    teststeps = [
        Step(
            RunRequest("获取账号列表")
            .get("/publish/user/getPageLists")
            .with_headers(
                **{
                    "User-Agent": "HttpRunner/${get_httprunner_version()}",
                    "source-id": "8",
                    "cw-authorization": "${get_token()}",
                }
            )
            # .with_params(**{"type_id": "2017001"})
            .extract()
            .with_jmespath("body.data.items[0].id", "item_id")
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 200)
            .assert_equal("body.message", "OK")
        )
    ]


if __name__ == "__main__":
    TestGetPageList().test_start()

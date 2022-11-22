# pytest-github-actions-reporter-example

This repository illustrates how to use [dorny/test-reporter](https://github.com/dorny/test-reporter) along with [pytest](https://docs.pytest.org/en/7.2.x/) to create a pretty test report inside Github Actions.

Check out [`.github/workflows/ci.yml`](https://github.com/dfederschmidt/pytest-github-actions-reporter-example/blob/ffa4426898a840e4ce009ea27e18ff3d142f92fa/.github/workflows/ci.yml) for an examle of how to set this up.

The key ingredient is the `--junitxml` flag which allows to output a report in XML format that can be understood by the test reporter.
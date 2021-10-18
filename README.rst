Spring Boot `/actuator/env` difffing
====================================

|PyPI| |Python Version| |License|

|Read the Docs| |Tests| |Codecov|

|pre-commit| |Black|

.. |PyPI| image:: https://img.shields.io/pypi/v/spring-boot-env-diff.svg
   :target: https://pypi.org/project/spring-boot-env-diff/
   :alt: PyPI
.. |Python Version| image:: https://img.shields.io/pypi/pyversions/spring-boot-env-diff
   :target: https://pypi.org/project/spring-boot-env-diff
   :alt: Python Version
.. |License| image:: https://img.shields.io/pypi/l/spring-boot-env-diff
   :target: https://opensource.org/licenses/MIT
   :alt: License
.. |Read the Docs| image:: https://img.shields.io/readthedocs/spring-boot-env-diff/latest.svg?label=Read%20the%20Docs
   :target: https://spring-boot-env-diff.readthedocs.io/
   :alt: Read the documentation at https://spring-boot-env-diff.readthedocs.io/
.. |Tests| image:: https://github.com/ties/spring-boot-env-diff/workflows/Tests/badge.svg
   :target: https://github.com/ties/spring-boot-env-diff/actions?workflow=Tests
   :alt: Tests
.. |Codecov| image:: https://codecov.io/gh/ties/spring-boot-env-diff/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/ties/spring-boot-env-diff
   :alt: Codecov
.. |pre-commit| image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
   :target: https://github.com/pre-commit/pre-commit
   :alt: pre-commit
.. |Black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: Black


Compare two outputs from the Spring Boot `/actuator/env` endpoint to make sure the configs match. Especially useful when refactoring configuration properties.

## How to run:
```
pipenv run python -m spring_boot_env_diff 20211018-properties-post.json 20211018-properties-pre.json
```

Features
--------

* Diff two Spring Boot `/actuator/env` endpoints and reports the differences.


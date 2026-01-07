Change Log
===========

1.0.11
-------
- Refactored `latest()` news method to use HTML scraping instead of a defunct JSON API.
- Removed automated testing framework (`pytest`, `pytest-mock`) and linter (`flake8`).
- Replaced automated tests with a comprehensive manual testing script.
- Cleaned up all related configuration files (`setup.py`, `setup.cfg`, CI files).
- Updated `README.md` for accuracy and better usage examples.

1.0.9
-------
- Change `requests` to `curl-cffi`
- Added GitHub Actions workflow for PyPI auto-publish.

1.0.8
-------
- Solve empty headlines

1.0.7
-------
- Add markets data to ycnbc

1.0.6
-------
- Remove pandas from meta.yaml


1.0.5
-------
- Excluded pandas dependency to streamline the library and reduce external dependencies.

1.0.4
-------
- Remapping Query Data

-------
1.0.3
-------
- Fixing Query Data

1.0.2
-------
- Mapping Posttime

-------
- Update Requirements.txt
- Add method for Get Data By Categories / URLs

-------
1.0.1
-------

- Update Requirements.txt
- Add method for Get Data By Categories / URLs

-------
1.0.0
-------

- Initial release (alpha)
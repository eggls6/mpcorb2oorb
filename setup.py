from setuptools import setup

setup(
   use_scm_version={
      "write_to": "mpcorb2oorb/version.py",
      "write_to_template": "__version__ = '{version}'",
    }
)

# setup.py
# Python setup script for a maturin project

from setuptools import setup

setup(
    name="pyrs_template",
    version="0.1.0",
    packages=["pyrs_template"],
    # Including Rust extension
    include_package_data=True,
    zip_safe=False,
    # Metadata for maturin
    maturin_project={
        "name": "pyrs_template_lib",
        "cargo_toml": "src/Cargo.toml",
    },
)


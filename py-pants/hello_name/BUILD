python_sources(name="lib")

python_tests(name="tests")

# This target allows us to build a `.whl` bdist and a `.tar.gz` sdist by auto-generating
#  `setup.py`. See https://www.pantsbuild.org/docs/python-distributions.
#
python_distribution(
    name="dist",
    dependencies=[":lib"],
    wheel=True,
    sdist=True,
    provides=setup_py(
        name="hello_name",
        version="0.0.1",
        description="Greet with hello name",
    ),
)

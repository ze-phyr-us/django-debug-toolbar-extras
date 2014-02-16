from setuptools import setup, find_packages

setup(
    name = "django-debug-toolbar-extras",
    version = __import__("debug_toolbar_extras").__version__,
    author = "Glenn Washburn",
    author_email = "development@efficientek.com",
    description = "A collection of add-on panels for Django's debug_toolbar.",
    url = "http://github.com/crass/django-debug-toolbar-extras/",
    license = "BSD",
    packages = find_packages(),
    include_package_data = True,
    classifiers = [
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Utilities",
        "Framework :: Django",
    ]
)

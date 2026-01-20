# Diff

[![Actions Status](https://github.com/Egorov-Andrey/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Egorov-Andrey/python-project-50/actions)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=Egorov-Andrey_python-project-50&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=Egorov-Andrey_python-project-50)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=Egorov-Andrey_python-project-50&metric=bugs)](https://sonarcloud.io/summary/new_code?id=Egorov-Andrey_python-project-50)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=Egorov-Andrey_python-project-50&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=Egorov-Andrey_python-project-50)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=Egorov-Andrey_python-project-50&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=Egorov-Andrey_python-project-50)
[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=Egorov-Andrey_python-project-50&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=Egorov-Andrey_python-project-50)

[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=Egorov-Andrey_python-project-50&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=Egorov-Andrey_python-project-50)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=Egorov-Andrey_python-project-50&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=Egorov-Andrey_python-project-50)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=Egorov-Andrey_python-project-50&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=Egorov-Andrey_python-project-50)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=Egorov-Andrey_python-project-50&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=Egorov-Andrey_python-project-50)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=Egorov-Andrey_python-project-50&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=Egorov-Andrey_python-project-50)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=Egorov-Andrey_python-project-50&metric=coverage)](https://sonarcloud.io/summary/new_code?id=Egorov-Andrey_python-project-50)

### Links

This project was built using these tools:

| Tool                                                    | Description                                                            |
|---------------------------------------------------------|------------------------------------------------------------------------|
| [uv](https://docs.astral.sh/uv/)                        | "An extremely fast Python package and project manager, written in Rust"|  
| [ruff](https://docs.astral.sh/ruff/)                    | "An extremely fast Python linter and code formatter, written in Rust"  |
| [pytest](https://docs.pytest.org/en/stable/contents.html)| "Framework for writing automated code validation tests"

### Description diff

The "diff" utility is designed to compare two files in the format ".json", ".yaml" and output differences in the formats 'stylish', 'plain', 'json'.
___
### Setup

```bash
make build
make install

```
### Run

```bash
gendiff first_file second_file
gendiff -f json first_file second_file
gendiff -f plain first_file second_file
```
### Tests 

```bash
make test
make test-coverage
```

### Asciinema with gendiff first_file second_file:

***Format "stylish"***

[![asciicast](https://asciinema.org/a/VzUqLVN8EzjLj6BC.svg)](https://asciinema.org/a/VzUqLVN8EzjLj6BC)

***Format "plain"***

[![asciicast](https://asciinema.org/a/kCL3K0nkUqQJhMuZ.svg)](https://asciinema.org/a/kCL3K0nkUqQJhMuZ)

***Format "json"***

[![asciicast](https://asciinema.org/a/qNWHxa0dDTRIOqux.svg)](https://asciinema.org/a/qNWHxa0dDTRIOqux)


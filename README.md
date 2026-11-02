# Accounts Microservice

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python 3.9](https://img.shields.io/badge/Python-3.9-green.svg)](https://www.python.org/)
[![CI Build](https://github.com/rutikgadre7565/devops-capstone-project/actions/workflows/ci-build.yaml/badge.svg)](https://github.com/rutikgadre7565/devops-capstone-project/actions/workflows/ci-build.yaml)

## Project Overview
A RESTful Accounts Microservice developed using Python, Flask, PostgreSQL and SQLAlchemy as part of the IBM DevOps Capstone Project.

## Features
- Create accounts
- List all accounts
- Read an account by ID
- Update account details
- Delete accounts
- Health check endpoint

## REST API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /accounts | Create account |
| GET | /accounts | List accounts |
| GET | /accounts/{id} | Read account |
| PUT | /accounts/{id} | Update account |
| DELETE | /accounts/{id} | Delete account |
| GET | /health | Health check |

## Technology Stack
- Python and Flask
- PostgreSQL and SQLAlchemy
- Git and GitHub
- GitHub Actions
- Docker
- Kubernetes and OpenShift
- Tekton Pipelines

## Project Structure
- service/ - Application and REST API
- tests/ - Automated tests
- deploy/ - Deployment resources
- tekton/ - CI/CD pipeline resources
- setup.cfg - Development tool configuration

## Testing
Run tests using:

    nosetests

## Author
Rutik Gadre

## License
Apache License 2.0

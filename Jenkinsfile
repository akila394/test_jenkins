pipeline{
    agent any

    stages{
        stage('Checkout') {
          steps{
            checkout scm
          }
        }

        stage('Setup Python'){
          steps{
            bat """
              python --version
              python -m venv .venv
              .venv\\Scripts\\python -m pip install --upgrade pip
              .venv\\Scripts\\python -m pip install -r requirements.txt
            """
          }
        }

        stage('Run tests'){
          steps{
            bat """
              .venv\\Scripts\\python -m pytest
            """
          }
        }
    }
}

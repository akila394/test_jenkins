pipeline{
    agent any

    environment{
      REPORT_DIR = "reports"
    }

    stages{
        stage('Checkout') {
          steps{
            checkout scm
          }
        }

        stage('Setup Python'){
          steps {
            bat """
              python -m venv .venv
              .venv\\Scripts\\python -m pip install -r requirements.txt
            """
          }
        }

        stage('Run tests'){
          steps{
            bat """
              if not exist %%REPORT_DIR%% mkdir %%REPORT_DIR%%
              .venv\\Scripts\\python -m pytest ^
              --junitxml=%REPORT_DIR%\\junit.xml ^
              --html=%REPORT_DIR%\\report.html ^
              --self-contained-html
            """
          }
        }
    }


    post {
      always {
        junit testResults: "reports/junit.xml",allowEmptyResults: true
        archiveArtifacts artifacts: 'reports/**', fingerprint: true
      }
    }
 }


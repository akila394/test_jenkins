pipeline{
    agent any

    environment{
      REPORT_DIR = "reports"
    }

    parameters {
      choice(name:'Suite', choices: ["smoke", "regression", "all"], description: 'which suits to run')
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

              set TEST_MARKER=
              if "%SUITE%"=="smoke" set TEST_MARKER=-m smoke
              if "%SUITE%"=="regression" set TEST_MARKER=-m regression

              .venv\\Scripts\\python -m pytest %TEST_MARKER% ^
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


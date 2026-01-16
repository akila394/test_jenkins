pipeline{
    agent any

    environment{
      VENV_PY = ".venv\\Scripts\\python"
      REPORT_DIR = "reports"
    }

    parameters {
      choice(name:'Suite', choices: ["smoke", "regression", "all"], description: 'which suits to run')
      choice(name:'ENV', choices: ["dev", "QA", "UAT", "prd"], description: 'which environment test to run')
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
              %VENV_PY% -m pip install -r requirements.txt
            """
          }
        }

        stage('Run tests'){
          steps{
            withCredentials([string(credentialId: 'calc-token', variable: 'TOKEN')]){
                bat """
              if not exist %%REPORT_DIR%% mkdir %%REPORT_DIR%%

              set TEST_MARKER=
              if "%SUITE%"=="smoke" set TEST_MARKER=-m smoke
              if "%SUITE%"=="regression" set TEST_MARKER=-m regression

              REM expose ENV to Python tests
              set ENV=%ENV%

             %VENV_PY% -m pytest %TEST_MARKER% ^
              --junitxml=%REPORT_DIR%\\junit.xml ^
              --html=%REPORT_DIR%\\report.html ^
              --self-contained-html
            """
            }

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


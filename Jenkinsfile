
pipeline {
    agent any

    options {
        timestamps()
    }

    stages {
        stage('Checkout') {
            steps {
                echo '代码由 Jenkins SCM 配置拉取'
            }
        }

        stage('Check Python') {
            steps {
                sh 'python3 --version'
                sh 'git --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv .venv
                    .venv/bin/python -m pip install -r requirements.txt
                '''
            }
        }

        stage('Run Pytest') {
            steps {
                sh '''
                    mkdir -p reports
                    .venv/bin/python -m pytest \
                      -v \
                      --junitxml=reports/junit.xml
                '''
            }
        }
    }

    post {
        always {
            junit testResults: 'reports/junit.xml',
                  allowEmptyResults: true
        }

        success {
            echo '测试执行成功'
        }

        failure {
            echo '测试执行失败，请查看控制台日志'
        }
    }
}

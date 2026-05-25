pipeline {
    agent any

    stages {

        stage('Check Python') {
            steps {
                sh 'python3 --version'
                sh 'pip3 --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m pip install --break-system-packages -r requirements.txt'
            }
        }

        stage('Train ML Model') {
            steps {
                sh 'python3 train_model.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ai-deployment-failure-predictor .'
            }
        }

        stage('Show Docker Images') {
            steps {
                sh 'docker images'
            }
        }
    }

    post {
        success {
            echo 'Pipeline executed successfully.'
        }

        failure {
            echo 'Pipeline failed.'
        }
    }
}
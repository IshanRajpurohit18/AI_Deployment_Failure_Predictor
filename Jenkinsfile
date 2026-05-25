pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Train ML Model') {
            steps {
                bat 'python train_model.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t ai-deployment-failure-predictor .'
            }
        }

        stage('Show Docker Images') {
            steps {
                bat 'docker images'
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
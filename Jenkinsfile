pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
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

pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/your-repo/project.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Train Model') {
            steps {
                sh 'python train_model.py'
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t deployment-failure-predictor .'
            }
        }
    }
}

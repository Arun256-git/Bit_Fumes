pipeline {
    agent any

    environment {
        IMAGE_NAME = 'arun256docker/fastapi-app:latest'
    }

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/Arun256-git/Python_FastAPI_Cloud.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    echo "Building Docker image: ${env.IMAGE_NAME}"
                    bat "docker build -t ${env.IMAGE_NAME} ."
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                    script {
                        bat """
                            docker context use default
                            echo %DOCKER_PASSWORD% | docker login -u %DOCKER_USERNAME% --password-stdin
                            docker push ${env.IMAGE_NAME}
                        """
                    }
                }
            }
        }

        stage('Clean Up Local Image') {
            steps {
                script {
                    bat "docker rmi ${env.IMAGE_NAME} || exit 0"
                }
            }
        }

        stage('Deploy (Optional)') {
            when {
                expression { return false } // Change to true when you implement deployment
            }
            steps {
                echo 'This stage is disabled.'
                // Insert deployment logic here
            }
        }
    }

    post {
        always {
            echo '✅ Jenkins pipeline finished.'
        }
        failure {
            echo '❌ Jenkins pipeline failed.'
        }
    }
}

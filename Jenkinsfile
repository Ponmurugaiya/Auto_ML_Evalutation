pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                // Checkout project from Git
                checkout scm
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image
                    sh 'docker build -t fraud-detection .'
                }
            }
        }
        stage('Run Evaluation') {
            steps {
                script {
                    // Run the Docker container for evaluation
                    sh 'docker run -v $(pwd)/reports:/app/reports fraud-detection'
                }
            }
        }
        stage('Archive Reports') {
            steps {
                // Archive the generated reports
                archiveArtifacts artifacts: 'reports/*', fingerprint: true
            }
        }
    }
    post {
        always {
            // Clean up workspace after run
            cleanWs()
        }
    }
}

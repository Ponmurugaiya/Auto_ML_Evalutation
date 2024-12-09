pipeline {
    agent any
    checkout([$class: 'GitSCM', 
          branches: [[name: '*/main']], 
          userRemoteConfigs: [[url: 'https://github.com/Ponmurugaiya/Auto_ML_Evalutation.git', 
                               credentialsId: 'GitHub_credentials']]])

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
                    bat 'docker build -t fraud-detection .'
                }
            }
        }
        stage('Run Evaluation') {
            steps {
                script {
                    // Run the Docker container for evaluation
                    bat 'docker run -v $(pwd)/reports:/app/reports fraud-detection'
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

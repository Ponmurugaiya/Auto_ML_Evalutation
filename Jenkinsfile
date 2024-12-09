pipeline {
    agent any

    environment {
        DATASET_URL = "https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud"
        KAGGLE_USERNAME = credentials('kaggle-username')
        KAGGLE_KEY = credentials('kaggle-key')
    }

    stages {
        stage('Checkout Code') {
            steps {
                git credentialsId: 'github-pat', url: 'https://github.com/Ponmurugaiya/Auto_ML_Evalutation.git', branch: 'main'
            }
        }

        stage('Build Docker Image') {
            steps {
                // Build the Docker image with necessary dependencies
                bat 'docker build -t automl-evaluation .'
            }
        }

        stage('Download Dataset') {
            steps {
                // Download dataset inside the Docker container
                bat '''
                docker run --rm ^
                -e KAGGLE_USERNAME=%KAGGLE_USERNAME% ^
                -e KAGGLE_KEY=%KAGGLE_KEY% ^
                -v "%CD%\\datasets:/app/datasets" ^
                automl-evaluation ^
                kaggle datasets download -d mlg-ulb/creditcardfraud --unzip -p /app/datasets
                '''
            }
        }

        stage('Train Model') {
            steps {
                // Train the model inside the Docker container
                bat '''
                docker run --rm ^
                -v "%CD%:/app" ^
                automl-evaluation ^
                python scripts/train_model.py
                '''
            }
        }

        stage('Evaluate Model') {
            steps {
                // Evaluate the model inside the Docker container
                bat '''
                docker run --rm ^
                -v "%CD%:/app" ^
                automl-evaluation ^
                python scripts/evaluate_model.py
                '''
            }
        }

        stage('Generate Report') {
            steps {
                // Generate the report inside the Docker container
                bat '''
                docker run --rm ^
                -v "%CD%:/app" ^
                automl-evaluation ^
                python scripts/generate_report.py
                '''
            }
        }
    }

    post {
        always {
            // Archive reports and logs
            archiveArtifacts artifacts: '**/reports/**', allowEmptyArchive: true
        }
        failure {
            // Notify on failure
            echo 'Pipeline failed!'
        }
    }
}

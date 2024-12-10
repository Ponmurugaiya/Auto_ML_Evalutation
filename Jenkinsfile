pipeline {
    agent any

    environment {
        DATASET_URL = "https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud"
        KAGGLE_USERNAME = credentials('kaggle-username') // Replace with your Jenkins credentials ID for Kaggle
        KAGGLE_KEY = credentials('kaggle-key') // Replace with your Jenkins credentials ID for Kaggle
    }

    stages {
        stage('Checkout Code') {
            steps {
                // Clone the repository
                git credentialsId: 'github-pat', 
                    url: 'https://github.com/Ponmurugaiya/Auto_ML_Evalutation.git', 
                    branch: 'main'
            }
        }

        stage('Build Docker Image') {
            steps {
                // Build Docker image with required dependencies
                bat 'docker build -t automl-evaluation .'
            }
        }

        stage('Download Dataset') {
            steps {
                // Download the dataset using Kaggle API inside Docker container
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
                // Train the model inside Docker container
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
                // Evaluate the model inside Docker container
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
                // Generate the report inside Docker container
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
            
            // Send email with the report
            emailext(
                subject: "Pipeline Execution Report: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: """
                The pipeline has completed successfully.

                - **Build URL**: ${env.BUILD_URL}
                - **Report**: Attached.

                Regards,
                Jenkins
                """,
                recipientProviders: [[$class: 'CulpritsRecipientProvider']],
                to: 'ponmurugaiya1@gmail.com',
                attachmentsPattern: '**/reports/model_report.pdf'
            )
        }
        failure {
            // Notify on failure
            emailext(
                subject: "Pipeline Failure: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: """
                The pipeline has failed.

                - **Build URL**: ${env.BUILD_URL}
                
                Please investigate the issue.
                """,
                to: 'ponmurugaiya1@gmail.com'
            )
            echo 'Pipeline failed!'
        }
    }
}

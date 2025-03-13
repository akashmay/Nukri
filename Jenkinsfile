pipeline {
    agent any  // This defines where the pipeline will run

    stages {
        stage('Checkout') {
            steps {
                script {
                    // Checkout code from Git repository
                    checkout scm
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    // Run pytest automation
                    sh 'pytest test_cases/update/update_headline.py -v -s --browser=chrome'
                }
            }
        }
    }
}

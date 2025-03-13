pipeline {
    agent any  // This defines where the pipeline will run
        tools {
        git 'Git'  // If you are using a custom Git installation
    }

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

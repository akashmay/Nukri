pipeline {
    agent any  // This defines where the pipeline will run
    tools {
        git 'Windows-git'  // If you are using a custom Git installation
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
                    // Run pytest automation using PowerShell on Windows
                    powershell '''
                        pytest test_cases\\update\\update_headline.py -v -s --browser=chrome
                    '''
                }
            }
        }
    }
}

pipeline {
    agent { label 'windows-slave' }  // Make sure this matches your Windows slave node label
    tools {
        git 'Windows Git'  // This should match the name you configured in Global Tool Configuration
    }
    stages {
        stage('Git Checkout') {
            steps {
                script {
                    // Checkout code from Git repository
                    checkout scm
                }
            }
        }
    }
}

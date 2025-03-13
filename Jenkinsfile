pipeline {
    agent { label 'windows-slave' }  // Make sure this matches your Windows slave node label
    tools {
        git 'Windows Git'  // Make sure this matches the Git tool name in Global Tool Configuration
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

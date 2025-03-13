pipeline {
    agent { label 'windows-slave' }  // Make sure this matches your Windows slave node label

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

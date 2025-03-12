pipeline {
    agent {
        label 'windows-agent'
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/akashmay/Nukri.git'
            }
        }
        stage('Setup Python') {
            steps {
                bat 'python -m venv venv'
                bat '.\\venv\\Scripts\\activate && pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                bat '.\\venv\\Scripts\\activate && pytest test_cases/'
            }
        }
        
    }
}

pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                echo "this is build"
                // git branch: 'main', url: 'https://github.com/akashmay/Nukri.git'
            }
        }
        stage('Setup Python') {
            steps {
                echo "this is setup python"
                // bat 'python -m venv venv'
                // bat '.\\venv\\Scripts\\activate && pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                echo "this is Running testn"
                // bat '.\\venv\\Scripts\\activate && pytest test_cases/'
            }
        }
        
    }
}

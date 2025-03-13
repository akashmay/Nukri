pipeline {
    agent {
        label 'windows-slave'  // Use the label of your Windows slave node
    }
    tools {
        git 'Windows Git'  // This should match the Git installation name configured for the Windows slave
    }
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

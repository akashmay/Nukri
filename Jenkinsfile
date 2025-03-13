pipeline {
    agent any  // This defines where the pipeline will run


    environment {
        PYTHON_VENV = 'C:\\jenkins\\python_venv'  // You can specify the path for your Python virtual environment
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

        stage('Setup Python Environment') {
            steps {
                script {
                    // Install Python dependencies from requirements.txt
                    powershell '''
                        # Create a virtual environment (if not exists)
                        if (!(Test-Path -Path $env:PYTHON_VENV)) {
                            python -m venv $env:PYTHON_VENV
                        }

                        # Activate the virtual environment
                        $env:VIRTUAL_ENV = $env:PYTHON_VENV
                        $env:PATH = "$env:VIRTUAL_ENV\\Scripts;$env:PATH"

                        # Install dependencies from requirements.txt
                        pip install --upgrade pip
                        pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    // Run pytest automation using PowerShell on Windows
                    powershell '''
                        # Ensure the virtual environment is activated
                        $env:VIRTUAL_ENV = $env:PYTHON_VENV
                        $env:PATH = "$env:VIRTUAL_ENV\\Scripts;$env:PATH"

                        # Run pytest automation
                        pytest test_cases\\update\\update_headline.py -v -s --browser=chrome
                    '''
                }
            }
        }
    }
}

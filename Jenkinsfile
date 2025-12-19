pipeline {
  agent {
    docker {
      image 'python_venv_pytest'
    }
  }

  //stages {
    //stage('Checkout from Git') {
      //steps {
        //git branch: 'calcul',
          //  url: 'https://github.com/FionaDoDev/my-python.git'
      //}
    //}

    stage('Run pytest') {
      steps {
        sh '''
          python --version
          pytest --version
          pytest
        '''
      }
    }
  }
}

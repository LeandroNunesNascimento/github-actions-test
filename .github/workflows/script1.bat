name: 'Run Bat File'
description: 'Run Bat File with parameters'
inputs:
  tipo:
    description: 'Tipo do bat'
    required: true
  int1:
    description: 'Number 1'
    required: true
  int2:
    description: 'Number 2'
    required: true
runs:
  using: "composite"
  steps:
    
    - name: condition teste
      if: inputs.tipo == 'teste'
      run: ${{ github.action_path }}\script1.bat ${{ inputs.int1 }} ${{ inputs.int2 }} ${{ inputs.tipo }}
      shell: cmd
    
    - name: condition producao
      if: inputs.tipo == 'producao'
      run: ${{ github.action_path }}\script2.bat
      shell: cmd

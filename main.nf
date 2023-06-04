#!/usr/bin/env nextflow
params.input_file = "Salary_Data.csv"
params.python_script = "process_data.py"
process runPythonScript {

    input:
    file input_file from file(params.input_file)

    output:
    stdout result

    script:
    """
    python3 "${params.python_script}" "${input_file}"
    """
}




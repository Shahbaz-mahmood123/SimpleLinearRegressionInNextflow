#!/usr/bin/env nextflow
params.input_file = "/Users/shahbazmahmood/workspace/nextflow-testing/python/Salary_Data.csv"

process runPythonScript {

    input:
    file input_file from file(params.input_file)

    output:
    stdout result

    script:
    """
    python3 /Users/shahbazmahmood/workspace/nextflow-testing/python/process_data.py "${input_file}"
    """
}




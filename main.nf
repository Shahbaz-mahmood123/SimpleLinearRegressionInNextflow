#!/usr/bin/env nextflow



process runPythonScript {

    params.input_data = "Hello, Nextflow!"

    input:
    val input_data from params.input_data

    output:
    stdout result

    script:
    """
    python3 /Users/shahbazmahmood/workspace/nextflow-testing/python/process_data.py "${input_data}"
    """
}




GENERAL INSTRUCTION
===================

1. to run experiment pipeline, from preprocessing raw data to final prediction result, do:

    $ cd exp

    $ sh run.sh

2. now trying libsvm with a subset of features, need to experiment with:
    - more features, and converting textual feature to numbers;
    - more libsvm configs, current config is default, maybe buggy for this project;

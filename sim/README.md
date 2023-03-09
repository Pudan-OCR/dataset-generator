# SIM Generator

SIM image generator

How to run:

* Cd to this directory
* In terminal run:

  ```
  main.py
  ```
  the datasets will be generated on **out** directory
* You also can run with several arguments:

  ```
  main.py -t <test> -n <number> -s <skew> -b <blur> -sp <salt_pepper>
  ```
* Arguments description:

  - `test` : true for test the program (dataset will not be generated)
  - `number` : (int) the number of the dataset will created (default = 10)
  - `skew` : (float) max skew angle in degree (default 3, 0 to switch off)
  - `blur` : (float) Max gaussian blur radius (default = 1.2, 0 to switch off)
  - `salt_pepper` : (int) max salt and pepper pixels (default = 5000)

### NAME
Fidelity plot

### VERSION
1.0

### AUTHOR
Khaos Research Group
Cristian Camilo Cuevas (cristianca@uma.es)

### DATE
23/06/2022

### DESCRIPTION
Convert a CSV file into EXCEL file.

### DOCKER
#### Build
```
docker build -t enbic2lab/flora/fidelityplot -f Fidelity_plot.dockerfile . 
```
#### Run
```
docker run -v $(pwd)/data:/usr/local/src/data/ docker.io/enbic2lab/flora/fidelityplot --filepath "data/support_snieves.csv" --delimiter ";"
```

### PARAMETERS
* filepath (str) --> Filepath for the input CSV File.
* delimiter (str) --> Delimiter of te input CSV File.

### OUTPUTS
* match.html
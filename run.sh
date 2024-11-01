# standard
g++ -o build/gauss src/gauss.cpp

# parallel
g++ -fopenmp src/gauss.cpp -o build/gauss

build/gauss 5 5 0.01 > results/gauss/output.txt
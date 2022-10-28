#!/opt/homebrew/bin/gnuplot -persist

set title "Location data"
set xlabel "location"
set ylabel "count"
set grid
plot "taxi.plt"

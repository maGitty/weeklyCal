 
pre =
"""
\documentclass[tikz]{standalone}% Does not support leap years.

%% Load needed packages
\usepackage{lmodern}
\usepackage{tikz}
    \usetikzlibrary{positioning}
\usepackage{ifthen}

%% Create needed conters  
    \newcounter{ThisYear}
    \newcounter{NewYearsDay}
    \newcounter{NewYearsWeek}
    \newcounter{NumberOfWeeksThisYear}
"""

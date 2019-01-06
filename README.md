***
# NYTimes-Twitter-Data-Aggregation-Big-Data-Analysis-and-Visualisation

## Project Summary

### Building a Big-Data production using the power of Python and Hadoop
We performed Data Aggregation, Big Data Analysis and Visualization which involves data aggregation from API exposed by NYTimes website and Twitter, then we applied classical big data analytic
method of MapReduce for perfroming word count on the unstructured data collected, usually text corpuses to build a visualised data product showing most trending words in the searched topic from NYTimes, using D3.js.
## Documentation
***
Report and documentation can be found on this [Report](https://github.com/jayantsolanki/NYTimes-Data-Aggregation-Big-Data-Analysis-and-Visualisation/tree/master/report) link

## Implementation
***
We created two scripts for collecting the data from NY Times and Twitter for five search topics. Data for whole week has been collected ranging from 1st April to 7th April, 2018. 
a. We chose 5 topics, trade war, donald trump, south china sea, cambridge analytica, and gun crime.
b. We then collected the data in the textcorpus folder and applied mapreduce to find the word count and word-co-occurrence count.
c. The csv files then generated were used in the d3js visualization.

#### Overall Workflow
<img src="https://github.com/jayantsolanki/NYTimes-Twitter-Data-Aggregation-Big-Data-Analysis-and-Visualisation/blob/master/report/images/flow.png" width=50% height=50%>

#### Word Cloud
<img src="https://github.com/jayantsolanki/NYTimes-Twitter-Data-Aggregation-Big-Data-Analysis-and-Visualisation/blob/master/report/images/imageedit_1_6249841619.png" width=50% height=50%>

#### Screencast description of the Live Project

[Video Download](https://buffalo.box.com/s/ltdluqv33nk36y9ojz4wk6bviyh8i03q)

## Folder Tree
***
* [**report**](https://github.com/jayantsolanki/NYTimes-Data-Aggregation-Big-Data-Analysis-and-Visualisation/tree/master/report) contains summary report detailing our implementation and results.
* [**codes**](https://github.com/jayantsolanki/NYTimes-Data-Aggregation-Big-Data-Analysis-and-Visualisation/tree/master/code)  contains the source code in python and ipython notebook
  1. Part1: Contains the data and the script files for the Lab1 chapter-wise (CH3,CH4,CH5 subfolders in it)
  2. Part2 : Contains the data and the script files for the Lab2 Nytimes and twitter folder contains the final csv files which are being
used for the web visualization. Input,output,output_co folders are used to store the text files which can be used further to perform the map-reduce operation.

## SOFTWARE/HARDWARE USED
* Anaconda
* Jupyter Notebook
* Python 3.6 Environment based on Anaconda
* Ubuntu 17, Intel core i7 processor
